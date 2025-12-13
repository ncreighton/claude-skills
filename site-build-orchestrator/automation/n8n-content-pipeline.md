# n8n Automation Integration

## Complete Automation System for Empire Operations

This guide defines the automation workflows that power hands-off content publishing, monitoring, and multi-site coordination across all 17 sites.

---

## Automation Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         n8n AUTOMATION HUB                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐         │
│  │ CONTENT         │    │ PUBLISHING      │    │ MONITORING      │         │
│  │ GENERATION      │    │ PIPELINE        │    │ & ALERTS        │         │
│  │                 │    │                 │    │                 │         │
│  │ • ZimmWriter    │───▶│ • Review queue  │───▶│ • Health checks │         │
│  │ • Image gen     │    │ • Formatting    │    │ • Analytics     │         │
│  │ • Scheduling    │    │ • Publishing    │    │ • Performance   │         │
│  └─────────────────┘    └─────────────────┘    └─────────────────┘         │
│           │                      │                      │                   │
│           ▼                      ▼                      ▼                   │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                        INTEGRATION LAYER                             │   │
│  │                                                                      │   │
│  │   WordPress MCP    Google Sheets    Slack    Email    Telegram       │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Core Workflows

### 1. Content Publishing Pipeline

**Trigger:** New row in Google Sheet OR manual trigger
**Purpose:** Auto-publish content from ZimmWriter to WordPress

```yaml
workflow: content_publishing_pipeline
trigger: 
  - google_sheets_new_row (Content Queue sheet)
  - manual

steps:
  1. get_content:
     - source: google_drive OR local_folder
     - format: HTML or Markdown
     
  2. validate_content:
     - check: word_count >= 1500
     - check: has_title
     - check: has_meta_description
     - on_fail: send_alert, skip
     
  3. select_site:
     - match: content_category → site_mapping
     - get: site_credentials
     
  4. format_content:
     - apply: site_specific_formatting
     - add: internal_links (from link database)
     - add: affiliate_links (if applicable)
     - add: featured_image (if not present)
     
  5. publish_to_wordpress:
     - via: WordPress MCP or REST API
     - status: draft OR scheduled
     - set: categories, tags, excerpt
     - set: SEO (RankMath fields)
     
  6. post_publish:
     - submit: Google Indexing API
     - add: to_social_queue
     - update: content_log
     - notify: slack/telegram

  7. verify:
     - check: post_live
     - check: no_errors
     - log: success/failure
```

### 2. Multi-Site Health Monitor

**Trigger:** Scheduled (every 6 hours)
**Purpose:** Monitor all sites for uptime and issues

```yaml
workflow: empire_health_monitor
trigger: schedule("0 */6 * * *")  # Every 6 hours

steps:
  1. for_each_site:
     sites: [list_of_17_sites]
     
     check:
       - uptime: HTTP GET homepage, expect 200
       - ssl: certificate_valid, not_expiring_soon
       - performance: PageSpeed API score
       - backup: UpdraftPlus last_backup_date
       - security: Wordfence last_scan
       
  2. aggregate_results:
     - compile: status_for_each_site
     - flag: any_issues
     
  3. alert_if_issues:
     if: any_site_down OR ssl_expiring OR backup_old
     then:
       - slack: @nick #alerts
       - telegram: urgent_channel
       - email: nick@email.com
       
  4. daily_report:
     if: time == "08:00"
     then:
       - compile: daily_health_summary
       - send: slack #daily-report
```

### 3. Analytics Aggregation

**Trigger:** Daily at 6 AM
**Purpose:** Compile analytics across all sites

