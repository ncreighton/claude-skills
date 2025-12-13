---
name: knowledge-accumulator
description: Continuous learning system that extracts, stores, connects, and compounds knowledge across all conversations. Builds an ever-growing intelligence base from interactions, web searches, task executions, and discoveries. ALWAYS ACTIVE to ensure every interaction makes Claude smarter. Triggers on every conversation to extract learnings, when patterns are detected, when new information is discovered, or when user asks about past learnings.
---

# Knowledge Accumulator

24/7 learning system for continuous intelligence growth.

## Core Mission

Every interaction should make Claude smarter by:
- Extracting learnings from conversations
- Storing insights in memory
- Connecting related knowledge
- Building pattern recognition
- Compounding intelligence over time

## Learning Extraction Protocol

### After Every Conversation

```python
def extract_learnings(conversation):
    """Extract all learnable content from conversation."""
    
    learnings = {
        "facts": [],           # Concrete information
        "preferences": [],     # User preferences
        "patterns": [],        # Recurring behaviors
        "domain_knowledge": [],# Business-specific info
        "tool_insights": [],   # Tool usage learnings
        "error_lessons": [],   # What went wrong and why
        "optimizations": [],   # Better ways discovered
        "connections": [],     # Related topics linked
    }
    
    # Process conversation
    for message in conversation:
        # Extract facts
        facts = identify_factual_statements(message)
        learnings["facts"].extend(facts)
        
        # Identify preferences
        prefs = detect_preference_signals(message)
        learnings["preferences"].extend(prefs)
        
        # Spot patterns
        patterns = recognize_patterns(message, past_conversations)
        learnings["patterns"].extend(patterns)
    
    return learnings
```

### Learning Categories

#### 1. User Model
```yaml
nick_model:
  work_style:
    - Prefers bold, decisive action
    - Values creative control
    - Wants execution without permission-asking
    - Appreciates proactive suggestions
    
  communication:
    - Direct and efficient
    - Technical proficiency: expert
    - Tolerance for complexity: high
    
  priorities:
    current:
      - Automate all 17 sites
      - Scale KDP publishing
      - Launch agency services
    ongoing:
      - Minimal manual work
      - Maximum automation
      - Quality at scale
```

#### 2. Domain Knowledge
```yaml
publishing_empire:
  sites:
    witchcraft:
      - Main vertical
      - Mystical warmth tone
      - Beginner-friendly content
    smart_home:
      - Tech authority tone
      - Product reviews
      - CSS issue on homepage (LIVE)
    mythology:
      - Scholarly wonder tone
      - Research-heavy content
    # ... all 17 sites
    
  content_system:
    - ZimmWriter for generation
    - Make.com for automation (0 scenarios built)
    - MCP for WordPress control
    - Custom outlines per site
    
  tech_stack:
    - Docker, WSL2, Python
    - Hostinger hosting
    - WP-CLI access
    - Figma design system
```

#### 3. Tool Mastery
```yaml
tool_learnings:
  zimmwriter:
    - Custom outline format works best
    - Brand voice templates improve quality
    - Batch generation saves time
    
  mcp:
    - Browser MCP uses existing Chrome profile
    - Browserbase needs API keys
    - WordPress MCP enables direct control
    
  make_com:
    - CRITICAL: Zero scenarios built
    - Highest priority to set up
    - Can connect all systems
```

#### 4. Pattern Recognition
```yaml
detected_patterns:
  recurring_tasks:
    - Content publishing to multiple sites
    - Keyword research workflows
    - Plugin development cycles
    - SEO optimization passes
    
  preferences:
    - Files over inline responses
    - Action over explanation
    - Comprehensive over partial
    - Modern tech stack choices
    
  pain_points:
    - Manual content distribution
    - Repetitive WordPress tasks
    - Cross-site consistency
```

## Memory Integration

### Store Critical Learnings
```python
# Use memory_user_edits to persist learnings
memory_store = [
    "User operates 17 WordPress content sites",
    "Flagship vertical is witchcraft/spirituality",
    "Zero Make.com automation scenarios - critical bottleneck",
    "SmartHomeWizards.com homepage has CSS issue on LIVE",
    "Prefers bold execution without asking permission",
    "ZimmWriter is primary content generation tool",
    "All sites need automated hands-off content generation",
    # ... continues
]
```

### Retrieve and Connect
```python
# Before any task, gather relevant context
def gather_context(task):
    # Search past conversations
    relevant_chats = conversation_search(task_keywords)
    
    # Load user memories
    user_context = load_user_memories()
    
    # Connect related information
    connections = find_connections(task, relevant_chats, user_context)
    
    return synthesize_context(connections)
```

## Intelligence Compounding

### Level 1: Raw Facts
```
"User has 17 WordPress sites"
"ZimmWriter generates content"
"Make.com has zero scenarios"
```

