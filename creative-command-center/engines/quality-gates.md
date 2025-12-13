# 🚦 QUALITY GATES

## PURPOSE

Quality Gates are **mandatory checkpoints** between phases.

Every phase must pass its gate before proceeding.
**There is no skipping. There is no "we'll fix it later."**

---

## GATE OVERVIEW

```
┌────────────────────────────────────────────────────────────────┐
│                                                                │
│  CREATIVE DIRECTOR                                             │
│         │                                                      │
│         ▼                                                      │
│    ╔═══════════╗                                              │
│    ║  GATE 1   ║  Vision Clarity Gate                         │
│    ╚═══════════╝                                              │
│         │                                                      │
│         ▼                                                      │
│  UX ARCHITECT                                                  │
│         │                                                      │
│         ▼                                                      │
│    ╔═══════════╗                                              │
│    ║  GATE 2   ║  Flow Integrity Gate                         │
│    ╚═══════════╝                                              │
│         │                                                      │
│         ▼                                                      │
│  SEO ENGINEER                                                  │
│         │                                                      │
│         ▼                                                      │
│    ╔═══════════╗                                              │
│    ║  GATE 3   ║  Structure Validity Gate                     │
│    ╚═══════════╝                                              │
│         │                                                      │
│         ▼                                                      │
│  WORDPRESS ENGINEER                                            │
│         │                                                      │
│         ▼                                                      │
│    ╔═══════════╗                                              │
│    ║  GATE 4   ║  Implementation Quality Gate                 │
│    ╚═══════════╝                                              │
│         │                                                      │
│         ▼                                                      │
│  BRUTAL CRITIC                                                 │
│         │                                                      │
│         ▼                                                      │
│    ╔═══════════╗                                              │
│    ║  GATE 5   ║  Final Approval Gate                         │
│    ╚═══════════╝                                              │
│         │                                                      │
│         ▼                                                      │
│    PRODUCTION                                                  │
│                                                                │
└────────────────────────────────────────────────────────────────┘
```

---

## GATE 1: VISION CLARITY GATE

**After:** Creative Director completes Design Brief
**Before:** UX Architect begins

### Checklist

```
MANDATORY (all must pass):

□ Soul statement exists and is specific to THIS site
  Test: Does it work for any other site? (Must fail)

□ Emotional journey is mapped with specific stages
  Test: Are emotions generic ("positive") or specific ("reverent curiosity")?

□ Archetype alignment is explicit
  Test: Is the archetype named and applied?

□ Sensory profile is complete
  Test: Can you imagine the sound, texture, temperature?

□ At least 2 signature moments defined
  Test: Are they memorable or generic?

□ Prohibitions are specific, not generic
  Test: Are prohibitions for THIS site or generic advice?

□ Zero code appears anywhere
  Test: Search for CSS, HTML, JavaScript mentions

□ Passes the "could this brief be for any site" test
  Test: Remove site name - is it still clearly for this site?
```

### Pass Criteria

**ALL boxes must be checked.**

### Fail Actions

| Failure | Action |
|---------|--------|
| Generic soul statement | Revise until specific |
| Vague emotional journey | Specify with concrete emotions |
| Missing prohibitions | Add site-specific forbidden patterns |
| Code present | Remove all code, Creative Director doesn't code |

### Gate 1 Declaration

```
═══════════════════════════════════════════════════════════════
GATE 1: VISION CLARITY
Result: [PASS / FAIL]
Timestamp: [DateTime]

Checklist: [X/8] items passed

If FAIL:
Failed Items: [List]
Required Fix: [Description]
Return To: Creative Director

If PASS:
Proceed To: UX Architect
═══════════════════════════════════════════════════════════════
```

---

## GATE 2: FLOW INTEGRITY GATE

**After:** UX Architect completes User Flow Document
**Before:** SEO Engineer begins

### Checklist

```
MANDATORY (all must pass):

□ Entry points analyzed for all traffic types
  Test: Are organic, direct, social, return visitors considered?

□ Information hierarchy defined with L1-L5 levels
  Test: Is there only ONE L1 per viewport?

□ Pacing pattern chosen and justified
  Test: Does pacing match the site archetype?

□ Section flow mapped with connections
  Test: Are transitions between sections defined?

□ Scroll experience designed (not generic)
  Test: Is first scroll moment specifically designed?

□ Navigation philosophy defined
  Test: Does nav approach match site purpose?

□ Interaction concepts are conceptual, not coded
  Test: No CSS/JS in the document

□ No visual design decisions made
  Test: No colors, fonts, or specific pixel values

□ Aligns with Creative Director's vision
  Test: Does it honor the soul statement and emotional journey?
```

