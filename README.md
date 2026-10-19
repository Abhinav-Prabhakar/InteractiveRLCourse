# Interactive RL Course

An interactive-first reinforcement learning curriculum, from MDPs to RLHF. Each chapter is a single self-contained HTML page with LaTeX derivations and in-browser visualisations.

**Contents:** open [`index.html`](index.html) — the table of contents linking every chapter, grouped by part.

- `index.html` — the table of contents / landing page
- `outputs/` — the chapters (`NN-slug.html`), each fully self-contained
- `RL.html` — the design reference every chapter is matched against
- `prompt.md` — the brief each chapter is written from
- `index.md` — the curriculum outline
- `tools/` — maintenance scripts: `add_chapter_nav.py` (prev/next pager), `normalize_chapters.py` (consistent titles, eyebrows, arrow-key navigation), `prose-count.sh` (prose word count)

Chapters link to one another with Previous / Next / Contents navigation at the foot of every page, and the brand in the top bar returns to the contents.

## GitHub Pages

The site deploys automatically from `main` via GitHub Actions
(`.github/workflows/pages.yml`). The workflow assembles a static `_site/`
containing `index.html`, `outputs/`, and `RL.html`, then publishes it to
GitHub Pages. No build step and no gating checks — a push to `main` is all it
takes.
