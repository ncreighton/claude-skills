---
name: multi-task-orchestrator
description: Orchestration system for running multiple parallel AI agent tasks across web and automation workflows. Enables superhuman productivity through concurrent execution, task decomposition, dependency management, and result aggregation. Use when user needs to run multiple tasks simultaneously, automate across multiple sites, batch process operations, parallelize workflows, or coordinate complex multi-step automations. Triggers include "parallel", "simultaneously", "batch", "multiple sites", "all at once", "concurrent", "automate all", "orchestrate", "coordinate tasks", or any multi-task requests.
---

# Multi-Task Orchestrator

Superhuman productivity through intelligent parallel task execution.

## Core Capabilities

### Task Decomposition
- Break complex tasks into parallel units
- Identify independent vs dependent steps
- Optimize execution order
- Minimize total completion time

### Parallel Execution
- Run multiple browser sessions
- Execute independent API calls concurrently
- Process files in parallel
- Coordinate cross-service operations

### Dependency Management
- Build task dependency graphs
- Execute in optimal order
- Pass results between tasks
- Handle failure cascades

### Result Aggregation
- Collect outputs from all tasks
- Merge into unified results
- Generate summary reports
- Identify partial failures

## Orchestration Patterns

### Pattern 1: Multi-Site Data Collection
```
┌─────────────────────────────────────────┐
│           ORCHESTRATOR                  │
├─────────────────────────────────────────┤
│                                         │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐ │
│  │ Site A  │  │ Site B  │  │ Site C  │ │
│  │ Extract │  │ Extract │  │ Extract │ │
│  └────┬────┘  └────┬────┘  └────┬────┘ │
│       │            │            │       │
│       └────────────┼────────────┘       │
│                    │                    │
│              ┌─────┴─────┐              │
│              │ AGGREGATE │              │
│              │  RESULTS  │              │
│              └───────────┘              │
└─────────────────────────────────────────┘
```

### Pattern 2: Content Publishing Pipeline
```
┌────────────────────────────────────────────────┐
│                ORCHESTRATOR                    │
├────────────────────────────────────────────────┤
│                                                │
│  ┌──────────────────────────────────────┐     │
│  │     CONTENT GENERATION (Serial)      │     │
│  │  Research → Write → Edit → Optimize  │     │
│  └─────────────────┬────────────────────┘     │
│                    │                          │
│  ┌─────────────────┴─────────────────────┐   │
│  │      PUBLISHING (Parallel)            │   │
│  │                                       │   │
│  │  ┌────────┐ ┌────────┐ ┌────────┐   │   │
│  │  │ WP #1  │ │ WP #2  │ │ WP #3  │   │   │
│  │  │ Post   │ │ Post   │ │ Post   │   │   │
│  │  └────────┘ └────────┘ └────────┘   │   │
│  └───────────────────────────────────────┘   │
└────────────────────────────────────────────────┘
```

### Pattern 3: Account Management
```
┌─────────────────────────────────────────────┐
│              ORCHESTRATOR                   │
├─────────────────────────────────────────────┤
│                                             │
│  Load Credentials from Vault                │
│              │                              │
│  ┌───────────┼───────────┐                 │
│  │           │           │                 │
│  ▼           ▼           ▼                 │
│ ┌───────┐ ┌───────┐ ┌───────┐            │
│ │Gmail  │ │Twitter│ │LinkedIn│            │
│ │Check  │ │Post   │ │Update  │            │
│ │Inbox  │ │Update │ │Status  │            │
│ └───┬───┘ └───┬───┘ └───┬───┘            │
│     │         │         │                 │
│     └─────────┼─────────┘                 │
│               │                           │
│         ┌─────┴─────┐                     │
│         │  REPORT   │                     │
│         │ SUMMARY   │                     │
│         └───────────┘                     │
└─────────────────────────────────────────────┘
```

## Task Definition Format

```yaml
orchestration:
  name: "Multi-Site Content Sync"
  mode: parallel  # parallel | sequential | mixed
  
  tasks:
    - id: extract_site_a
      type: browser_automation
      config:
        url: "https://site-a.com/content"
        action: extract
        selector: ".article-list"
      dependencies: []
      
    - id: extract_site_b
      type: browser_automation
      config:
        url: "https://site-b.com/feed"
        action: extract
        selector: ".posts"
      dependencies: []
      
    - id: merge_content
      type: data_processing
      config:
        action: merge
        inputs: ["extract_site_a.output", "extract_site_b.output"]
      dependencies: [extract_site_a, extract_site_b]
      
    - id: publish_all
      type: multi_publish
      config:
        destinations:
          - site_a: "${merged_content}"
          - site_b: "${merged_content}"
          - site_c: "${merged_content}"
      dependencies: [merge_content]

  on_failure:
    strategy: continue  # continue | abort | retry
    max_retries: 3
    notify: true
```

## Execution Strategies

