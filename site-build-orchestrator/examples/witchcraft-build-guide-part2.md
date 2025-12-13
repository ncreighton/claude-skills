## Phase 4: Homepage

**CRITICAL: The homepage must create an ATMOSPHERE. If it feels generic, iterate until visitors PAUSE on arrival.**

### P4.1 - Create Homepage
```
Create a new page:
- Title: "Home" (or leave blank)
- Permalink: (set as front page)
- Template: Full Width (no sidebar)
- Go to Settings → Reading → Set as static front page
```

### P4.2 - Hero Section
```
Create the homepage hero section for WitchcraftForBeginners.

This is THE MOST IMPORTANT section. It must feel like crossing a threshold into a candlelit sanctuary.

Requirements:
- Height: 100vh (full viewport)
- Background: #0F0F1A with subtle radial gradient lighter in center
- Content emerges from darkness with 1.2s fade-in animation
- Moon phase indicator in corner (can be placeholder for now)

Hero Content:
- Headline: In Cinzel, #D4AF37, 4.209rem
  "Where Ancient Wisdom Meets Modern Seekers"
  (or similar - NOT "Welcome to our website")
  
- Subhead: In Lora, #E8E4D9, 1.333rem, max-width 600px
  "Your trusted guide into authentic witchcraft practice. 
   Every journey begins with a single question."
  
- CTA: Single button, lower third
  Text: "Begin Your Journey" (NOT "Learn More" or "Get Started")
  Style: Primary button with subtle glow on hover
  
- Position: Slightly off-center left, content emerges from shadow
  NOT perfectly centered (that's generic)

Animation CSS:
.hero-content {
    animation: emerge 1.2s ease-out forwards;
    opacity: 0;
}
@keyframes emerge {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

Background effect (optional):
- Subtle vignette from edges
- Very faint constellation pattern (5% opacity)
- NO parallax - it's overdone

FORBIDDEN:
- Stock witch image
- Pentagram hero image
- Multiple CTAs
- "Welcome to WitchcraftForBeginners"
- Bright colors
- Centered-everything layout
```

### P4.3 - Moon Phase Indicator
```
Add the signature moon phase indicator.

For now, use a static representation:
- Position: Fixed top-right of hero, or in header
- Size: 32px icon
- Color: #D4AF37
- Style: Elegant line art, not cartoonish

Create placeholder:
<div class="moon-phase" title="Current Moon Phase">
    <!-- SVG moon icon here -->
    <span class="moon-label">Waxing Crescent</span>
</div>

Future: Will connect to moon phase API for dynamic updates.
```

### P4.4 - Section 1: Invitation for Beginners
```
Create "Begin Your Path" section:

Purpose: Clear entry point for new visitors (our primary audience is Curious Clara)

Layout:
- Full-width with max-width container
- Heading + 3-4 paths/options
- Asymmetric card layout (not identical grid)

Content:
Heading: "Not Sure Where to Start?" (Cinzel, #E8E4D9)
Subhead: "Every practitioner was once a seeker. Here are your first steps." (Lora)

Three Paths (as styled cards):
1. "What is Witchcraft?" - For the truly curious
2. "Your First Spell" - For those ready to practice  
3. "Building Your Altar" - For those setting up sacred space

Each card:
- Background: #16213E (Midnight Blue)
- Border: 1px solid rgba(212, 175, 55, 0.2)
- Hover: Border brightens, subtle glow
- Title: Cinzel
- Brief description: Lora
- Arrow or "Explore →" link

Spacing: 120px from hero, 80px between sections
```

### P4.5 - Section 2: Featured Content
```
Create "Essential Grimoire" section:

Purpose: Showcase best/most important content (editorial curation, not "latest posts")

Layout:
- Magazine-style with featured item larger
- 1 large feature + 3 smaller
- NOT a 4-column identical grid

Content:
Heading: "From the Grimoire" or "Essential Reading"

Featured Card (2x size):
- Large image or illustration
- Title
- Excerpt
- "Read the Guide" link

Smaller Cards (3):
- Thumbnail
- Title
- Category tag
- No excerpt

Selection: Manually curated evergreen content, not auto-latest.
```

### P4.6 - Section 3: Moon Magic Teaser
```
Create Moon Magic section:

Purpose: Highlight lunar content (major content pillar) and create connection to natural cycles

Layout:
- Split: Left text, Right large moon image/illustration
- OR: Centered with moon phases graphic

Content:
Heading: "Work With the Moon" (Cinzel)
Body: "The moon has guided practitioners for millennia. Learn to align your practice with her cycles." (Lora)
CTA: "Explore Moon Magic" (links to moon magic category)

Visual:
- Moon illustration or high-quality photo
- Subtle animation: very slow pulse or glow (3s cycle)
- NOT: Cheesy glitter effects

Include current phase mention:
"Tonight: [Moon Phase] - [What it's good for]"
```

### P4.7 - Section 4: Newsletter CTA
```
Create newsletter/community section:

Purpose: Email list building with voice-appropriate messaging

Layout:
- Centered, max-width 600px
- Decorative flourish above/below (botanical or celestial)
- Form with email field + button

Content:
Heading: "Enter the Circle" (NOT "Subscribe to our Newsletter")
Body: "Join our community of seekers and practitioners. Receive moon phase reminders, seasonal rituals, and guidance for your path."
Button: "Light Your Candle" (NOT "Subscribe" or "Sign Up")

Form styling:
- Dark input field matching site
- Button matches primary style
- Subtle validation feedback

Note: Connect to email provider later. For now, create the visual.
```

