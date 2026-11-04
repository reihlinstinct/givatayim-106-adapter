# Givatayim municipal form adapter (fill-only)

The optional [Givatayim adapter design](docs/design/GIVATAYIM-FILL-ONLY.md)
uses a fresh resident-owned session to fill the official form. It has **no report
submission capability**. No captcha bypass or token reuse. The caller provides
the resident's own details, never another person's reporter identity.

Install this package and Playwright browser dependencies, then use:

```python
from playwright.sync_api import sync_playwright
from givatayim_adapter import create_session

# RESIDENT_REPORT is a validated ResidentReport containing the resident's input.
with sync_playwright() as playwright:
    browser = playwright.chromium.launch()
    session = create_session(browser)
    try:
        session.open()
        result = session.fill(RESIDENT_REPORT)
        assert result["submission_enabled"] is False
    finally:
        session.close()
        browser.close()
```

`ResidentReport` fields: first_name, last_name, mobile_phone, national_id,
resident_street_id, resident_house_number, incident_street_id,
incident_house_number, description, and attachments (tuple of image Paths).
Description: 1-700 characters. Four JPG/PNG attachments maximum, 10 MB each.
No data is logged or persisted. Enable the module logger's DEBUG level only for
stage codes. On any failure close the session and start fresh, never retry a
partially filled session. Do not remove its guards to submit.

Offline browser tests: `docker build --target test .`. Both Chromium
and WebKit use a synthetic intercepted form with no municipality requests.
An ordinary passive headless load on 2026-11-04 was stopped at Cloudflare
human verification (403) and obtained no token. Actual live filling and municipal
acceptance remain unverified; a separately
approved real Givatayim case is required before any live submission testing.

Python3.11+; version0.1.0. CI enforces80% branch coverage with synthetic Chromium/WebKit tests in containers. See CONTRIBUTING.md, SECURITY.md and CHANGELOG.md.