### Full Parallel
All independent tasks run simultaneously.
```
Best for: Independent site operations, data collection
Example: Scraping 10 different sites at once
```

### Staged Parallel
Groups of parallel tasks with serial dependencies.
```
Best for: Publishing pipelines, ETL workflows
Example: Generate content (serial) → Publish to all sites (parallel)
```

### Rate-Limited Parallel
Parallel execution with concurrency limits.
```
Best for: API-bound operations, avoiding rate limits
Example: Process 100 items, 5 at a time
```

### Priority Queue
Tasks executed by priority with parallel capacity.
```
Best for: Mixed urgency operations
Example: Critical updates first, then batch operations
```

## Implementation Helpers

### Python Async Orchestrator
```python
import asyncio
from typing import List, Dict, Any

class TaskOrchestrator:
    def __init__(self, max_concurrent: int = 5):
        self.max_concurrent = max_concurrent
        self.semaphore = asyncio.Semaphore(max_concurrent)
        self.results = {}
        
    async def execute_task(self, task_id: str, task_func, *args):
        """Execute single task with semaphore control."""
        async with self.semaphore:
            try:
                result = await task_func(*args)
                self.results[task_id] = {"status": "success", "data": result}
            except Exception as e:
                self.results[task_id] = {"status": "error", "error": str(e)}
        return self.results[task_id]
    
    async def run_parallel(self, tasks: List[Dict]):
        """Run multiple tasks in parallel."""
        coroutines = [
            self.execute_task(t["id"], t["func"], *t.get("args", []))
            for t in tasks
        ]
        await asyncio.gather(*coroutines, return_exceptions=True)
        return self.results
    
    def get_summary(self) -> Dict:
        """Get execution summary."""
        success = sum(1 for r in self.results.values() if r["status"] == "success")
        failed = sum(1 for r in self.results.values() if r["status"] == "error")
        return {
            "total": len(self.results),
            "success": success,
            "failed": failed,
            "results": self.results
        }
```

### Browser Session Pool
```python
class BrowserSessionPool:
    def __init__(self, pool_size: int = 5):
        self.pool_size = pool_size
        self.sessions = []
        self.available = asyncio.Queue()
        
    async def initialize(self):
        """Create browser session pool."""
        for _ in range(self.pool_size):
            session = await create_browser_session()
            await self.available.put(session)
            self.sessions.append(session)
    
    async def acquire(self):
        """Get available session from pool."""
        return await self.available.get()
    
    async def release(self, session):
        """Return session to pool."""
        await self.available.put(session)
    
    async def execute_on_pool(self, tasks):
        """Execute tasks using session pool."""
        async def run_task(task):
            session = await self.acquire()
            try:
                return await task(session)
            finally:
                await self.release(session)
        
        return await asyncio.gather(*[run_task(t) for t in tasks])
```

## Integration Points

### With Browser Automation
- Maintain session pool for parallel browsing
- Share credential vault across sessions
- Coordinate navigation to avoid conflicts

### With Credential Vault
- Load all needed credentials at orchestration start
- Distribute to parallel sessions
- Collect updated sessions at end

### With Smart Operator Core
- Apply operator principles to each sub-task
- Maintain proactive behavior across parallel streams
- Aggregate insights from all tasks

## Error Handling Matrix

| Scenario | Strategy |
|----------|----------|
| Single task fails | Log, continue others, report in summary |
| Dependency fails | Skip dependent tasks, report chain |
| Rate limit hit | Backoff, retry with delay |
| Session expires | Refresh and retry task |
| Full failure | Abort remaining, report status |

## Monitoring & Reporting

### Real-time Status
```
[██████████████░░░░░░] 70% Complete
├─ Site A: ✓ Complete (2.3s)
├─ Site B: ✓ Complete (1.8s)
├─ Site C: ⏳ Running...
├─ Site D: ⏳ Queued
└─ Site E: ✗ Failed (retry 1/3)
```

### Summary Report
```
ORCHESTRATION COMPLETE
═══════════════════════════════════════
Tasks:      25 total
Success:    23 (92%)
Failed:     2 (8%)
Duration:   45.2 seconds
Parallel:   5 concurrent max

FAILURES:
- Task #12 (site-e.com): Connection timeout
- Task #19 (api-call): Rate limited

OUTPUTS:
- /outputs/aggregated_results.json
- /outputs/execution_log.txt
═══════════════════════════════════════
```

## Quick Reference

| Goal | Approach |
|------|----------|
| Maximum speed | Full parallel, high concurrency |
| Rate limit safe | Staged parallel, low concurrency |
| Complex pipeline | Dependency graph, mixed mode |
| Resource limited | Priority queue, session pool |

## Resources

- **scripts/orchestrator.py** - Core orchestration engine
- **scripts/session_pool.py** - Browser session pooling
- **scripts/dependency_resolver.py** - Task dependency management
- **references/patterns.md** - Common orchestration patterns