```yaml
workflow: daily_analytics_rollup
trigger: schedule("0 6 * * *")

steps:
  1. fetch_analytics:
     for_each_site:
       - google_analytics_4:
           metrics: [sessions, users, pageviews, bounce_rate, revenue]
           period: yesterday
       - google_search_console:
           metrics: [clicks, impressions, ctr, position]
           period: yesterday
           
  2. aggregate:
     - total_sessions: sum(all_site_sessions)
     - total_revenue: sum(affiliate + ads)
     - top_performers: rank_by(sessions)
     - biggest_changes: compare_to_yesterday
     
  3. generate_report:
     - format: structured_summary
     - include: highlights, concerns, opportunities
     
  4. distribute:
     - google_sheet: Empire Analytics Master
     - slack: #analytics
     - email: weekly_digest (if Monday)
```

### 4. Content Queue Manager

**Trigger:** Daily at 5 AM
**Purpose:** Manage content scheduling across sites

```yaml
workflow: content_queue_manager
trigger: schedule("0 5 * * *")

steps:
  1. check_publishing_schedule:
     for_each_site:
       - posts_scheduled_today
       - content_gap_days (days since last publish)
       
  2. alert_gaps:
     if: content_gap_days > 7
     then:
       - alert: "Site [X] hasn't published in [Y] days"
       - suggest: next_priority_content
       
  3. balance_queue:
     - ensure: no_site_over_3_posts_per_day
     - redistribute: if_unbalanced
     
  4. prepare_social:
     - for_scheduled_posts: queue_social_shares
     - platforms: twitter, pinterest, facebook
```

### 5. Image Generation Pipeline

**Trigger:** Content needs images
**Purpose:** Auto-generate featured images

```yaml
workflow: image_generation
trigger: 
  - new_content_without_image
  - manual

steps:
  1. analyze_content:
     - extract: title, main_topic, mood
     - determine: site_style (from DNA)
     
  2. generate_prompt:
     - template: site_specific_prompt_template
     - include: style_guidelines, color_palette
     - avoid: site_specific_forbidden_elements
     
  3. generate_image:
     - api: midjourney OR dalle OR stable_diffusion
     - size: 1200x630 (og:image compatible)
     - variations: 2-3 options
     
  4. optimize_image:
     - compress: lossy, quality 85
     - convert: webp
     - resize: multiple sizes for responsive
     
  5. upload_to_wordpress:
     - via: WordPress MCP
     - set: alt_text, title, caption
     - attach: to_post
```

### 6. Backup Verification

**Trigger:** Daily at 3 AM
**Purpose:** Ensure all backups are current and valid

```yaml
workflow: backup_verification
trigger: schedule("0 3 * * *")

steps:
  1. check_updraftplus:
     for_each_site:
       - last_backup_date
       - backup_size
       - backup_location (google_drive)
       
  2. verify_integrity:
     - check: backup_files_exist
     - check: file_sizes_reasonable
     - optional: test_restore (staging)
     
  3. alert_issues:
     if: backup_older_than_48_hours OR backup_missing
     then:
       - alert: URGENT_backup_issue
       - trigger: manual_backup
       
  4. monthly_test:
     if: first_of_month
     then:
       - select: random_site
       - perform: test_restore_to_staging
       - verify: site_functional
       - report: test_results
```

---

## Site-Specific Automation Configs

### WitchcraftForBeginners
```yaml
site_id: witchcraft-for-beginners
automations:
  - moon_phase_content:
      trigger: moon_phase_change
      action: publish_moon_content_reminder
      
  - sabbat_content:
      trigger: 2_weeks_before_sabbat
      action: alert_sabbat_content_needed
      
  - ritual_scheduling:
      preferred_publish_times: [tuesday, thursday]
      time: "09:00 EST"
```

### SmartHomeWizards
```yaml
site_id: smart-home-wizards
automations:
  - price_tracking:
      trigger: daily
      action: check_amazon_prices
      alert_if: price_drop > 20%
      
  - new_product_alerts:
      trigger: weekly
      action: scan_for_new_smart_home_products
      
  - review_update_reminders:
      trigger: product_age > 6_months
      action: remind_to_update_review
```

