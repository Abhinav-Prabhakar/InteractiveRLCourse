# Interactive RL Course

An interactive-first reinforcement learning curriculum, from MDPs to RLHF. Each chapter and project is a single self-contained HTML page with LaTeX derivations and in-browser visualisations.

**Contents:** open [`index.html`](index.html) — the table of contents linking every chapter and project, grouped by part. Projects sit at the end of the part they extend.

- `index.html` — the table of contents / landing page
- `outputs/` — the 22 chapters (`NN-slug.html`), each fully self-contained
- `projects/` — the 6 guided project labs (`NN-slug.html`), slotted between parts on the contents page
- `RL.html` — the design reference every page is matched against
- `prompt.md` — the brief each chapter is written from
- `prompt-projects.md` — the brief each project is written from
- `index.md` — the curriculum outline
- `tools/` — maintenance scripts: `add_chapter_nav.py` (chapter pager), `normalize_chapters.py` (chapter chrome), `normalize_projects.py` (project chrome + pager), `prose-count.sh`

Chapters and projects link to one another with Previous / Next / Contents navigation at the foot of every page, the brand in the top bar returns to the contents, and ← / → move between pages. Project pages add syntax-highlighted code blocks (self-contained highlighter, same palette) alongside their interactive labs.

## GitHub Pages

The site deploys automatically from `main` via GitHub Actions
(`.github/workflows/pages.yml`). The workflow assembles a static `_site/`
containing `index.html`, `outputs/`, and `RL.html`, then publishes it to
GitHub Pages. No build step and no gating checks — a push to `main` is all it
takes.
