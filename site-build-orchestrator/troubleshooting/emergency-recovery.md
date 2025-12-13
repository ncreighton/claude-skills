# Troubleshooting & Emergency Recovery

## Quick Reference: Emergency Contacts

| Issue | First Response | Escalation |
|-------|---------------|------------|
| Site Down | Clear cache, check hosting | Hostinger support |
| Hacked | Wordfence scan, maintenance mode | Security specialist |
| Data Loss | UpdraftPlus restore | Hostinger backups |
| SSL Issues | Hostinger panel | Let's Encrypt support |
| Plugin Conflict | Disable plugins via FTP | Developer support |

---

## 🚨 Emergency Decision Tree

```
SITE PROBLEM DETECTED
        │
        ▼
Is the site loading at all?
        │
   ┌────┴────┐
   │         │
  YES       NO → SITE DOWN PROCEDURE
   │
   ▼
Is it showing correctly?
        │
   ┌────┴────┐
   │         │
  YES       NO → DISPLAY ISSUE PROCEDURE
   │
   ▼
Is it working correctly?
        │
   ┌────┴────┐
   │         │
  YES       NO → FUNCTIONALITY ISSUE
   │
   ▼
Is it fast enough?
        │
   ┌────┴────┐
   │         │
  YES       NO → PERFORMANCE ISSUE
   │
   ▼
ALL GOOD ✓
```

---

## Site Down Procedure

### Step 1: Verify It's Actually Down (2 min)
```
Checks:
□ Try from different browser (incognito)
□ Try from phone on cellular (not WiFi)
□ Check downfor.io or isitdown.site
□ Check from different location (VPN)

If only YOU can't access:
- Clear browser cache
- Check your DNS/ISP
- Try different DNS (8.8.8.8)
```

### Step 2: Check Hosting Status (3 min)
```
□ Login to Hostinger hPanel
□ Check server status indicator
□ Check for maintenance notices
□ Review error logs in hPanel
□ Check Hostinger status page

If Hostinger is down:
- Wait for resolution
- Check Hostinger status Twitter
- Submit support ticket if prolonged
```

### Step 3: Check for Obvious Errors (5 min)
```
□ Can you access wp-admin?
□ What error message shows?

Common errors:
- "Error establishing database connection" → DB issue
- "500 Internal Server Error" → PHP/plugin issue
- "503 Service Unavailable" → Server overload
- White screen (WSOD) → PHP fatal error
- "This site can't be reached" → DNS/server issue
```

### Step 4: Fix Common Issues

#### Database Connection Error
```
1. Check database credentials in wp-config.php
2. Access phpMyAdmin from hPanel
3. If DB exists and credentials correct → restart MySQL
4. If DB missing → restore from backup
```

#### 500 Internal Server Error
```
1. Access site via FTP/File Manager
2. Check .htaccess file - rename to .htaccess.bak
3. Check PHP error log
4. Disable plugins (rename /wp-content/plugins to /plugins.bak)
5. Test - if works, plugins caused it
6. Re-enable plugins one by one to find culprit
```

#### White Screen of Death
```
1. Enable WP_DEBUG in wp-config.php:
   define('WP_DEBUG', true);
   define('WP_DEBUG_LOG', true);
   define('WP_DEBUG_DISPLAY', false);
2. Check /wp-content/debug.log for error
3. Usually: plugin conflict or PHP memory
4. Increase memory: define('WP_MEMORY_LIMIT', '256M');
5. Disable plugins via FTP if needed
```

### Step 5: Restore from Backup
```
If nothing works:
1. Access hPanel or UpdraftPlus
2. Find most recent clean backup
3. Restore files and database
4. Verify site works
5. Investigate what caused issue
6. Re-apply any changes carefully
```

---

## Hacked/Malware Procedure

### Immediate Actions (First 15 min)

```
1. ENABLE MAINTENANCE MODE
   - Use plugin or add to .htaccess:
   RewriteEngine On
   RewriteCond %{REMOTE_ADDR} !^YOUR\.IP\.ADDRESS
   RewriteRule .* - [R=503,L]

2. CHANGE ALL PASSWORDS
   - WordPress admin password
   - Database password
   - FTP password
   - Hosting account password
   - Any API keys exposed

3. DOCUMENT WHAT YOU SEE
   - Screenshot any defacement
   - Note any strange files
   - Record timestamps
```

