# Coyote Legal — Google Sheets lead capture

Both forms (study guide + contact) POST leads to a Google Sheet.

## One-time setup (~5 minutes)

1. Go to [Google Sheets](https://sheets.google.com) → **Blank spreadsheet**
2. Name it **Coyote Legal Leads**
3. **Extensions → Apps Script**
4. Delete any code in the editor and paste everything from `scripts/google-apps-script.gs`
5. Click **Save** (name the project "Coyote Legal Leads")
6. **Deploy → New deployment**
   - Type: **Web app**
   - Execute as: **Me**
   - Who has access: **Anyone**
7. Click **Deploy** → authorize when prompted → copy the **Web App URL**
8. Open `assets/js/leads-config.js` and replace the placeholder:

```javascript
var LEADS_ENDPOINT = 'https://script.google.com/macros/s/YOUR_ID/exec';
```

9. Commit and push (or tell your developer to push)

## Test

1. Visit `study-guide.html` on the live site
2. Submit the form with test data
3. A new row should appear in your Google Sheet within a few seconds

## Sheet columns

| Timestamp | Source | Name | Email | Phone | Office | Message | Page |
|-----------|--------|------|-------|-------|--------|---------|------|
| | study-guide or contact | | | | Dallas / Ft. Worth | | /study-guide.html |

## Until the URL is configured

Forms fall back to opening a `mailto:` to `baba@coyotelegal.com` — same broken behavior as before. **The Web App URL must be set for leads to land in Sheets.**
