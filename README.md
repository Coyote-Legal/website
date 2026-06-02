# Coyote Legal — GitHub Pages

Static website for [coyotelegal.com](https://coyotelegal.com) — Margaret A. Donnelly, P.C.

## Deploy to GitHub Pages

1. Create a new GitHub repository (e.g. `coyotelegal`).
2. Push this folder:

```bash
cd /home/baba/coyotelegal
git init
git add .
git commit -m "Initial Coyote Legal website for GitHub Pages"
git branch -M main
git remote add origin git@github.com:YOUR_USERNAME/coyotelegal.git
git push -u origin main
```

3. In GitHub → **Settings → Pages**:
   - Source: **Deploy from a branch**
   - Branch: **main** / **/ (root)**
   - Save

4. Point `coyotelegal.com` DNS to GitHub Pages (add the custom domain in Pages settings and configure your DNS A/CNAME records per GitHub docs).

## Pages

| Page | File |
|------|------|
| Home | `index.html` |
| About | `about.html` |
| Services | `services.html` |
| Testimonials | `testimonials.html` |
| Social Feed | `social.html` |
| Contact | `contact.html` |
| Study Guide (lead funnel) | `study-guide.html` |
| Disclaimer | `disclaimer.html` |

## CRM hookup

The study guide form stores leads in `localStorage` for now. To connect a CRM (HubSpot, Mailchimp, etc.), replace the submit handler in `study-guide.html` with your form endpoint or webhook URL.

The contact form currently opens a `mailto:` draft — swap the submit handler in `contact.html` when you have a CRM endpoint.

## Local preview

```bash
cd /home/baba/coyotelegal
python3 -m http.server 8765
```

Open http://127.0.0.1:8765
