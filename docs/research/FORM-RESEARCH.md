# Official form research, 2026-11-04

Sources: two resident-supplied saved page loads of the official public form.
Raw source and changing session/token values are excluded.
Official form: https://www.givatayim.muni.il/moked/
Contact page: https://givatayim.muni.il/516/

Binaa Smart Form46 declares multipart POST to /moked/#form-46. An external
Smart Form script may intercept submission, so this is not a documented API.
The script could not be read because of Cloudflare verification; no bypass.
Fresh csrf and page_session_hash values differed across snapshots. No values
are recorded. Turnstile is present. No captcha token was replayed or submitted.

Fields: c2100 first name, c6100 surname, c8100 mobile, c47100 resident branch,
c21100 ID, c11100 resident street, c14100 resident house, c26100 incident street,
c29100 incident house, c32100 description (700 characters). Four10MB files:
c35100, c39100, c45100, c1684132793. Adapter supports JPG/PNG filenames only.
No category field observed. Street IDs must exist in the current form.

Passive unmodified headless Chromium returned403 and stayed at human
verification after30seconds. Token empty, form absent, fresh CSRF/session
unconfirmed. No live report, upload, test submission or municipal letter sent.
