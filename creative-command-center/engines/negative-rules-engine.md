# 🚫 NEGATIVE RULES ENGINE

## PURPOSE

The Negative Rules Engine is a **gatekeeper that all design output must pass through**.

It is NOT guidance. It is NOT "things to consider."

**If ANY rule is violated, the design is REJECTED.**

---

## HOW TO USE THIS ENGINE

1. Before finalizing ANY design decision, check against this engine
2. If a pattern matches a forbidden rule → STOP
3. Redesign to avoid the violation
4. Re-check until no violations remain

**There are no exceptions. There are no "just this once."**

---

## SECTION 1: FORBIDDEN LAYOUT PATTERNS

### 1.1 The Template Trap

**FORBIDDEN:** Hero → 3-Column Features → CTA

This pattern is:
```
[Hero Section]
      ↓
[Feature] [Feature] [Feature]
      ↓
[Call to Action]
```

**Why Forbidden:**
- Every WordPress theme demo uses this
- Users have seen it 10,000 times
- It signals "I used a template"
- Zero memorability

**Detection Triggers:**
- Hero followed immediately by 3 equal-width columns
- Columns containing icon + heading + paragraph
- Section ending with centered button

**VERDICT: REJECT**

---

### 1.2 The SaaS Marketing Flow

**FORBIDDEN:** Stats Bar → Feature Grid → Testimonials → Pricing → CTA

```
[Hero]
[Stats: 1M+ Users | 50+ Countries | 99.9% Uptime]
[Feature Grid]
[Testimonial Carousel]
[Pricing Tables]
[Final CTA]
```

**Why Forbidden:**
- Designed for B2B SaaS, wrong for content sites
- Optimized for transactions, not experiences
- Every startup uses this exact flow
- Doesn't match empire site purposes

**VERDICT: REJECT**

---

### 1.3 The Blog Grid

**FORBIDDEN:** Identical cards in perfect grid

```
[Card] [Card] [Card]
[Card] [Card] [Card]
[Card] [Card] [Card]
```

