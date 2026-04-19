# Portfolio v1 — Datacentre Background

Archived snapshot of the portfolio as it existed before the v2 redesign session (commit `9fdf808`, 2026-03-30).

## What's included

| File | Description |
|------|-------------|
| `index.html` | Main HTML at the time of archiving |
| `assets/css/main.css` | Base CSS (HTML5 UP Dimension template, includes `#bg` / `background.webp`) |
| `assets/css/secondary.css` | Custom overrides and component styles |
| `assets/js/main.js` | Template JS (article panels, animations) |
| `assets/js/gototop.js` | Scroll-to-top button |
| `assets/js/visitorcount.js` | AWS Lambda visitor counter |
| `assets/js/contact-form.js` | Formspree async contact handler |
| `images/background.webp` | The datacentre background image used in this version |

## How to restore

Copy these files back to the repo root (and `assets/` subdirectories) and deploy — the site will work as-is since it references the same Formspree endpoint, AWS API, and Credly/image paths.
