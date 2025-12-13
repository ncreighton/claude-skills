# n8n Mastery Corpus Reference

This document consolidates core n8n concepts, patterns, and best practices for the AI architect agent.

## 1. Core Concepts

### Data Model
Each node receives an array of items:
```typescript
Array<{
  json: Record<string, any>;
  binary?: Record<string, BinaryData>;
}>
```

### Execution Modes
- **Manual** - Run from editor with sample data
- **Production** - Triggered by real events (webhooks, schedules)

### Credentials
n8n stores encrypted credentials. Nodes reference credentials by name; secrets are not in workflow JSON.

## 2. Node Engineering

### HTTP & Webhooks
- **HTTP Node** - Call external APIs (REST, GraphQL)
  - Use timeouts, retries, credentials
- **Webhook Node** - Start workflows on HTTP request
  - Validate → Normalize → Queue → Worker pattern

### Function/Code Nodes
- **Code** - Modern node for custom JavaScript/Python
  - Transform JSON shapes
  - Enforce schemas
  - Compute derived values

### Logic Nodes
- **IF** - Two-way branching
- **Switch** - Multi-way branching
- **Set** - Add, rename, delete fields
- **Merge** - Combine data streams

### Database Nodes
- Use parameter binding (prevent SQL injection)
- Use UPSERT for idempotency
- Prefer soft deletes

### Binary & Files
- Binary data lives in `item.binary`
- Typical: HTTP download → Binary → Storage/Processing

### Control Nodes
- **Execute Workflow** - Call sub-workflows
- **Split In Batches** - Process in chunks
- **Wait** - Pause execution

## 3. Architecture Patterns

### Architecture Layers
1. **Ingress** - Events enter (webhooks, schedulers)
2. **Routing/Validation** - Schema validation, normalization
3. **Queueing** - Persist work units
4. **Workers** - Process queued work
5. **Persistence** - Databases, storage
6. **Egress** - Notifications, external APIs

### Common Patterns

#### Event-Driven
```
Webhook → Validate → Normalize → Queue → Workers → Persist → Notify
```

#### Worker/Orchestrator
```
Orchestrator assigns tasks, Workers process
```

#### State Machine
```
Status fields: pending → in_progress → completed|failed
```

#### Microservice-Style
```
Each workflow = clear API contract
Compose via Execute Workflow nodes
```

### Scaling
- **Vertical** - More CPU/RAM per instance
- **Horizontal** - Multiple workers behind queues

## 4. AI Autonomy & Agent Systems

### Autonomy Components
- **Goals** - What to achieve
- **Planning** - Break goals into steps
- **Action** - Invoke tools (HTTP, DB, workflows)
- **Observation** - Inspect results
- **Reflection** - Evaluate success
- **Memory** - Short-term and long-term context
- **Guardrails** - Prevent unsafe behavior

### Agent Loop
1. **PLAN** - Decide next action
2. **ACT** - Call tool/node/workflow
3. **OBSERVE** - Inspect response
4. **REFLECT** - Evaluate outcome
5. **REPLAN** - Choose next step

### Memory Types
- **Short-term** - In-execution context
- **Long-term** - Stored in DB/files
- **Vector** - Embeddings for semantic search
- **Logs** - Historical traces

## 5. Content & Publishing Systems

### AI Blog Factory Pattern
```
Idea → Score → Outline → Draft → Edit → SEO → Publish → Link → Distribute
```

Workflows:
- `WS-BLOG-01: Idea Intake & Scoring`
- `WS-BLOG-02: Outline & Draft Generation`
- `WS-BLOG-03: Editing & Style Enforcement`
- `WS-BLOG-04: SEO & Structural Pass`
- `WS-BLOG-05: CMS Publishing`

### AI Substack Engine Pattern
```
Idea → Audience Analysis → Draft → Edit → Fact-Check → Format → Publish → Distribute
```

Tracks:
```json
{
  "post_id": "...",
  "status": "queued|drafted|edited|factchecked|ready_to_publish|published",
  "tier": "free|paid|subscribers_only"
}
```

### AI YouTube Script Factory
- **Shorts** (30-60 sec): Hook → Core idea → Payoff
- **Longform** (8-15 min): Chapters, pattern breaks, visuals

### AI Book Publishing
```
Research → Niche Validation → Outline → Chapter Drafts → Style Pass → Format → Cover → Launch
```

### AI Podcast Production
```
Plan → Record → Ingest → Transcribe → Notes → Chapters → Quotes → Clips → Distribute
```

## 6. Hard Rules

### MUST Do
- Idempotent designs (safe to retry)
- Logging to critical branches
- Error handlers and error workflows
- Small modular workflows (microservice-style)
- Strict JSON outputs from AI nodes
- Plan → Act → Observe → Reflect loops for agents

### MUST NOT Do
- Hallucinate n8n features
- Skip validation on webhooks
- Create monolithic workflows
- Hardcode secrets or environment values
- Destructive operations without confirmation

## 7. Tri-Style Documentation

### A) Formal Documentation
Precise, structured, minimal fluff. Technical manual style.

### B) Mentor/Explainer
Conversational, practical, explains WHY. Teaching style.

### C) AI-Agent Instruction
Rules for autonomous operation. MUST/MUST NOT language.

## 8. Design Mindset

Think like a senior automation architect designing:
- Event-driven systems
- Queue-based ingestion pipelines
- Multi-worker execution
- Orchestrator/worker patterns
- Microservice workflows
- High-availability installations
- Multi-tenant environments
- AI agent ecosystems
