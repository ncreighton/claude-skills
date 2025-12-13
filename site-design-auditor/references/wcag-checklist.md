# WCAG 2.1 Quick Reference Checklist

## Level A (Minimum)

### Perceivable
- [ ] **1.1.1** Non-text Content: All images have alt text
- [ ] **1.2.1** Audio/Video: Captions or alternatives provided
- [ ] **1.3.1** Info and Relationships: Semantic HTML used correctly
- [ ] **1.3.2** Meaningful Sequence: Content order makes sense
- [ ] **1.3.3** Sensory Characteristics: Instructions don't rely solely on shape/color
- [ ] **1.4.1** Use of Color: Color not only means of conveying info
- [ ] **1.4.2** Audio Control: Auto-playing audio can be paused

### Operable
- [ ] **2.1.1** Keyboard: All functionality accessible by keyboard
- [ ] **2.1.2** No Keyboard Trap: Users can navigate away from any element
- [ ] **2.1.4** Character Key Shortcuts: Can be turned off or remapped
- [ ] **2.2.1** Timing Adjustable: Time limits can be extended
- [ ] **2.2.2** Pause, Stop, Hide: Moving content can be controlled
- [ ] **2.3.1** Three Flashes: No content flashes more than 3x/second
- [ ] **2.4.1** Bypass Blocks: Skip navigation links provided
- [ ] **2.4.2** Page Titled: Descriptive page titles
- [ ] **2.4.3** Focus Order: Logical tab order
- [ ] **2.4.4** Link Purpose: Link text describes destination
- [ ] **2.5.1** Pointer Gestures: Complex gestures have alternatives
- [ ] **2.5.2** Pointer Cancellation: Can cancel accidental clicks
- [ ] **2.5.3** Label in Name: Accessible name contains visible text
- [ ] **2.5.4** Motion Actuation: Motion-triggered actions have alternatives

### Understandable
- [ ] **3.1.1** Language of Page: Lang attribute on html element
- [ ] **3.2.1** On Focus: Focus doesn't cause unexpected changes
- [ ] **3.2.2** On Input: Input doesn't cause unexpected changes
- [ ] **3.3.1** Error Identification: Errors clearly identified
- [ ] **3.3.2** Labels or Instructions: Form inputs have labels

### Robust
- [ ] **4.1.1** Parsing: Valid HTML
- [ ] **4.1.2** Name, Role, Value: Custom controls have ARIA

## Level AA (Recommended)

### Perceivable
- [ ] **1.3.4** Orientation: Works in both portrait and landscape
- [ ] **1.3.5** Identify Input Purpose: Autocomplete attributes used
- [ ] **1.4.3** Contrast (Minimum): 4.5:1 for normal text, 3:1 for large
- [ ] **1.4.4** Resize Text: Text can zoom to 200%
- [ ] **1.4.5** Images of Text: Real text used, not images
- [ ] **1.4.10** Reflow: Content reflows at 320px width
- [ ] **1.4.11** Non-text Contrast: 3:1 for UI components
- [ ] **1.4.12** Text Spacing: Adjustable spacing doesn't break layout
- [ ] **1.4.13** Content on Hover/Focus: Tooltips dismissible and persistent

### Operable
- [ ] **2.4.5** Multiple Ways: Multiple ways to find pages
- [ ] **2.4.6** Headings and Labels: Descriptive headings/labels
- [ ] **2.4.7** Focus Visible: Keyboard focus indicator visible

### Understandable
- [ ] **3.1.2** Language of Parts: Lang attribute for foreign phrases
- [ ] **3.2.3** Consistent Navigation: Navigation consistent across pages
- [ ] **3.2.4** Consistent Identification: Components identified consistently
- [ ] **3.3.3** Error Suggestion: Error corrections suggested
- [ ] **3.3.4** Error Prevention: Reversible/confirmed for legal/financial

### Robust
- [ ] **4.1.3** Status Messages: Status changes announced to AT

## Level AAA (Enhanced)

### Perceivable
- [ ] **1.4.6** Contrast (Enhanced): 7:1 for normal, 4.5:1 for large
- [ ] **1.4.8** Visual Presentation: Customizable text display
- [ ] **1.4.9** Images of Text (No Exception): No images of text

### Operable
- [ ] **2.2.3** No Timing: No time limits
- [ ] **2.2.4** Interruptions: Interruptions can be postponed
- [ ] **2.2.5** Re-authenticating: Data preserved on timeout
- [ ] **2.2.6** Timeouts: Users warned about inactivity timeouts
- [ ] **2.3.2** Three Flashes: No flashing content at all
- [ ] **2.3.3** Animation: Motion can be disabled
- [ ] **2.4.8** Location: Breadcrumbs or site map
- [ ] **2.4.9** Link Purpose (Link Only): Link text alone is descriptive
- [ ] **2.4.10** Section Headings: Content organized with headings
- [ ] **2.5.5** Target Size: Click targets at least 44x44px
- [ ] **2.5.6** Concurrent Input: Support multiple input methods

### Understandable
- [ ] **3.1.3** Unusual Words: Glossary provided
- [ ] **3.1.4** Abbreviations: Abbreviations expanded
- [ ] **3.1.5** Reading Level: Lower secondary reading level
- [ ] **3.1.6** Pronunciation: Pronunciation provided
- [ ] **3.2.5** Change on Request: Changes only happen on request
- [ ] **3.3.5** Help: Context-sensitive help available
- [ ] **3.3.6** Error Prevention (All): All submissions reversible

## Quick Tests

### Keyboard Navigation
1. Tab through entire page
2. Verify focus visible at all times
3. Verify logical tab order
4. Test all interactive elements

### Screen Reader
1. Verify heading hierarchy
2. Check image alt text
3. Verify form labels
4. Check landmark regions

### Color Contrast
- Normal text: 4.5:1 minimum
- Large text (18px+): 3:1 minimum
- UI components: 3:1 minimum

### Touch Targets
- Minimum size: 44x44 CSS pixels
- Adequate spacing between targets