### P4.8 - Candle Glow Effect
```
Add the signature candle glow effect to key sections.

CSS for glow effect:
.candle-glow {
    position: relative;
}
.candle-glow::before {
    content: '';
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 300px;
    height: 300px;
    background: radial-gradient(ellipse at center, 
        rgba(212, 175, 55, 0.08) 0%,
        transparent 70%);
    pointer-events: none;
    animation: flicker 4s ease-in-out infinite;
}
@keyframes flicker {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.7; }
}

Apply to:
- Hero section
- Newsletter section
- Maybe 1 other focal point

Remember: These are special because they're RARE. Max 2-3 per page.
```

### P4.9 - Homepage Polish
```
Final homepage review and polish:

1. Check section spacing:
   - Between hero and Section 1: 120px
   - Between other sections: 80-100px
   
2. Check content-to-whitespace ratio:
   - Target: 40% content, 60% space
   - If feeling cramped, add more padding
   
3. Test emergence animations:
   - Hero content fades in on load
   - Sections fade in on scroll (use Intersection Observer)
   
4. Verify mobile layout:
   - Hero still atmospheric but simplified
   - Cards stack nicely
   - Text readable without zoom
   - Touch targets 44px minimum
   
5. Check load performance:
   - No huge images blocking render
   - Fonts loading with swap
   
6. Final atmosphere check:
   - Does it feel like entering a candlelit study?
   - Would you pause and look around?
   - Is it screenshot-worthy?
```

### ✓ Phase 4 Checkpoint
```
Run Phase 4 checkpoint with DNA quality tests:

1. Load homepage fresh - does atmosphere hit within 3 seconds?

2. Screenshot Test:
   Would a professional designer save this for inspiration?
   ⬜ Yes (PASS) / ⬜ No (FAIL - iterate)

3. Swap Test:
   Could this homepage work on any generic spiritual site?
   ⬜ Yes (FAIL - too generic) / ⬜ No (PASS - it's unique)

4. Memory Test:
   What specific element will visitors remember in a week?
   Answer: _____________ (should be able to name something)

5. Ten-Second Test:
   Show someone for 10 seconds. Ask what the site is about.
   They should say: Witchcraft/magic education
   
6. Grandmother Test:
   If a skeptical grandmother saw this, would she think:
   ⬜ "A real, professional website" (PASS)
   ⬜ "Spooky Halloween nonsense" (FAIL)

7. Emotional Check:
   - Warm mysticism: ⬜ Present
   - Empowering: ⬜ Present  
   - Fear/anxiety: ⬜ Absent (good)
   
8. Technical:
   - Console errors: ⬜ None
   - Mobile layout: ⬜ Works
   - Animations smooth: ⬜ Yes

If ANY major item fails, do not proceed. Iterate until pass.
```

---

## Phase 5-10: Quick Reference

*Full prompts in main BUILD-GUIDE template. Key site-specific notes below.*

### Phase 5: Templates - Site-Specific
```
Single Post Template:
- Max width: 720px (for reading comfort)
- NO sidebar on articles - full focus on content
- Related posts: "Continue Your Journey" - max 3, curated feel
- Reading time estimate in meta
- Last updated date (for evergreen content)

Category Template:
- Magazine layout with 1 featured post larger
- Category description at top (write mystical intros for each)
- "Load More" button (not infinite scroll)
```

### Phase 6: Core Pages - Site-Specific
```
Begin Here (/begin-here/):
- This is THE pillar page
- Structure: Welcome → What is Witchcraft → First Steps → Tools → Next Steps
- Internal links to all major sections
- Make it feel like an orientation, not a sales page

About (/about/):
- Voice: The wise woman telling her story
- Include: Why this site exists, who it's for, what we believe
- NOT: Corporate "About Us" copy

Affiliate Disclosure (/affiliate-disclosure/):
- Honest about affiliate relationships
- Explain how we choose what to recommend
- Must exist for FTC compliance
```

### Phase 7: SEO - Site-Specific
```
Primary Keywords:
- witchcraft for beginners
- how to start witchcraft
- beginner witch
- learn witchcraft

Schema:
- Article schema on all posts
- HowTo schema on ritual/spell guides
- FAQ schema on beginner guides
- Recipe schema on spell "recipes" (via WP Recipe Maker)

Content Pillars:
1. Begin Here (cornerstone)
2. Spells & Rituals
3. Moon Magic
4. Tools & Supplies
5. Sabbats & Seasons
```

### Phase 8: Performance
```
Targets:
- Mobile PageSpeed: >80
- Desktop PageSpeed: >90
- LCP: <2.5s
- CLS: <0.1

Special considerations:
- Dark images compress well
- Custom fonts: subset if possible
- Emergence animations: Use CSS, not JS
```

---

## CRITICAL REMINDERS FOR THIS SITE

Throughout ALL phases, remember:

### Voice
- Wise but warm
- Patient teacher
- Invitation, not command
- "Begin Your Journey" not "Get Started"
- "Enter the Circle" not "Subscribe"

### Visual
- DARK MODE - no white backgrounds ever
- Emergence from shadow - content appears, not lands
- Slow transitions (0.5s+) - never bouncy
- Candle glow, not neon glow
- Cinzel for headings, Lora for body - NO sans-serif

### Forbidden (Instant Rejection)
- Sans-serif headings
- White/light backgrounds
- Stock witch costumes
- Halloween imagery
- "Welcome to our website"
- Generic CTAs ("Learn More", "Click Here")
- Purple-to-blue gradients
- Perfectly centered everything

### The Feeling
Every page should feel like:
*A candlelit study in an old cottage. Bookshelves of grimoires. Fire crackling low. The visitor is a welcome guest, not a customer.*

---

*Generated by Site Build Orchestrator*
*For: WitchcraftForBeginners*
*DNA Version: 2.0.0*