### Level 2: Connected Insights
```
"17 sites need content → ZimmWriter generates → 
 But no Make.com automation → Manual distribution bottleneck"
```

### Level 3: Strategic Understanding
```
"The entire publishing empire is blocked by missing Make.com 
 automation. Solving this ONE issue unlocks automated content 
 distribution to ALL 17 sites, potentially 100x productivity."
```

### Level 4: Proactive Action
```
"Without being asked, prioritize:
 1. Building Make.com scenarios
 2. Connecting ZimmWriter → Make.com → WordPress MCP
 3. Creating monitoring for automated publishing"
```

## Learning Triggers

### Explicit Learning
```
User says: "Remember that I..."
Action: Store in memory immediately
```

### Implicit Learning
```
User demonstrates preference through actions
Action: Detect pattern, store as preference
```

### Error-Based Learning
```
Task fails or produces suboptimal result
Action: Analyze cause, store lesson, prevent recurrence
```

### Discovery-Based Learning
```
New information found via search/research
Action: Evaluate relevance, integrate if valuable
```

## Knowledge Graph

### Building Connections
```
                    ┌─────────────────┐
                    │     NICK        │
                    │   (User Model)  │
                    └────────┬────────┘
                             │
          ┌──────────────────┼──────────────────┐
          │                  │                  │
    ┌─────┴─────┐     ┌──────┴──────┐    ┌─────┴─────┐
    │ PUBLISHING│     │    TECH     │    │  BUSINESS │
    │   EMPIRE  │     │    STACK    │    │   GOALS   │
    └─────┬─────┘     └──────┬──────┘    └─────┬─────┘
          │                  │                  │
    ┌─────┴─────┐     ┌──────┴──────┐    ┌─────┴─────┐
    │ 17 Sites  │     │ ZimmWriter  │    │ Automate  │
    │ Content   │     │ Make.com    │    │ Scale     │
    │ Verticals │     │ MCP/Docker  │    │ Launch    │
    └───────────┘     └─────────────┘    └───────────┘
```

### Query Knowledge Graph
```python
def query_knowledge(topic):
    """Find all connected knowledge about a topic."""
    
    # Direct connections
    direct = graph.get_connections(topic)
    
    # Second-degree connections
    indirect = []
    for node in direct:
        indirect.extend(graph.get_connections(node))
    
    # Relevance scoring
    scored = score_by_relevance(direct + indirect, current_context)
    
    return sorted(scored, key=lambda x: x.relevance, reverse=True)
```

## Daily Learning Goals

### Minimum Daily Learning
```
☐ 1 new fact about user's business
☐ 1 pattern recognition
☐ 1 tool optimization
☐ 1 connection between topics
☐ 1 proactive suggestion made
```

### Weekly Knowledge Review
```
☐ Consolidate similar learnings
☐ Prune outdated information
☐ Strengthen key connections
☐ Identify knowledge gaps
☐ Plan learning priorities
```

## Proactive Knowledge Application

### Before Any Task
```python
def prepare_for_task(task):
    # What do I know that's relevant?
    relevant_knowledge = query_knowledge(task)
    
    # What worked before?
    past_successes = find_similar_successes(task)
    
    # What failed before?
    past_failures = find_similar_failures(task)
    
    # What does user prefer?
    preferences = get_relevant_preferences(task)
    
    # Synthesize approach
    approach = synthesize_best_approach(
        relevant_knowledge,
        past_successes,
        past_failures,
        preferences
    )
    
    return approach
```

### During Task Execution
```python
def learn_during_execution(task, progress):
    # What's working?
    if progress.success:
        store_success_pattern(task, progress)
    
    # What's challenging?
    if progress.difficulty:
        note_challenge(task, progress)
    
    # What's new?
    if progress.discovery:
        integrate_discovery(progress.discovery)
```

### After Task Completion
```python
def post_task_learning(task, result):
    # What was the outcome?
    outcome = evaluate_outcome(result)
    
    # What should be remembered?
    learnings = extract_learnings(task, result)
    
    # How to do better next time?
    optimizations = identify_optimizations(task, result)
    
    # Store everything
    store_learnings(learnings)
    store_optimizations(optimizations)
    update_user_model(task, result)
```

## Quick Commands

| Command | Action |
|---------|--------|
| "What do you know about X?" | Query knowledge graph |
| "What have you learned?" | Summarize recent learnings |
| "Remember this:" | Explicit memory storage |
| "Connect X to Y" | Create knowledge link |
| "What patterns do you see?" | Pattern analysis |
| "How have I changed?" | User model evolution |

## Always Active

This skill operates continuously:
- Extracting from every message
- Storing valuable insights
- Connecting related knowledge
- Building deeper understanding
- Making Claude smarter with every interaction

The goal: Claude should know more at the end of every conversation than at the beginning.