### Investigation (30-60 min)

```
1. RUN WORDFENCE SCAN
   - Full scan with high sensitivity
   - Check for modified core files
   - Check for unknown files
   - Review scan results

2. CHECK FILE MODIFICATION TIMES
   - Via FTP, sort by date modified
   - Look for recently changed files
   - Especially in: /wp-content/, /wp-includes/
   - Any .php files in /uploads/ is BAD

3. CHECK USER ACCOUNTS
   - Look for unknown admin users
   - Check for privilege escalation
   - Review user creation dates

4. CHECK .HTACCESS AND WP-CONFIG.PHP
   - Look for injected code
   - Compare to clean versions
```

### Cleaning Options

#### Option A: Clean Restore (Recommended)
```
1. Backup current state (for forensics)
2. Delete all WordPress files
3. Fresh WordPress install
4. Restore wp-content/uploads (scan first)
5. Re-install theme from scratch
6. Re-install plugins from fresh downloads
7. Import database (after scanning)
8. Change all passwords again
9. Harden security
```

#### Option B: Manual Cleaning (If restore not possible)
```
1. Replace all core files with fresh download
2. Delete and re-download all plugins
3. Delete and re-download theme
4. Manually review custom code
5. Clean database of suspicious entries
6. Very time-consuming - restore usually better
```

### Post-Cleanup Hardening
```
□ Update WordPress, all plugins, all themes
□ Delete unused plugins and themes
□ Add 2FA to all admin accounts
□ Install security plugin (Wordfence)
□ Configure firewall rules
□ Set correct file permissions (644/755)
□ Disable file editing in wp-config.php:
  define('DISALLOW_FILE_EDIT', true);
□ Limit login attempts
□ Change database prefix if default (wp_)
□ Consider changing salts in wp-config.php
```

### Google Recovery (if blacklisted)
```
If Google flagged site:
1. Verify site in Search Console
2. Submit malware removal request
3. Wait for Google re-review (24-72 hours)
4. Monitor Search Console for issues
```

---

## Plugin Conflict Resolution

### Identify the Problem Plugin

```
METHOD 1: Binary Search (Fast)
1. Deactivate half of all plugins
2. Test if problem persists
3. If fixed: problem in deactivated group
   If not: problem in active group
4. Repeat with problem group
5. Narrow down to single plugin

METHOD 2: One-by-One (Thorough)
1. Deactivate ALL plugins (via FTP if needed)
2. Activate ONE plugin, test
3. Repeat until problem appears
4. Problem plugin identified

METHOD 3: Safe Mode
1. Create mu-plugin to disable all plugins
2. Use WP-CLI: wp plugin deactivate --all
```

### Common Conflict Patterns

```
Caching + Forms:
- Problem: Forms don't submit, show cached responses
- Fix: Exclude form pages from cache

SEO Plugins (multiple):
- Problem: Duplicate meta tags, conflicts
- Fix: Use only ONE SEO plugin

Security + Performance:
- Problem: Firewall blocks optimization
- Fix: Whitelist optimization plugin

Page Builder + Theme:
- Problem: Styling conflicts
- Fix: Disable theme styling for builder pages
```

### When to Seek Help
```
Seek developer help if:
- Problem persists after all plugins disabled
- Error logs show database corruption
- Core WordPress files modified
- You've spent >2 hours without progress
```

---

## Performance Emergencies

### Site Suddenly Slow

```
IMMEDIATE CHECKS:
□ Check hosting server load (hPanel)
□ Check if traffic spike (Google Analytics)
□ Check for runaway processes (phpMyAdmin)
□ Clear all caches
□ Check for plugin auto-updates that broke things

COMMON CAUSES:
1. Bad plugin update → roll back
2. Traffic spike → increase resources
3. Database bloat → optimize tables
4. Uncached heavy queries → add caching
5. External resource timeout → lazy load
```

### Core Web Vitals Failure

```
LCP TOO HIGH (>2.5s):
□ Preload largest image
□ Eliminate render-blocking resources
□ Upgrade hosting if TTFB is slow
□ Use CDN for images

CLS TOO HIGH (>0.1):
□ Add width/height to images
□ Reserve space for ads
□ Don't insert content above existing

FID/INP TOO HIGH:
□ Defer non-critical JavaScript
□ Break up long tasks
□ Remove unused JavaScript
```

