#!/usr/bin/env python3
"""
Multi-Task Orchestrator.
Run multiple parallel AI agent tasks with dependency management.
"""

import asyncio
import json
import time
from datetime import datetime
from typing import List, Dict, Any, Callable, Optional
from dataclasses import dataclass, field, asdict
from enum import Enum
import traceback


class TaskStatus(Enum):
    PENDING = "pending"
    RUNNING = "running"
    SUCCESS = "success"
    FAILED = "failed"
    SKIPPED = "skipped"


@dataclass
class TaskResult:
    task_id: str
    status: TaskStatus
    output: Any = None
    error: Optional[str] = None
    duration: float = 0.0
    started_at: Optional[str] = None
    completed_at: Optional[str] = None


@dataclass
class Task:
    id: str
    name: str
    func: Callable
    args: tuple = field(default_factory=tuple)
    kwargs: dict = field(default_factory=dict)
    dependencies: List[str] = field(default_factory=list)
    timeout: float = 300.0
    retries: int = 3
    priority: int = 0  # Higher = more important


class Orchestrator:
    """Orchestrate parallel task execution with dependencies."""
    
    def __init__(self, max_concurrent: int = 5, on_failure: str = "continue"):
        self.max_concurrent = max_concurrent
        self.on_failure = on_failure  # continue, abort, retry
        self.semaphore = asyncio.Semaphore(max_concurrent)
        
        self.tasks: Dict[str, Task] = {}
        self.results: Dict[str, TaskResult] = {}
        self.task_events: Dict[str, asyncio.Event] = {}
        
        self.started_at: Optional[datetime] = None
        self.completed_at: Optional[datetime] = None
        self.aborted = False
    
    def add_task(self, task: Task):
        """Add a task to the orchestrator."""
        self.tasks[task.id] = task
        self.task_events[task.id] = asyncio.Event()
        self.results[task.id] = TaskResult(
            task_id=task.id,
            status=TaskStatus.PENDING
        )
    
    def add_tasks(self, tasks: List[Task]):
        """Add multiple tasks."""
        for task in tasks:
            self.add_task(task)
    
    async def _wait_for_dependencies(self, task: Task) -> bool:
        """Wait for all task dependencies to complete."""
        for dep_id in task.dependencies:
            if dep_id not in self.task_events:
                print(f"Warning: Unknown dependency {dep_id} for task {task.id}")
                continue
            
            # Wait for dependency to complete
            await self.task_events[dep_id].wait()
            
            # Check if dependency succeeded
            dep_result = self.results.get(dep_id)
            if dep_result and dep_result.status != TaskStatus.SUCCESS:
                if self.on_failure == "abort":
                    self.aborted = True
                    return False
                # Skip this task if dependency failed
                return False
        
        return True
    
    async def _execute_task(self, task: Task) -> TaskResult:
        """Execute a single task with retry logic."""
        result = self.results[task.id]
        
        # Wait for dependencies
        deps_ok = await self._wait_for_dependencies(task)
        if not deps_ok:
            result.status = TaskStatus.SKIPPED
            result.error = "Dependencies failed"
            self.task_events[task.id].set()
            return result
        
        # Check if aborted
        if self.aborted:
            result.status = TaskStatus.SKIPPED
            result.error = "Orchestration aborted"
            self.task_events[task.id].set()
            return result
        
        # Execute with semaphore
        async with self.semaphore:
            result.status = TaskStatus.RUNNING
            result.started_at = datetime.now().isoformat()
            
            last_error = None
            for attempt in range(task.retries):
                try:
                    start_time = time.time()
                    
                    # Execute task (handle both sync and async)
                    if asyncio.iscoroutinefunction(task.func):
                        output = await asyncio.wait_for(
                            task.func(*task.args, **task.kwargs),
                            timeout=task.timeout
                        )
                    else:
                        output = await asyncio.wait_for(
                            asyncio.get_event_loop().run_in_executor(
                                None, lambda: task.func(*task.args, **task.kwargs)
                            ),
                            timeout=task.timeout
                        )
                    
                    result.status = TaskStatus.SUCCESS
                    result.output = output
                    result.duration = time.time() - start_time
                    result.completed_at = datetime.now().isoformat()
                    break
                    
                except asyncio.TimeoutError:
                    last_error = f"Timeout after {task.timeout}s"
                except Exception as e:
                    last_error = f"{type(e).__name__}: {str(e)}"
                    traceback.print_exc()
                
                if attempt < task.retries - 1:
                    await asyncio.sleep(2 ** attempt)  # Exponential backoff
            
            if result.status != TaskStatus.SUCCESS:
                result.status = TaskStatus.FAILED
                result.error = last_error
                result.completed_at = datetime.now().isoformat()
                
                if self.on_failure == "abort":
                    self.aborted = True
        
        # Signal completion
        self.task_events[task.id].set()
        return result
    
    async def run(self) -> Dict[str, TaskResult]:
        """Run all tasks with dependency resolution."""
        self.started_at = datetime.now()
        self.aborted = False
        
        # Sort tasks by priority (higher first)
        sorted_tasks = sorted(
            self.tasks.values(),
            key=lambda t: t.priority,
            reverse=True
        )
        
        # Create all task coroutines
        coroutines = [self._execute_task(task) for task in sorted_tasks]
        
        # Run all tasks concurrently
        await asyncio.gather(*coroutines, return_exceptions=True)
        
        self.completed_at = datetime.now()
        return self.results
    
    def get_summary(self) -> Dict:
        """Get execution summary."""
        success = sum(1 for r in self.results.values() 
                     if r.status == TaskStatus.SUCCESS)
        failed = sum(1 for r in self.results.values() 
                    if r.status == TaskStatus.FAILED)
        skipped = sum(1 for r in self.results.values() 
                     if r.status == TaskStatus.SKIPPED)
        
        duration = None
        if self.started_at and self.completed_at:
            duration = (self.completed_at - self.started_at).total_seconds()
        
        return {
            "total": len(self.results),
            "success": success,
            "failed": failed,
            "skipped": skipped,
            "success_rate": f"{(success / len(self.results) * 100):.1f}%" if self.results else "0%",
            "duration_seconds": duration,
            "started_at": self.started_at.isoformat() if self.started_at else None,
            "completed_at": self.completed_at.isoformat() if self.completed_at else None,
            "aborted": self.aborted,
            "max_concurrent": self.max_concurrent
        }
    
    def get_results(self) -> Dict[str, Dict]:
        """Get all results as dict."""
        return {
            task_id: {
                "task_id": r.task_id,
                "status": r.status.value,
                "output": r.output,
                "error": r.error,
                "duration": r.duration,
                "started_at": r.started_at,
                "completed_at": r.completed_at
            }
            for task_id, r in self.results.items()
        }
    
    def print_report(self):
        """Print execution report."""
        summary = self.get_summary()
        
        print("\n" + "=" * 50)
        print("ORCHESTRATION REPORT")
        print("=" * 50)
        print(f"Total Tasks:    {summary['total']}")
        print(f"Success:        {summary['success']} ({summary['success_rate']})")
        print(f"Failed:         {summary['failed']}")
        print(f"Skipped:        {summary['skipped']}")
        print(f"Duration:       {summary['duration_seconds']:.2f}s")
        print(f"Max Concurrent: {summary['max_concurrent']}")
        
        if self.aborted:
            print("\n⚠️  ABORTED due to failure")
        
        # Print failed tasks
        failed_tasks = [r for r in self.results.values() 
                       if r.status == TaskStatus.FAILED]
        if failed_tasks:
            print("\nFAILED TASKS:")
            for r in failed_tasks:
                print(f"  - {r.task_id}: {r.error}")
        
        print("=" * 50 + "\n")


