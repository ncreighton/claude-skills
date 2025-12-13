---
name: auto-skill-generator
description: Automatically generates new Claude skills from detected patterns, repeated workflows, and identified needs. Transforms recurring tasks into reusable skills, codifies domain knowledge, and expands capabilities through self-authoring. Use when patterns are detected that would benefit from skill creation, when user requests skill creation, or when capability gaps would be solved by a new skill. Triggers include "create skill", "make skill for", "automate this", when same workflow detected 3+ times, or when manual workaround is being used repeatedly.
---

# Auto-Skill Generator

Self-authoring system for continuous skill expansion.

## Core Mission

Transform patterns into power by:
- Detecting repeated workflows
- Identifying skill opportunities
- Auto-generating skill files
- Testing and validating skills
- Expanding capabilities automatically

## Skill Generation Triggers

### Automatic Triggers
```python
triggers = {
    # Pattern-based
    "same_task_3x": "Task performed 3+ times identically",
    "manual_workaround": "Using workaround instead of proper solution",
    "multi_step_repetition": "Same multi-step process repeated",
    
    # Gap-based
    "capability_missing": "Desired capability doesn't exist",
    "tool_limitation": "Current tools can't do what's needed",
    "integration_needed": "Need to connect systems",
    
    # Request-based
    "user_request": "User explicitly asks for skill",
    "suggested_skill": "Self-evolution engine recommends",
}
```

### Detection Algorithm
```python
def detect_skill_opportunity(conversation_history):
    """Detect when a skill should be created."""
    
    # Pattern frequency analysis
    patterns = extract_patterns(conversation_history)
    repeated = [p for p in patterns if p.frequency >= 3]
    
    # Manual workaround detection
    workarounds = detect_workarounds(conversation_history)
    
    # Complexity analysis
    complex_tasks = [t for t in tasks if t.steps >= 5]
    
    # Generate opportunities
    opportunities = []
    
    for pattern in repeated:
        opportunities.append({
            "type": "repeated_pattern",
            "pattern": pattern,
            "benefit": f"Saves {pattern.frequency * pattern.time} minutes",
            "priority": calculate_priority(pattern)
        })
    
    for workaround in workarounds:
        opportunities.append({
            "type": "workaround_replacement",
            "current": workaround,
            "benefit": "Proper solution vs hack",
            "priority": "HIGH"
        })
    
    return opportunities
```

## Skill Generation Process

### Step 1: Analyze Pattern
```python
def analyze_pattern(pattern):
    """Deep analysis of pattern for skill creation."""
    
    analysis = {
        "inputs": identify_inputs(pattern),
        "outputs": identify_outputs(pattern),
        "steps": decompose_steps(pattern),
        "variations": find_variations(pattern),
        "dependencies": identify_dependencies(pattern),
        "error_cases": identify_errors(pattern),
    }
    
    return analysis
```

### Step 2: Design Skill Structure
```python
def design_skill(analysis):
    """Design the skill structure."""
    
    skill_design = {
        "name": generate_skill_name(analysis),
        "description": generate_description(analysis),
        "triggers": generate_triggers(analysis),
        
        "structure": {
            "SKILL.md": design_skill_md(analysis),
            "scripts": design_scripts(analysis),
            "references": design_references(analysis),
            "assets": design_assets(analysis),
        },
        
        "integration_points": identify_integrations(analysis),
    }
    
    return skill_design
```

### Step 3: Generate Files
```python
def generate_skill_files(design):
    """Generate all skill files."""
    
    # Create SKILL.md
    skill_md = f"""---
name: {design['name']}
description: {design['description']}
---

# {design['name'].replace('-', ' ').title()}

{generate_overview(design)}

## Quick Start

{generate_quickstart(design)}

## Capabilities

{generate_capabilities(design)}

## Usage

{generate_usage(design)}

## Integration

{generate_integration(design)}
"""
    
    # Create scripts
    scripts = {}
    for script in design['structure']['scripts']:
        scripts[script['name']] = generate_script(script)
    
    # Create references
    references = {}
    for ref in design['structure']['references']:
        references[ref['name']] = generate_reference(ref)
    
    return {
        "SKILL.md": skill_md,
        "scripts": scripts,
        "references": references,
    }
```

### Step 4: Validate & Package
```python
def validate_and_package(skill_files, skill_name):
    """Validate skill and create package."""
    
    # Write files
    skill_path = f"/home/claude/skills/{skill_name}"
    write_skill_files(skill_path, skill_files)
    
    # Validate
    validation = run_validation(skill_path)
    if not validation.success:
        fix_issues(skill_path, validation.issues)
    
    # Package
    package_path = package_skill(skill_path)
    
    return package_path
```

## Skill Templates

### Automation Skill Template
```yaml
template: automation
structure:
  SKILL.md:
    sections:
      - overview
      - configuration
      - workflow_steps
      - error_handling
      - integration
  scripts:
    - main_automation.py
    - config_loader.py
  references:
    - config_schema.json
```

### Integration Skill Template
```yaml
template: integration
structure:
  SKILL.md:
    sections:
      - overview
      - api_reference
      - authentication
      - endpoints
      - examples
  scripts:
    - api_client.py
    - auth_handler.py
  references:
    - api_docs.md
    - endpoints.json
```