---

## SSL/HTTPS Issues

### Mixed Content Warnings
```
Cause: HTTP resources on HTTPS page

Fix:
1. Run Really Simple SSL plugin
2. Or search/replace in database:
   http://yourdomain.com → https://yourdomain.com
3. Check for hardcoded HTTP in theme/plugins
```

### SSL Certificate Expired
```
1. Check certificate status in hPanel
2. Usually auto-renews - check for errors
3. Manually renew in hPanel if needed
4. If using Cloudflare, check there too
5. Clear browser cache after renewal
```

### SSL Not Working at All
```
1. Check hosting SSL settings
2. Ensure domain pointed correctly
3. Wait for DNS propagation (up to 48h)
4. Force HTTPS in .htaccess:
   RewriteEngine On
   RewriteCond %{HTTPS} off
   RewriteRule ^(.*)$ https://%{HTTP_HOST}%{REQUEST_URI} [L,R=301]
```

---

## Data Loss Recovery

### Accidental Content Deletion

```
1. CHECK TRASH FIRST
   - Posts/Pages: All Posts → Trash
   - Stays in trash 30 days by default

2. CHECK REVISIONS
   - Edit post/page
   - Look for "Revisions" in sidebar
   - Restore previous version

3. RESTORE FROM BACKUP
   - UpdraftPlus: selective restore
   - Hostinger: automatic daily backups
   - Restore database only if possible
```

### Database Corruption

```
Signs:
- Random errors on different pages
- "Error establishing database connection"
- Tables missing or damaged

Fix:
1. phpMyAdmin → Select database
2. Check all tables → "Repair table"
3. If fails, restore database from backup
4. Consider: wp db repair (WP-CLI)
```

---

## Rollback Procedures

### Plugin Rollback
```
1. Via WP Rollback plugin (install if needed)
2. Or manually:
   - Download older version from wordpress.org
   - Delete current plugin via FTP
   - Upload older version
   - Activate
```

### Theme Rollback
```
1. If child theme: restore from backup
2. If parent theme: download older version
3. Access via FTP if wp-admin broken
```

### WordPress Core Rollback
```
1. Download specific version from wordpress.org/download/releases/
2. Via FTP:
   - Delete wp-admin and wp-includes
   - Upload from downloaded version
   - DO NOT delete wp-content
```

### Database Rollback
```
1. UpdraftPlus → Restore → Database only
2. Or phpMyAdmin: Import backup SQL file
3. Warning: May lose content since backup
```

---

## Preventive Measures

### Daily Automated Checks
```yaml
checklist:
  - uptime_monitoring: enabled
  - backup_verification: daily
  - security_scan: scheduled
  - performance_check: automated
```

### Weekly Manual Checks
```
□ Review Wordfence dashboard
□ Check for plugin/theme updates
□ Review error logs
□ Verify backups completed
□ Check site speed
```

### Monthly Audit
```
□ Full security scan
□ Backup restoration test
□ Performance deep-dive
□ Update all plugins (on staging first)
□ Review user accounts
□ Check SSL certificate expiry
```

---

## Emergency Kit

### Files to Keep Ready
```
/emergency-kit/
├── fresh-wordpress.zip (latest version)
├── clean-htaccess.txt (default)
├── clean-wp-config-template.php
├── maintenance-page.html
├── emergency-contacts.txt
└── site-credentials-encrypted.txt
```

### Commands to Know
```bash
# Disable all plugins (WP-CLI)
wp plugin deactivate --all

# Reset password
wp user update admin --user_pass=newpassword

# Search replace (if moved/cloned)
wp search-replace 'oldurl.com' 'newurl.com'

# Repair database
wp db repair

# Flush cache
wp cache flush

# Check for core file integrity
wp core verify-checksums
```

---

## When to Escalate

### Hostinger Support
- Server-side issues
- Can't access hPanel
- SSL problems
- Database server issues
- DDoS attacks

### Security Professional
- Confirmed hack beyond basic cleanup
- Sensitive data potentially compromised
- Repeat infections
- Legal/compliance concerns

### Developer
- Custom code issues
- Complex plugin conflicts
- Database corruption
- Theme structural problems

---

*Troubleshooting & Emergency Recovery - Site Build Orchestrator v2.0*