### AIinActionHub
```yaml
site_id: ai-in-action-hub
automations:
  - news_monitoring:
      trigger: hourly
      sources: [arxiv, techcrunch, verge]
      keywords: [AI, LLM, GPT, Claude]
      action: add_to_news_queue
      
  - tool_tracking:
      trigger: weekly
      action: check_for_new_ai_tools
```

---

## Workflow Templates

### Template: Basic Content Publisher
```json
{
  "name": "Basic Content Publisher",
  "nodes": [
    {
      "type": "trigger_manual",
      "name": "Manual Trigger"
    },
    {
      "type": "google_sheets_read",
      "name": "Get Content from Sheet",
      "params": {
        "spreadsheet_id": "{{CONTENT_QUEUE_SHEET}}",
        "range": "Queue!A:Z",
        "filter": "Status = 'Ready'"
      }
    },
    {
      "type": "http_request",
      "name": "Publish to WordPress",
      "params": {
        "method": "POST",
        "url": "{{SITE_URL}}/wp-json/wp/v2/posts",
        "auth": "application_password",
        "body": {
          "title": "{{title}}",
          "content": "{{content}}",
          "status": "draft"
        }
      }
    },
    {
      "type": "slack_message",
      "name": "Notify Success",
      "params": {
        "channel": "#content-published",
        "message": "Published: {{title}} to {{site_name}}"
      }
    }
  ]
}
```

### Template: Site Health Check
```json
{
  "name": "Site Health Check",
  "nodes": [
    {
      "type": "trigger_schedule",
      "name": "Every 6 Hours",
      "params": {
        "cron": "0 */6 * * *"
      }
    },
    {
      "type": "http_request",
      "name": "Check Site Up",
      "params": {
        "method": "GET",
        "url": "{{SITE_URL}}",
        "timeout": 30
      }
    },
    {
      "type": "if",
      "name": "Check Response",
      "conditions": [
        {
          "field": "statusCode",
          "operator": "not_equals",
          "value": 200
        }
      ]
    },
    {
      "type": "telegram_message",
      "name": "Alert Down",
      "params": {
        "chat_id": "{{ALERT_CHAT}}",
        "message": "🚨 SITE DOWN: {{site_name}}"
      }
    }
  ]
}
```

---

## Credentials Required

### Per-Site Credentials
```
WordPress:
- Application Password (for REST API)
- Or: MCP Connection URL

Google:
- Google Sheets API (content queue)
- Google Drive API (backups, content storage)
- Google Analytics 4 API
- Google Search Console API
- Google Indexing API

Affiliate:
- Amazon PA-API credentials
- Other network API keys
```

### Global Credentials
```
Notification:
- Slack Webhook URL
- Telegram Bot Token
- Email SMTP credentials

Image Generation:
- Midjourney API (via proxy)
- OpenAI API (DALL-E)
- Stability AI API

Monitoring:
- PageSpeed API key
- Uptime Robot API
```

---

## Implementation Checklist

### Phase 1: Foundation
```
□ n8n instance running (Docker or cloud)
□ All site credentials stored
□ Slack/Telegram notifications working
□ Google Sheets connected
```

### Phase 2: Publishing
```
□ Content queue sheet created
□ Basic publisher workflow active
□ Formatting rules configured per site
□ Post-publish verification working
```

### Phase 3: Monitoring
```
□ Health check workflow scheduled
□ Analytics aggregation running
□ Backup verification active
□ Alert thresholds configured
```

### Phase 4: Advanced
```
□ Image generation pipeline
□ Auto-internal linking
□ Social media scheduling
□ Cross-site content coordination
```

---

## Troubleshooting

### Common Issues

**Workflow Not Triggering:**
- Check: Cron schedule format
- Check: Trigger credentials valid
- Check: n8n service running

**WordPress API Errors:**
- Check: Application password correct
- Check: REST API enabled
- Check: User has publish permissions

**Rate Limiting:**
- Add: Delays between API calls
- Use: Batch operations where possible
- Implement: Exponential backoff

---

*n8n Automation Integration - Site Build Orchestrator v2.0*