### Domain Knowledge Skill Template
```yaml
template: domain_knowledge
structure:
  SKILL.md:
    sections:
      - overview
      - key_concepts
      - workflows
      - best_practices
      - glossary
  references:
    - concepts.md
    - examples.md
    - glossary.json
```

### Multi-Site Skill Template
```yaml
template: multi_site
structure:
  SKILL.md:
    sections:
      - overview
      - site_configuration
      - per_site_customization
      - batch_operations
      - monitoring
  scripts:
    - site_manager.py
    - batch_processor.py
  references:
    - site_configs.json
    - site_templates/
```

## Pattern-to-Skill Examples

### Example 1: Content Publishing Pattern
```yaml
detected_pattern:
  name: "Multi-site content publishing"
  frequency: 15 times
  steps:
    - Generate content with ZimmWriter
    - Format for each site's style
    - Add site-specific elements
    - Publish to WordPress
    - Update internal links
  time_per_execution: 45 minutes
  
generated_skill:
  name: "multi-site-publisher"
  benefit: "Reduces 45 min to 5 min"
  
  SKILL.md: |
    ---
    name: multi-site-publisher
    description: One-click content publishing to all 17 WordPress 
    sites with automatic formatting, style adaptation, and link 
    management. Triggers on "publish everywhere", "post to all sites",
    "distribute content".
    ---
    
    # Multi-Site Publisher
    
    Publish content to all 17 sites simultaneously.
    
    ## Quick Publish
    
    Simply say: "Publish this to all sites"
    
    ## Site-Specific Formatting
    
    Each site gets content adapted to its voice:
    - Witchcraft: Mystical warmth
    - Smart Home: Tech authority
    - Mythology: Scholarly wonder
    ...
```

### Example 2: SEO Workflow Pattern
```yaml
detected_pattern:
  name: "SEO content optimization"
  frequency: 20 times
  steps:
    - Keyword research
    - Competitor analysis
    - Content outline
    - Draft creation
    - SEO optimization
    - Internal linking
  
generated_skill:
  name: "seo-content-pipeline"
  benefit: "Automated end-to-end SEO content"
```

### Example 3: Site Maintenance Pattern
```yaml
detected_pattern:
  name: "WordPress maintenance"
  frequency: 17 times (once per site)
  steps:
    - Check plugin updates
    - Review security status
    - Optimize database
    - Clear caches
    - Check broken links
  
generated_skill:
  name: "wp-maintenance-automator"
  benefit: "Batch maintenance for all sites"
```

## Self-Improvement Integration

### Feed Patterns to Generator
```python
# From self-evolution-engine
patterns = self_evolution.get_detected_patterns()

for pattern in patterns:
    if pattern.frequency >= 3 and pattern.complexity >= "medium":
        skill_opportunity = auto_skill_generator.analyze(pattern)
        
        if skill_opportunity.value_score > 70:
            # Generate the skill
            new_skill = auto_skill_generator.create(skill_opportunity)
            
            # Notify user
            suggest_skill_adoption(new_skill)
```

### From Knowledge Accumulator
```python
# Domain knowledge that should become skills
domain_knowledge = knowledge_accumulator.get_domain_insights()

for domain in domain_knowledge:
    if domain.complexity >= "high" and domain.reusability >= "frequent":
        # Create knowledge skill
        skill = auto_skill_generator.create_knowledge_skill(domain)
```

## Skill Quality Standards

### Must Have
```
☐ Clear, comprehensive description
☐ Specific trigger phrases
☐ Working code (if scripts)
☐ Error handling
☐ Usage examples
☐ Integration points documented
```

### Should Have
```
☐ Quick start section
☐ Configuration options
☐ Troubleshooting guide
☐ Performance considerations
```

### Nice to Have
```
☐ Advanced usage patterns
☐ Alternative approaches
☐ Version history
☐ Community contributions
```

## Quick Commands

| Command | Action |
|---------|--------|
| "Create skill for X" | Generate skill from description |
| "What skills should exist?" | Analyze patterns, suggest skills |
| "Turn this into a skill" | Convert current workflow |
| "Package skill X" | Create .skill file |
| "Validate skill X" | Check skill quality |
| "Improve skill X" | Enhance existing skill |

## Skill Lifecycle

```
┌─────────────────────────────────────────────────────┐
│               SKILL LIFECYCLE                        │
├─────────────────────────────────────────────────────┤
│                                                     │
│  ┌─────────┐    ┌─────────┐    ┌─────────┐        │
│  │ DETECT  │ →  │ DESIGN  │ →  │GENERATE │        │
│  │ Pattern │    │ Skill   │    │ Files   │        │
│  └────┬────┘    └────┬────┘    └────┬────┘        │
│       │              │              │              │
│       └──────────────┼──────────────┘              │
│                      │                             │
│                 ┌────┴────┐                        │
│                 │VALIDATE │                        │
│                 └────┬────┘                        │
│                      │                             │
│                 ┌────┴────┐                        │
│                 │ PACKAGE │                        │
│                 └────┬────┘                        │
│                      │                             │
│                 ┌────┴────┐                        │
│                 │  ADOPT  │                        │
│                 └────┬────┘                        │
│                      │                             │
│                 ┌────┴────┐                        │
│                 │ ITERATE │ → [Back to DETECT]     │
│                 └─────────┘                        │
└─────────────────────────────────────────────────────┘
```

The generator continuously creates new skills from patterns, expanding Claude's capabilities automatically.