### Pass Criteria

**ALL boxes must be checked.**

### Fail Actions

| Failure | Action |
|---------|--------|
| Multiple L1 elements | Reduce to single L1 per viewport |
| Visual decisions | Remove, return to concept level |
| Pacing mismatch | Align with archetype |
| Vision conflict | Return to Creative Director for alignment |

### Gate 2 Declaration

```
═══════════════════════════════════════════════════════════════
GATE 2: FLOW INTEGRITY
Result: [PASS / FAIL]
Timestamp: [DateTime]

Checklist: [X/9] items passed

If FAIL:
Failed Items: [List]
Required Fix: [Description]
Return To: UX Architect

If PASS:
Proceed To: SEO Structural Engineer
═══════════════════════════════════════════════════════════════
```

---

## GATE 3: STRUCTURE VALIDITY GATE

**After:** SEO Engineer completes Content Architecture
**Before:** WordPress Engineer begins

### Checklist

```
MANDATORY (all must pass):

□ H1 defined, unique, and appropriate
  Test: Is there exactly one H1? Does it match page purpose?

□ Heading hierarchy is sequential (no skips)
  Test: H1 → H2 → H3 (not H1 → H3)

□ Content depth position identified
  Test: Is this page's role in content hierarchy clear?

□ Internal links mapped (inbound and outbound)
  Test: Are linking requirements specific?

□ Schema type selected with structure outlined
  Test: Is JSON-LD structure provided?

□ Semantic HTML structure specified
  Test: Are <main>, <article>, <section> defined?

□ URL structure defined
  Test: Is the URL specified and validated?

□ Image SEO requirements documented
  Test: Are filenames and alt text specified?

□ Performance considerations flagged
  Test: Is LCP element identified?

□ No visual design decisions
  Test: No colors, fonts, or layout choices

□ No implementation code
  Test: No PHP, CSS, or JavaScript (schema structure is specification)

□ Supports Creative Director vision
  Test: Does structure enable the emotional journey?
```

### Pass Criteria

**ALL boxes must be checked.**

### Fail Actions

| Failure | Action |
|---------|--------|
| Heading hierarchy broken | Fix sequence |
| Schema missing | Add required schema |
| Performance not considered | Identify LCP, add recommendations |
| Code present | Remove, keep to specification only |

### Gate 3 Declaration

```
═══════════════════════════════════════════════════════════════
GATE 3: STRUCTURE VALIDITY
Result: [PASS / FAIL]
Timestamp: [DateTime]

Checklist: [X/12] items passed

If FAIL:
Failed Items: [List]
Required Fix: [Description]
Return To: SEO Structural Engineer

If PASS:
Proceed To: WordPress Systems Engineer
═══════════════════════════════════════════════════════════════
```

---

## GATE 4: IMPLEMENTATION QUALITY GATE

**After:** WordPress Engineer completes Implementation
**Before:** Brutal Critic review

### Checklist

```
MANDATORY (all must pass):

□ Code implements spec exactly (no additions, no subtractions)
  Test: Compare to Design Brief + User Flow + Content Architecture

□ Zero creative decisions made
  Test: All visual choices traceable to specifications

□ CSS uses brand variables
  Test: No hardcoded colors/fonts

□ Mobile-first responsive
  Test: Check all breakpoints

□ Accessibility standards met
  Test: WCAG 2.1 AA compliance

□ Performance targets achieved
  Test: PageSpeed/Lighthouse scores

□ Code is documented
  Test: Comments explain purpose

□ No console errors
  Test: Browser developer tools

□ Schema validates
  Test: Google Rich Results Test

□ All files organized per standard
  Test: Follows file structure specification

□ Tested on staging
  Test: Live testing completed
```

### Technical Requirements

| Metric | Target | Tool |
|--------|--------|------|
| PageSpeed Mobile | >80 | Google PageSpeed Insights |
| PageSpeed Desktop | >90 | Google PageSpeed Insights |
| LCP | <2.5s | Web Vitals |
| CLS | <0.1 | Web Vitals |
| FID | <100ms | Web Vitals |
| Accessibility | >90 | Lighthouse |
| Best Practices | >90 | Lighthouse |

### Fail Actions

| Failure | Action |
|---------|--------|
| Spec deviation | Correct to match specification |
| Creative decision made | Remove, flag for appropriate role |
| Performance fails | Optimize until targets met |
| Accessibility fails | Fix until compliant |

### Gate 4 Declaration

