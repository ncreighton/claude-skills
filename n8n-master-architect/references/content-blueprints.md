# Content & Publishing Blueprints

Detailed patterns for AI-powered content automation systems.

## 1. AI Blog Factory

### Architecture
```
┌─────────────────────────────────────────────────────────────────┐
│                     AI Blog Factory                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  [Idea Sources] ─→ [Scoring] ─→ [Outline] ─→ [Draft]           │
│                                        │                        │
│                                        ▼                        │
│  [Publish] ←─ [CMS Format] ←─ [SEO] ←─ [Edit]                  │
│      │                                                          │
│      ▼                                                          │
│  [Internal Links] ─→ [Social Posts]                            │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Database Schema
```sql
CREATE TABLE blog_ideas (
  id UUID PRIMARY KEY,
  title TEXT,
  topic TEXT,
  score INTEGER,
  status VARCHAR(20) DEFAULT 'pending',
  created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE blog_articles (
  id UUID PRIMARY KEY,
  idea_id UUID REFERENCES blog_ideas(id),
  title TEXT,
  slug TEXT UNIQUE,
  content TEXT,
  meta_description TEXT,
  status VARCHAR(20) DEFAULT 'draft',
  published_at TIMESTAMP,
  created_at TIMESTAMP DEFAULT NOW()
);
```

### Workflow IDs
- `WS-BLOG-01` - Idea Intake & Scoring
- `WS-BLOG-02` - Outline & Draft Generation
- `WS-BLOG-03` - Editing & Style Enforcement
- `WS-BLOG-04` - SEO & Structural Pass
- `WS-BLOG-05` - CMS Publishing
- `WS-BLOG-06` - Internal Linking
- `WS-BLOG-07` - Social Distribution

### AI Prompts

**Outline Generator:**
```json
{
  "role": "system",
  "content": "Generate a blog post outline. Output strict JSON."
}
```

**Response Schema:**
```json
{
  "title": "string",
  "sections": [
    {
      "heading": "string",
      "key_points": ["string"]
    }
  ],
  "target_word_count": "number"
}
```

---

## 2. AI Substack Engine

### Architecture
```
┌─────────────────────────────────────────────────────────────────┐
│                    AI Substack Engine                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  [Idea] ─→ [Audience/Angle] ─→ [Outline] ─→ [Draft]            │
│                                        │                        │
│                                        ▼                        │
│  [Publish] ←─ [Meta/Tags] ←─ [Format] ←─ [Fact-Check] ←─ [Edit]│
│      │                                                          │
│      ▼                                                          │
│  [Image Prompt] ─→ [Social + Email]                            │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Post Tracking Schema
```json
{
  "post_id": "uuid",
  "title": "string",
  "status": "queued|drafted|edited|factchecked|ready_to_publish|published",
  "tier": "free|paid|subscribers_only",
  "fact_check_score": "number",
  "created_at": "timestamp",
  "published_at": "timestamp"
}
```

### Key Considerations
- Free vs paid post tracking
- Newsletter voice enforcement via style guide
- Fact-checking for sensitive topics
- Image prompt generation for headers

---

## 3. AI YouTube Script Factory

### Architecture
```
┌─────────────────────────────────────────────────────────────────┐
│                  AI YouTube Script Factory                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  [Content Pillars] ─→ [Idea Engine] ─→ [Script Outline]        │
│                                              │                   │
│                                              ▼                   │
│  [Upload Meta] ←─ [SEO Pack] ←─ [Thumbnail] ←─ [Full Script]   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Script Formats

**Shorts (30-60 sec):**
```json
{
  "format": "shorts",
  "target_duration_sec": 45,
  "hook": "First 3-5 seconds grab attention",
  "core_idea": "One main point",
  "payoff": "Quick conclusion"
}
```

**Longform (8-15 min):**
```json
{
  "format": "longform",
  "target_duration_min": 12,
  "chapters": [
    {
      "title": "string",
      "duration_sec": "number",
      "visual_suggestions": ["string"]
    }
  ],
  "pattern_breaks": ["string"]
}
```

### Thumbnail Concepts
- Short, bold text (2-4 words)
- Clear focal point
- High-contrast imagery
- Face with expression (if applicable)

---

## 4. AI Book Publishing

### Architecture
```
┌─────────────────────────────────────────────────────────────────┐
│                  AI Book Publishing System                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  [Idea] ─→ [Market Research] ─→ [Niche Validation]             │
│                                        │                        │
│                                        ▼                        │
│  [Cover + Meta] ←─ [Style Pass] ←─ [Chapters] ←─ [Outline/TOC] │
│       │                                                         │
│       ▼                                                         │
│  [Interior Format] ─→ [Listing Copy] ─→ [Launch Assets]        │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Book Tracking Schema
```json
{
  "book_id": "uuid",
  "title": "string",
  "status": "ideation|outlining|drafting|editing|formatting|ready_to_publish",
  "chapter_count": "number",
  "word_count": "number",
  "niche": "string"
}
```

### Per-Chapter Workflow
Each chapter processed independently:
1. Draft chapter
2. Style/consistency check
3. Internal review
4. Merge to book

### Important Flags
- Maintain consistent voice, POV, terminology
- Flag claims requiring citations
- Cover prompts: genre, mood, audience (no text unless specified)

---

## 5. AI Podcast Production

### Architecture
```
┌─────────────────────────────────────────────────────────────────┐
│                  AI Podcast Production System                    │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  [Planning] ─→ [Recording] ─→ [Audio Ingest] ─→ [Transcription]│
│                                                      │          │
│                                                      ▼          │
│  [Distribute] ←─ [Title/Thumb] ←─ [Quotes/Clips] ←─ [Notes]    │
│                                                      │          │
│                                                      ▼          │
│                                              [Chapters/Times]   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Episode Tracking Schema
```json
{
  "episode_id": "uuid",
  "episode_number": "number",
  "title": "string",
  "status": "planned|recorded|transcribed|processed|published",
  "duration_sec": "number",
  "guest_name": "string"
}
```

### Clip Extraction
```json
{
  "clip_id": "uuid",
  "episode_id": "uuid",
  "start_time": "HH:MM:SS",
  "end_time": "HH:MM:SS",
  "hook_line": "string",
  "speaker": "host|guest"
}
```

### Outputs Generated
- Blog-style summaries
- Show notes with links
- Chapter markers with timestamps
- Social media clips
- Email newsletter content
- Searchable transcript archive

---

## Implementation Notes

### State Machine Pattern
All content systems use status-based state machines:
```
pending → in_progress → [intermediate states] → completed|failed
```

### AI Node Requirements
- All AI outputs MUST be strict JSON
- Define response schema in prompts
- Validate before downstream processing

### Database Tables
Each system needs:
- Ideas/Planning table
- Draft/Content table
- Published/Output table
- Logs/Errors table

### Error Handling
- Dedicated error workflows
- Retry logic for transient failures
- Human review queues for AI failures
