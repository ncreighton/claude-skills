# CLAUDE.md Generator

## Purpose

**One job: Transform a DNA file into a self-contained CLAUDE.md for Claude Code projects.**

No fetching. No external dependencies. One file that contains everything Claude Code needs to build and maintain a site.

---

## When to Use

- Setting up a new Claude Code project for any of your 17 sites
- Updating a project's CLAUDE.md after DNA changes
- Creating CLAUDE.md for a new site

---

## Quick Start

```
Generate a CLAUDE.md for [site-name] using the CLAUDE.md Generator skill.
DNA file: /mnt/skills/user/creative-command-center/brains/[site-name].json
```

Or if you have the DNA content directly:
```
Generate a CLAUDE.md from this DNA: [paste DNA or upload file]
```

---

## What It Outputs

A single `CLAUDE.md` file containing:

```markdown
# [SITE NAME] - Claude Code Project

## Identity & Voice
[Extracted from DNA: archetype, soul, emotional tone, voice rules]

## Design Tokens
[Converted to actual CSS/Tailwind values - ready to use]

## Code Patterns
[WordPress/Blocksy patterns specific to this site]

## Content Rules
[Writing style, forbidden phrases, encouraged phrases]

## Anti-Patterns
[What to NEVER do - from DNA anti_patterns section]

## Technical Stack
[Deployment info, plugins, performance targets]

## Quick Reference
[Cheat sheet of most-used values]
```

---

## Process

### Step 1: Load DNA
Read the site's DNA file from Creative Command Center or accept pasted/uploaded content.

### Step 2: Extract & Transform
Pull each section and transform into actionable instructions:

| DNA Section | CLAUDE.md Section |
|-------------|-------------------|
| `archetype`, `soul`, `emotional_tone` | Identity & Voice |
| `colors.palette` | Design Tokens (CSS variables + Tailwind) |
| `typography` | Design Tokens (font stacks + scale) |
| `visual_philosophy`, `spacing_rhythm` | Design Tokens (spacing + effects) |
| `voice`, `cta_voice` | Content Rules |
| `anti_patterns` | Anti-Patterns |
| `technical` | Technical Stack |
| `seo` | SEO Configuration |

### Step 3: Generate Code-Ready Values

Transform design specs into actual code:

**DNA Input:**
```json
"primary": {
  "hex": "#6B46C1",
  "name": "Mystic Purple"
}
```

**CLAUDE.md Output:**
```css
--color-primary: #6B46C1;
```
```js
// tailwind.config.js
colors: {
  primary: '#6B46C1',
}
```

### Step 4: Add Project Context

Inject standard sections:
- File structure expectations
- Deployment workflow
- Testing checklist
- Common tasks

### Step 5: Output

Save to `/mnt/user-data/outputs/[site-name]-CLAUDE.md`

---

## Template Sections

### Required Sections (always included)
1. **Header** - Site name, last updated, DNA version
2. **Identity & Voice** - Who this site is
3. **Design Tokens** - All visual values
4. **Content Rules** - Writing guidelines
5. **Anti-Patterns** - What to never do
6. **Technical Stack** - Platform specifics
7. **Quick Reference** - Cheat sheet

### Optional Sections (based on DNA content)
- SEO Configuration (if `seo` section exists)
- Signature Elements (if `signature_elements` exists)
- Differentiation Notes (if `differentiation_from_*` exists)

---

## File Locations

- **Template:** `/mnt/skills/user/claudemd-generator/templates/claude-md-template.md`
- **Output:** `/mnt/user-data/outputs/[site-name]-CLAUDE.md`
- **Examples:** `/mnt/skills/user/claudemd-generator/examples/`

---

## Integration with Empire

```
┌─────────────────────────┐
│ Creative Command Center │
│ (DNA Files)             │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│ CLAUDE.md Generator     │◄─── YOU ARE HERE
│ (This Skill)            │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│ Claude Code Project     │
│ /CLAUDE.md              │
│ (Self-Contained)        │
└─────────────────────────┘
```

---

## Usage Examples

### Generate for Single Site
```
Generate CLAUDE.md for WitchcraftForBeginners
```

### Generate for All Sites (Batch)
```
Generate CLAUDE.md files for all 16 sites in Creative Command Center
```

### Update Existing
```
Regenerate CLAUDE.md for SmartHomeWizards - the DNA was updated
```

---

## Output Quality Checklist

Before delivering a CLAUDE.md, verify:

- [ ] All color tokens have CSS variables AND Tailwind config
- [ ] Typography includes actual font-family strings and sizes
- [ ] Spacing scale is complete (all values from DNA)
- [ ] Voice section has concrete examples, not just descriptions
- [ ] Anti-patterns are specific and actionable
- [ ] No references to "see DNA file" - everything is self-contained
- [ ] Quick Reference section has the 10 most-used values

---

## Maintenance

When a DNA file is updated in Creative Command Center:
1. Regenerate the CLAUDE.md
2. Copy to the Claude Code project
3. Commit to the project's git repo

This ensures Claude Code always has current instructions without fetching.
