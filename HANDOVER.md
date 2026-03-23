# DCNS Lab Website Handover (Minimum Deliverable)

## 1) Project Overview

- Framework: Hugo + PaperMod
- Deployment: GitHub Pages (project site)
- URL: https://dcns-lab-fju.github.io/lab-website/
- Repository: DCNS-Lab-FJU/lab-website

This site uses a project-site base path (`/lab-website/`).
Do not hardcode `"/lab-website/"` in content links.

---

## 2) Local Development

### Prerequisites

- Hugo Extended (recommended latest)
- Git

### Run locally

```bash
hugo server -D
```

Local preview URL is usually:

```text
http://localhost:1313/lab-website/
```

### Production build check

```bash
hugo --minify
```

Generated files are in `public/` and should not be committed.

---

## 3) Content Structure

```text
content/
  _index.md
  members/
    _index.md
    faculty/
      _index.md
      lu-shu-ping.md
    students/
      _index.md
      student-demo.md
      student-template.md
  publications/
    _index.md

static/
  images/
    members/
  files/
    students/
```

---

## 4) Add or Update a Member

### Add faculty

1. Create a new file under `content/members/faculty/`.
2. Fill front matter and profile content.
3. Add photo to `static/images/members/`.
4. Use shortcode image syntax:

```markdown
{{< img src="images/members/example.jpg" alt="Example" w="220" >}}
```

### Add student

1. Copy `content/members/students/student-template.md` to a new file.
2. Update fields and profile text.
3. Put PDF outputs in `static/files/students/<student-id>/`.
4. Link files with shortcode:

```markdown
{{< filelink path="files/students/<student-id>/report.pdf" text="Project Report" >}}
```

---

## 5) Add Publications

Edit `content/publications/_index.md`.

Use this normalized format per item:

```markdown
- **Year:** 2026  
  **Authors:** A, B, C  
  **Title:** Paper title  
  **Venue:** Conference/Journal  
  **Link:** https://...
```

Keep sections:

- Journal Articles
- Conference Papers
- Patents
- Technical Reports

This keeps migration to YAML or BibTeX easy later.

---

## 6) Paths and Linking Rules (Project Site Safe)

### Internal page links

Use `relref`:

```markdown
[Members]({{< relref "/members/_index.md" >}})
```

### Static files

Use `filelink` shortcode (internally uses `relURL`):

```markdown
{{< filelink path="files/students/demo/report.pdf" text="Project Report" >}}
```

### Do not do

- Do not hardcode `/lab-website/...`
- Do not use root-only links like `/members/` in Markdown content

---

## 7) Mandatory Credits

Credits are configured in `hugo.toml` under `params.footer.text`.

Last updated is rendered in `layouts/partials/extend_footer.html` using page `Lastmod`.

For better timestamp quality, `enableGitInfo = true` is enabled.

---

## 8) Deployment

GitHub Actions workflow file:

- `.github/workflows/pages.yml`

Flow:

1. Push to `main`
2. Action builds Hugo site
3. Deploy to GitHub Pages

If deployment fails, check:

- Hugo version
- baseURL
- broken relative links
- missing submodule checkout

---

## 9) Common Pitfalls

1. **404 after deploy**
   Usually caused by hardcoded root paths.
2. **Image missing**
   Ensure files are in `static/images/...` and linked by shortcode.
3. **PDF link broken**
   Ensure files are in `static/files/...` and linked with `filelink`.
4. **Members page shows unwanted cards**
   Keep `content/members/_index.md` using `layout: "members"`.

---

## 10) PR Maintenance SOP (Recommended)

For each member update PR:

1. One topic per PR (member profile or publication update)
2. Include changed Markdown and assets only
3. Reviewer checklist:
   - links open correctly
   - image/PDF path valid
   - no hardcoded `/lab-website/`
   - `hugo --minify` passes locally or in CI

---

## 11) Future Upgrade Plan (Not Immediate)

1. Move publications to data-driven format (YAML/BibTeX)
2. Enable search for members/publications index
3. Add CSV/Excel export script (Python-based)
4. Move large PDFs/slides to GitHub Releases and keep website as index page
