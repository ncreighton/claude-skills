# Preflight Checklist Template

## Pre-Build Requirements for {{SITE_NAME}}

**Generated:** {{DATE}}  
**Site URL:** {{SITE_URL}}  
**Status:** {{SITE_STATUS}} (New Build / Redesign / Upgrade)

---

## 🚦 GO/NO-GO Checklist

Complete ALL items before proceeding to Phase 1. Any ❌ = STOP and resolve first.

---

### 1. HOSTING & INFRASTRUCTURE

| Requirement | Status | Notes |
|-------------|--------|-------|
| Domain registered and active | ⬜ | Domain: {{DOMAIN}} |
| Domain pointed to hosting | ⬜ | Nameservers: Hostinger |
| SSL certificate installed | ⬜ | Must be HTTPS |
| WordPress installed | ⬜ | Latest version |
| PHP version 8.1+ | ⬜ | Check hosting panel |
| MySQL database created | ⬜ | Automatic with WP install |

**Verification command:**
```bash
# Via WP-CLI (if available)
wp core version
wp option get siteurl
```

**Manual verification:**
- [ ] Visit https://{{DOMAIN}} - loads without errors
- [ ] Visit https://{{DOMAIN}}/wp-admin - login works
- [ ] Browser shows padlock (SSL working)

---

### 2. WORDPRESS ADMIN ACCESS

| Requirement | Status | Notes |
|-------------|--------|-------|
| Admin account created | ⬜ | Use strong password |
| Admin email verified | ⬜ | For notifications |
| Site title set | ⬜ | Can be temporary |
| Timezone correct | ⬜ | America/New_York (or appropriate) |
| Permalink structure | ⬜ | Set to: Post name (/%postname%/) |

**Settings to verify:**
```
Settings → General:
- Site Title: {{SITE_NAME}}
- Tagline: (leave blank for now)
- WordPress Address: https://{{DOMAIN}}
- Site Address: https://{{DOMAIN}}
- Admin Email: [verified email]
- Timezone: [correct timezone]

Settings → Permalinks:
- Common Settings: Post name
- Save Changes (important!)
```

---

### 3. MCP CONNECTION (Claude Code)

| Requirement | Status | Notes |
|-------------|--------|-------|
| MCP server URL obtained | ⬜ | From AI Engine plugin |
| MCP config file created | ⬜ | .mcp/config.json |
| Connection tested | ⬜ | Test from Claude Code |

**MCP Configuration:**
```json
{
  "mcpServers": {
    "wordpress-{{SITE_SLUG}}": {
      "url": "{{MCP_URL}}",
      "transport": "sse"
    }
  }
}
```

**Test command in Claude Code:**
```
Test the WordPress MCP connection for {{SITE_NAME}}.
List installed plugins.
```

---

### 4. PROJECT FILES

| Requirement | Status | Notes |
|-------------|--------|-------|
| CLAUDE.md generated | ⬜ | From CLAUDE.md Generator |
| BUILD-GUIDE.md present | ⬜ | This file |
| DNA file accessible | ⬜ | For reference |
| Project folder created | ⬜ | C:\Claude Code Projects\{{SITE_SLUG}}\ |

**Project folder structure:**
```
C:\Claude Code Projects\{{SITE_SLUG}}\
├── CLAUDE.md              ✓ Required
├── BUILD-GUIDE.md         ✓ Required
├── PREFLIGHT-CHECKLIST.md ✓ This file
├── PHASE-CHECKPOINTS.md   ✓ Required
├── PLUGIN-MANIFEST.md     ✓ Required
├── .mcp/
│   └── config.json        ✓ Required
└── notes/                 ○ Optional
```

---

### 5. ACCOUNTS & API KEYS

| Service | Status | Notes |
|---------|--------|-------|
| Hostinger access | ⬜ | hPanel login |
| Google Search Console | ⬜ | For SEO verification |
| Google Analytics 4 | ⬜ | Tracking property |
| RankMath account | ⬜ | For Pro license |
| QUIC.cloud account | ⬜ | For LiteSpeed CDN |
| ShortPixel account | ⬜ | For image optimization |

**API Keys to have ready:**
```
ShortPixel API Key: [from account]
QUIC.cloud Domain Key: [from account]
Google Analytics Measurement ID: G-XXXXXXXXXX
```

---

### 6. DESIGN ASSETS

| Asset | Status | Notes |
|-------|--------|-------|
| Logo (SVG preferred) | ⬜ | Or high-res PNG |
| Favicon (512x512) | ⬜ | PNG format |
| Social share image | ⬜ | 1200x630px |
| Hero images (if ready) | ⬜ | Site-specific |

**Asset locations:**
```
/assets/
├── logo.svg
├── logo.png (fallback)
├── favicon.png
├── og-image.png
└── hero/
    └── [hero images]
```

---

### 7. CONTENT PREPARATION

| Item | Status | Notes |
|------|--------|-------|
| Site tagline/description | ⬜ | From DNA |
| About page content | ⬜ | Draft at minimum |
| Contact information | ⬜ | Email, social links |
| Privacy policy draft | ⬜ | Can use generator |
| Terms of service draft | ⬜ | Can use generator |
| Initial content plan | ⬜ | At least pillar topics |

---

### 8. SITE-SPECIFIC REQUIREMENTS

{{SITE_SPECIFIC_REQUIREMENTS}}

---

## ✅ FINAL GO/NO-GO

Before proceeding to Phase 1:

| Check | Status |
|-------|--------|
| All infrastructure items green | ⬜ |
| WordPress admin accessible | ⬜ |
| MCP connection verified | ⬜ |
| All project files in place | ⬜ |
| Required accounts active | ⬜ |
| Basic assets available | ⬜ |

### GO Status: ⬜ READY / ⬜ NOT READY

**If NOT READY, resolve these items first:**
1. _________________________
2. _________________________
3. _________________________

---

## 🚀 Proceed to Phase 1

When all items are ✅, open Claude Code and run:

```
Read CLAUDE.md and BUILD-GUIDE.md.
Start Phase 1: Foundation.
```

---

*Generated by Site Build Orchestrator*