```
═══════════════════════════════════════════════════════════════
GATE 4: IMPLEMENTATION QUALITY
Result: [PASS / FAIL]
Timestamp: [DateTime]

Checklist: [X/11] items passed

Technical Scores:
- PageSpeed Mobile: [Score]
- PageSpeed Desktop: [Score]
- LCP: [Time]
- CLS: [Score]
- Accessibility: [Score]

If FAIL:
Failed Items: [List]
Required Fix: [Description]
Return To: WordPress Systems Engineer

If PASS:
Proceed To: Brutal Critic
═══════════════════════════════════════════════════════════════
```

---

## GATE 5: FINAL APPROVAL GATE

**After:** Brutal Critic completes review
**Before:** Production deployment

### Checklist (Brutal Critic Executes)

```
MANDATORY (all must pass):

□ DNA alignment verified
  Test: Matches site archetype and soul

□ Negative Rules Engine: Zero violations
  Test: No forbidden patterns detected

□ Screenshot Test passed
  Test: Would be saved for inspiration

□ Generic Test passed
  Test: Cannot be swapped to another site

□ Role Compliance verified
  Test: Each role stayed in lane

□ Technical Quality confirmed
  Test: Gate 4 standards maintained

□ Memory Test passed
  Test: Specific memorable elements identified
```

### Pass Criteria

**ALL boxes must be checked.**
**There is no partial pass.**

### Fail Actions

| Failure | Return To |
|---------|-----------|
| DNA alignment | Creative Director |
| Negative Rules | Whichever role created violation |
| Screenshot Test | Creative Director |
| Generic Test | Creative Director |
| Role Compliance | Full restart |
| Technical Quality | WordPress Engineer |
| Memory Test | Creative Director |

### Gate 5 Declaration

```
═══════════════════════════════════════════════════════════════
GATE 5: FINAL APPROVAL
Result: [APPROVED / REJECTED]
Timestamp: [DateTime]

Checklist: [X/7] items passed

If REJECTED:
Failed Items: [List]
Root Cause: [Role/Phase that failed]
Required Fix: [Description]
Return To: [Specified role]

If APPROVED:
Status: CLEARED FOR PRODUCTION
Deploy To: [Environment]
Monitoring: [What to watch]
═══════════════════════════════════════════════════════════════
```

---

## GATE ENFORCEMENT

### Rule 1: No Skipping

Gates cannot be skipped.

Even if "we're in a hurry."
Even if "it's just a small change."
Even if "we know it's fine."

### Rule 2: No Partial Passes

A gate either passes or fails.

There is no:
- "Mostly pass"
- "Pass with concerns"
- "Conditional pass"

### Rule 3: Failure Returns to Source

When a gate fails, work returns to the role responsible.

Not to the next role.
Not to a "quick fix."
To the role that owns the failure.

### Rule 4: All Failures Documented

Every gate failure is logged:
- What failed
- Why it failed
- What was required
- How it was resolved

### Rule 5: Gates Only Get Stricter

Standards can increase.
Standards never decrease.

---

## EXPEDITED REVIEW (Small Changes Only)

For minor updates (copy changes, small CSS fixes), an expedited gate may be used:

### Expedited Gate Eligibility

The change qualifies if:
- [ ] Does not affect layout structure
- [ ] Does not change brand elements
- [ ] Does not impact SEO structure
- [ ] Is purely cosmetic/copy fix
- [ ] Takes <30 minutes to implement

### Expedited Gate Checklist

```
□ Change matches specification intent
□ No forbidden patterns introduced
□ Technical quality maintained
□ Screenshot test still passes
```

**If any doubt → Full gate review required**

---

## GATE METRICS (Track Over Time)

| Metric | Target | Purpose |
|--------|--------|---------|
| Gate 1 pass rate | >80% | Creative briefs are clear |
| Gate 2 pass rate | >85% | Flows are well-designed |
| Gate 3 pass rate | >90% | Structure is solid |
| Gate 4 pass rate | >90% | Implementation is clean |
| Gate 5 pass rate | >70% | Final quality is high |
| Average iterations | <3 | Process is efficient |

**If Gate 5 pass rate is >95%, standards may be too low.**

---

## GATE FAILURE ESCALATION

### Level 1: Single Failure
- Return to responsible role
- Fix and re-submit
- Normal process

### Level 2: Repeated Failure (3+ times)
- Root cause analysis required
- May indicate role misunderstanding
- Process review triggered

### Level 3: Systemic Failure
- Multiple failures across projects
- System-level issue identified
- Framework update required

---

## THE GATES OATH

> The gates are not obstacles.
> The gates are protection.
> The gates ensure quality.
> The gates prevent shortcuts.
> The gates must be respected.