# Convenience functions for common patterns

async def parallel_map(func: Callable, items: List[Any], 
                       max_concurrent: int = 5) -> List[Any]:
    """Map a function over items in parallel."""
    orch = Orchestrator(max_concurrent=max_concurrent)
    
    for i, item in enumerate(items):
        orch.add_task(Task(
            id=f"item_{i}",
            name=f"Process item {i}",
            func=func,
            args=(item,)
        ))
    
    await orch.run()
    
    # Return results in order
    return [orch.results[f"item_{i}"].output for i in range(len(items))]


async def parallel_batch(tasks: List[Dict], 
                        max_concurrent: int = 5,
                        on_failure: str = "continue") -> Dict:
    """
    Run a batch of tasks in parallel.
    
    tasks format:
    [
        {"id": "task1", "func": some_func, "args": (arg1, arg2)},
        {"id": "task2", "func": other_func, "kwargs": {"key": "value"}},
    ]
    """
    orch = Orchestrator(max_concurrent=max_concurrent, on_failure=on_failure)
    
    for t in tasks:
        orch.add_task(Task(
            id=t["id"],
            name=t.get("name", t["id"]),
            func=t["func"],
            args=t.get("args", ()),
            kwargs=t.get("kwargs", {}),
            dependencies=t.get("dependencies", []),
            timeout=t.get("timeout", 300),
            retries=t.get("retries", 3),
            priority=t.get("priority", 0)
        ))
    
    await orch.run()
    orch.print_report()
    
    return {
        "summary": orch.get_summary(),
        "results": orch.get_results()
    }


# Example usage and testing

async def example_task(task_num: int, delay: float = 1.0) -> str:
    """Example async task."""
    await asyncio.sleep(delay)
    return f"Task {task_num} completed"


async def example_failing_task() -> str:
    """Example task that fails."""
    raise ValueError("Intentional failure")


async def main():
    """Run example orchestration."""
    print("Running example orchestration...")
    
    # Create orchestrator
    orch = Orchestrator(max_concurrent=3)
    
    # Add tasks with dependencies
    orch.add_task(Task(
        id="setup",
        name="Setup environment",
        func=example_task,
        args=(0, 0.5)
    ))
    
    orch.add_task(Task(
        id="task_a",
        name="Task A",
        func=example_task,
        args=(1, 1.0),
        dependencies=["setup"]
    ))
    
    orch.add_task(Task(
        id="task_b",
        name="Task B",
        func=example_task,
        args=(2, 1.5),
        dependencies=["setup"]
    ))
    
    orch.add_task(Task(
        id="task_c",
        name="Task C",
        func=example_task,
        args=(3, 0.8),
        dependencies=["setup"]
    ))
    
    orch.add_task(Task(
        id="aggregate",
        name="Aggregate results",
        func=example_task,
        args=(4, 0.3),
        dependencies=["task_a", "task_b", "task_c"]
    ))
    
    # Run
    await orch.run()
    orch.print_report()
    
    # Show results
    print("\nResults:")
    for task_id, result in orch.get_results().items():
        print(f"  {task_id}: {result['status']} - {result['output']}")


if __name__ == "__main__":
    asyncio.run(main())