**Why Forbidden:**
- Treats all content as equal (it's not)
- No hierarchy or editorial voice
- Pinterest-style without Pinterest's purpose
- Encourages skimming, not engagement

**Better Approach:** (for reference only - Creative Director decides)
- Featured content treated differently
- Varied card sizes
- Editorial curation visible
- Reading journey designed

**VERDICT: REJECT**

---

### 1.4 Perfect Symmetry

**FORBIDDEN:** Everything centered and balanced

```
        [Logo]
      [Headline]
     [Subheadline]
       [Button]
```

**Why Forbidden:**
- Boring and expected
- No visual tension
- No direction for eye movement
- Looks like a default template

**Exception:** Symmetry with intentional breaking element may be acceptable
(Creative Director must justify)

**VERDICT: REJECT** (unless explicitly justified in Design Brief)

---

### 1.5 The Five-Column Footer

**FORBIDDEN:** Footer with 5 identical widget columns

```
[Col 1] [Col 2] [Col 3] [Col 4] [Col 5]
Logo    About   Links   Social  Newsletter
```

**Why Forbidden:**
- Every theme does this
- Most columns have useless content
- Visual clutter at page end
- No design thought applied

**VERDICT: REJECT**

---

### 1.6 Hamburger Menu on Desktop

**FORBIDDEN:** Hidden navigation on screens >1024px

**Why Forbidden:**
- Hides important navigation
- One extra click for everything
- "Minimal" becomes "inconvenient"
- Only acceptable when truly necessary

**Exception:** Design systems with genuinely limited navigation (1-3 items)

**VERDICT: REJECT** (on desktop)

---

## SECTION 2: FORBIDDEN VISUAL PATTERNS

### 2.1 The AI Gradient

**FORBIDDEN:** Purple-to-blue gradients

```css
/* FORBIDDEN */
background: linear-gradient(to right, #8B5CF6, #3B82F6);
background: linear-gradient(135deg, purple, blue);
```

**Why Forbidden:**
- Every AI tool generates this
- Signals "I used an AI generator"
- Overused to the point of cliché
- Lacks brand specificity

**Also Forbidden:**
- Purple to cyan
- Blue to teal
- Any gradient that "screams AI"

**VERDICT: REJECT**

---

### 2.2 White + Pastel + Rounded

**FORBIDDEN:** Clean white background with pastel accents and rounded everything

```
- White background (#FFFFFF)
- Pastel accent colors
- border-radius: 16px+ on everything
- Soft shadows
- Lots of white space
```

**Why Forbidden:**
- The "modern minimal" template look
- Every Figma UI kit does this
- No personality or brand character
- Interchangeable with thousands of sites

**VERDICT: REJECT**

---

### 2.3 Generic Icon Sets

**FORBIDDEN:** Font Awesome defaults, Heroicons without customization

**Why Forbidden:**
- Everyone uses the same icons
- No brand differentiation
- Users have seen these icons everywhere
- Signals low design investment

**Acceptable:**
- Customized icons matching brand
- Illustrated icons with character
- No icons (text can work)

**VERDICT: REJECT** (if using standard icon libraries unchanged)

---

### 2.4 Stock Photo + Overlay

**FORBIDDEN:** Generic stock photo with color/gradient overlay

```
[Stock image of "business people" or "nature"]
      + 50% dark overlay
      + centered white text
```

**Why Forbidden:**
- Lazy design shortcut
- Stock images are recognizable
- Overlay doesn't make it unique
- Zero creative effort visible

**VERDICT: REJECT**

---

### 2.5 The Predictable Hover

**FORBIDDEN:** Standard hover effects without thought

```css
/* FORBIDDEN - Too common */
.card:hover {
    transform: scale(1.05);
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
}
```

**Why Forbidden:**
- Every card does this exact thing
- No surprise, no delight
- Feels template-generated
- Doesn't match brand personality

**Hovers should:**
- Match the site's pacing (fast site = snappy hover, contemplative site = slow hover)
- Reflect brand personality
- Surprise or delight somehow

**VERDICT: REJECT** (if using default hover patterns)

---

### 2.6 Perfectly Centered Hero Text

**FORBIDDEN:** Center-aligned headline in exact center of hero

```
        [Navigation]
        
        
        
     [Headline Here]
    [Subheadline Here]
        [Button]
        
        
```

**Why Forbidden:**
- Default template behavior
- No visual interest
- No direction for reading
- Forgettable

**VERDICT: REJECT**

---

## SECTION 3: FORBIDDEN TYPOGRAPHY

### 3.1 Banned Fonts

**FORBIDDEN:** Using these as primary/heading fonts:

```
- Inter
- Roboto
- Arial
- Helvetica
- System font stack for headings
- Open Sans (as primary)
- Montserrat (as only font)
```

**Why Forbidden:**
- Overused to meaninglessness
- Signal "I didn't think about typography"
- No brand personality
- Default choices

**Acceptable:**
- These fonts CAN be used for UI elements, code blocks, or specific purposes
- They CANNOT be the primary brand fonts

**VERDICT: REJECT** (if used as primary/heading)

---

### 3.2 The Typography Trio

**FORBIDDEN:** Giant headline + medium subheadline + button

```
[48px Bold Headline]
[18px Light Subheadline explaining the headline]
        [Button]
```

**Why Forbidden:**
- The exact structure of every landing page
- Predictable hierarchy
- No typographic creativity
- Template-obvious

**VERDICT: REJECT**

---

### 3.3 All Caps Abuse

**FORBIDDEN:** All caps for more than short labels

```
HELLO AND WELCOME TO OUR WEBSITE. WE ARE EXCITED TO HAVE
YOU HERE. PLEASE EXPLORE ALL OF OUR AMAZING CONTENT AND
DON'T FORGET TO SUBSCRIBE TO OUR NEWSLETTER.
```

**Why Forbidden:**
- Hard to read
- Feels like shouting
- Reduces comprehension
- Overused for "emphasis"

**Acceptable Uses:**
- Button labels (3-4 words max)
- Short labels/badges
- Navigation items (sparingly)

**VERDICT: REJECT** (if used for body text or long headings)

---

### 3.4 Perfect 16px Body Everywhere

**FORBIDDEN:** Using 16px body text as default without thought

**Why Forbidden:**
- Browser default
- Doesn't consider the content type
- Doesn't consider the audience
- One-size-fits-all thinking

**Consider Instead:**
- 18px for reading-heavy sites
- Type scale that creates hierarchy
- Different sizes for different content types

**VERDICT: REJECT** (if 16px is used without justification)

---

## SECTION 4: FORBIDDEN INTERACTIONS

### 4.1 Generic CTAs

**FORBIDDEN:** These exact CTA phrases:

```
- "Learn More"
- "Get Started"
- "Sign Up"
- "Click Here"
- "Read More"
- "Submit"
- "Download Now"
```

**Why Forbidden:**
- Every website uses these
- No brand voice
- No indication of value
- Boring

**CTAs Should:**
- Reflect brand voice
- Indicate specific value
- Feel like an invitation, not a command

**Examples for Empire Sites:**
- Witchcraft: "Begin Your Journey" / "Enter the Circle"
- SmartHome: "Build Your Smart Home" / "See the Possibilities"
- Family: "Start Thriving" / "Join Our Community"

**VERDICT: REJECT** (if using generic CTA text)

---

### 4.2 Aggressive Popups

**FORBIDDEN:** Popups appearing within first 5 seconds

```
[User arrives]
[2 seconds pass]
[POPUP: "SUBSCRIBE NOW! 10% OFF!"]
```

**Why Forbidden:**
- Interrupts experience
- User hasn't seen value yet
- Feels desperate
- Damages trust

**If popups are needed:**
- Time-delayed (30+ seconds)
- Exit-intent only
- Non-intrusive design
- Easy to dismiss

**VERDICT: REJECT** (if aggressive timing)

---

### 4.3 Exit Intent Guilt

**FORBIDDEN:** Exit-intent modals with guilt-trip copy

```
"Wait! Are you sure you want to miss out?"
"No thanks, I don't want to improve my life"
"I'll stay stuck forever"
```

**Why Forbidden:**
- Manipulative
- Damages brand trust
- Users hate this
- Short-term gain, long-term loss

**VERDICT: REJECT**

---

### 4.4 Autoplay Video with Sound

**FORBIDDEN:** Videos that play automatically with audio

**Why Forbidden:**
- Surprises users
- Violates accessibility
- Unprofessional
- Users immediately close tab

**Acceptable:**
- Muted autoplay (in certain contexts)
- User-initiated playback
- Video with clear play button

**VERDICT: REJECT** (if autoplay with sound)

---

### 4.5 Sticky Elements Covering Content

**FORBIDDEN:** Fixed elements that obstruct reading

```
[Sticky Header - 80px]
[Sticky CTA Bar - 60px]
[Content... but 140px is always covered]
[Sticky Chat Widget]
[Cookie Banner]
```

**Why Forbidden:**
- Reduces readable viewport
- Distracts from content
- Feels aggressive
- Mobile becomes unusable

**Limit:**
- ONE sticky element (usually navigation)
- Must not cover content
- Must be dismissible

**VERDICT: REJECT** (if multiple persistent elements)

---

## SECTION 5: FORBIDDEN CONTENT PATTERNS

### 5.1 Stock Phrases

**FORBIDDEN:**

```
- "Transform your life"
- "Unlock your potential"
- "Take your X to the next level"
- "Best-in-class"
- "World-class"
- "Revolutionary"
- "Game-changing"
- "Synergy"
- "Leverage"
```

**Why Forbidden:**
- Meaningless through overuse
- Signal lazy copywriting
- Not specific to any brand
- Users filter them out

**VERDICT: REJECT** (if stock phrases appear)

---

### 5.2 The "Ultimate Guide" Claim

**FORBIDDEN:** Claiming to be "The Ultimate Guide" to everything

```
"The Ultimate Guide to Witchcraft"
"The Ultimate Guide to Candles"
"The Ultimate Guide to Moon Phases"
"The Ultimate Guide to Tarot"
```

**Why Forbidden:**
- Overused SEO tactic
- Makes unrealistic promises
- Signals low-quality content farms
- Dilutes brand authority

**Better:**
- "A Beginner's Guide"
- "Understanding X"
- "Your Introduction to"
- Or just... don't use "Guide" every time

**VERDICT: REJECT** (if "ultimate" is overused)

---

### 5.3 AI-Obvious Writing

**FORBIDDEN:** Content that reads like AI generation

**Markers of AI Content:**
- "In conclusion" as transition
- "It's important to note that..."
- "There are several factors to consider"
- Excessive hedging
- Lists that all start the same way
- Perfect 5-paragraph essay structure
- No personality or voice

**VERDICT: REJECT** (if content feels AI-generated)

---

## SECTION 6: THE GENERIC TESTS

### 6.1 The Swap Test

**Test:** Take the design and mentally place it on a competitor's site.

**Question:** Does it still work?

**If YES → REJECT**

The design lacks unique identity.

---

### 6.2 The "Could Be Anywhere" Test

**Test:** Remove the logo and brand name.

**Question:** Could you identify which site this is?

**If NO → REJECT**

The design is generic.

---

### 6.3 The Template Demo Test

**Test:** Search for WordPress themes in this niche.

**Question:** Does the design look like any of the demo sites?

**If YES → REJECT**

The design is template-obvious.

---

### 6.4 The Screenshot Test

**Test:** Screenshot the design.

**Question:** Would a professional designer save this to their inspiration folder?

**If NO → REJECT**

The design is not exceptional.

---

### 6.5 The Forgettable Test

**Test:** Show the design to someone for 10 seconds, then close it.

**Question:** What specific elements do they remember?

**If "nothing specific" → REJECT**

The design has no memorable moments.

---

### 6.6 The "Pretty Good" Test

**Test:** Ask yourself honestly how you'd describe the design.

**If "pretty good" → REJECT**

"Pretty good" is not the standard. "Remarkable" is.

---

## SECTION 7: SITE-SPECIFIC RULES

Each site has additional forbidden patterns beyond the global rules.

### WitchcraftForBeginners

**Additional Forbidden:**
- Stock witch imagery (pentagram poses, black cats clichés)
- Halloween aesthetic
- Neon/bright colors
- "Wicca 101" generic content
- Harry Potter references
- Cultural appropriation (closed practices)
- Clean white minimalism

---

### SmartHomeWizards

**Additional Forbidden:**
- Matrix/cyberpunk aesthetic
- Overly technical jargon without explanation
- Stock "smart home" photos (finger on phone)
- Competitor brand bashing
- Fear-based security messaging
- Geek-exclusive tone

---

### MythicalArchives

**Additional Forbidden:**
- Hollywood mythology (Disney, Marvel interpretations)
- AI-generated mythological art
- Casual/jokey tone about sacred stories
- Western-centric mythology bias
- Treating mythology as fiction (respect source cultures)

---

### Family-Flourish

**Additional Forbidden:**
- Stock family photos (diverse family on couch)
- Mommy blog clichés
- Pinterest-perfect unrealistic standards
- Gender-stereotyped parenting
- Preachy or judgmental tone
- MLM-adjacent messaging

---

## ENFORCEMENT PROTOCOL

### Level 1: Warning (First Violation)

```
⚠️ NEGATIVE RULES WARNING

Pattern Detected: [Pattern name]
Location: [Where in design]
Rule Reference: [Section number]

Immediate correction required.
```

### Level 2: Rejection (Pattern Persists)

```
❌ NEGATIVE RULES REJECTION

Violation: [Pattern name]
This is a [Level 1/2/3] violation.
Design cannot proceed until resolved.

RETURN TO: [Appropriate role]
```

### Level 3: Full Reset (Multiple Violations)

```
🔴 NEGATIVE RULES - FULL RESET REQUIRED

Multiple/severe violations detected:
1. [Violation]
2. [Violation]
3. [Violation]

The design foundation is compromised.
Full restart from Creative Director required.
```

---

## THE NEGATIVE RULES OATH

> These rules exist because generic is easy.
> These rules exist because templates are everywhere.
> These rules exist because "good enough" is not enough.
> These rules are not suggestions.
> These rules are the law.
> Violate them and face rejection.

---

## UPDATES TO THIS ENGINE

The Negative Rules Engine evolves:
- New generic patterns emerge → Add them
- Standards change → Update thresholds
- New site acquired → Add site-specific rules

**But rules are never relaxed.**

**The standard only goes up.**
