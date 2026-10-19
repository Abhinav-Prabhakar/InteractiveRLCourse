You are writing ONE chapter of an interactive reinforcement-learning book. The
output is a single self-contained HTML file that should look like a sibling of
`RL.html` and teach its topic exceptionally well. Other agents are writing the
other chapters in parallel, so follow the shared conventions below closely and
use your own judgement for everything else.

# Inputs
- `RL.html` — the design reference. Read all of it before you start. It is the
  ground truth for look, components, writing voice, and JS style.
- `index.md` — the book's table of contents. Use it for context: what earlier
  chapters have already taught, what later ones will cover, and how to refer to
  them. Treat the bullet list for your chapter as a guide to scope, not a
  checklist. Ignore its mentions of quizzes and coding exercises unless you
  find a format that actually helps the reader (see below).
- Your chapter number, title, file name, and neighbours, given in your task.

Do not open anything in `outputs/`.

# Output
- Write exactly one file: `results/<NN>-<slug>.html` (the name is given in your
  task). Do not create or modify any other file.
- Self-contained: one `<style>`, one `<script>`. KaTeX 0.16.9 from the same CDN
  as the reference is the only external dependency. No images, no build step.

# Design
- Start from the reference's full `<style>` block, copied as-is, so tokens,
  type, spacing, buttons, sliders, `.eqbox`, `.note`, `.panel`, `table.cmp`,
  etc. are identical. Drop rules you don't use; add new ones only when you
  need a new component, built from the same tokens (palette: #111 primary,
  #2563eb positive, #dc2626 negative, #c2c9d4 inactive, #fafafa/#f0f0f0 muted
  panels, #eef2ff/#1e3a8a highlight). Keep the `@media (max-width:640px)` block
  and extend it if your components need it.
- Same skeleton: sticky `.topbar` (brand, nav anchors, `#progress`), `.hero`
  (eyebrow, h1, one-sentence lede), numbered `section`s with
  `<h2><span class="num">NN</span>Title</h2>`, a final Summary section with a
  `table.cmp` and a "Cheat sheet" `.eqbox`, then `footer`.
- Reuse the reference's `.tip` and `.def` components with `initExplanations()`:
  `.def` for first-use jargon, `.tip` for a non-obvious mathematical step
  (`.eq-split` when only part of a display equation is the trigger,
  `.tip.eq-block` for the whole display). Both are accessible and restrained;
  do not underline every bold term or explain every formula.
- No emoji, icons, decorative gradients, or illustrations.

# Shared conventions (keep these identical across chapters)
- `<title>`: `Chapter N · <Title>`.
- Brand in topbar: `<span class="brand">Ch. NN · <Short title></span>`.
- Eyebrow: `Reinforcement Learning · Part <Roman> · Chapter N`.
- Footer: chapter navigation, in this exact form (omit a side that doesn't exist):
  ```html
  <footer>
    <div class="wrap" style="display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap">
      <a href="<prev-file>" style="color:#9ca3af">← Ch. NN · <Prev title></a>
      <a href="<next-file>" style="color:#9ca3af">Ch. NN · <Next title> →</a>
    </div>
  </footer>
  ```
- The Summary's last line is a single `<p class="small muted">` sentence that
  points forward to the next ideas in the book by name.

# Writing
The reader is smart, comfortable with linear algebra, probability and calculus,
and new to RL. Write exactly like `RL.html`: compressed, confident, fast. Study
its prose before you write a word. The equation does the explaining; prose
frames it and reads it back.

**Shape of one idea.** One or two framing sentences, then the `.eqbox`, then a
single interpretive line or a short `.note`. That is the unit. A chapter grows
by covering more ideas, never by spending more words per idea. If an idea seems
to need a paragraph, find the sharper sentence or let a visualiser carry it.

**Devices the reference uses (use them, sparingly):**
- One-sentence lede. No throat-clearing anywhere.
- Bolded verdicts: "**the state is a sufficient statistic for the future.**",
  "**The $\max$ is the whole story.**" (at most one per section).
- Contrastive italics: *where you are* vs. *how you got there*.
- Pointing at the load-bearing step: "The third line is exactly where the
  Markov property is spent."
- A "read it back" line after a dense equation (once or twice per chapter).
- Terse imperative invitations: "Drag the slider and watch…", "Click a state
  to plug its numbers into the Bellman equation."
- Bold a technical term on first use.

**Cut on sight:** restating what an equation already says, previews and
recaps, "in this section", roadmaps, objective boxes, takeaway lists, hedges,
transitional filler, step-by-step derivation narration (one pointer to the key
step is enough).

**Self-check per paragraph:** could `RL.html` have said this in fewer words?
If yes, rewrite it. Every number quoted in prose must match what the page
computes (verify by running the same model in node). Notation follows the
reference; use μ for state distributions so π always means a policy.

# Interactive visualisations
These are the heart of the chapter: the page should be visual-first, with the
prose as connective tissue between panels. Build plenty — typically 5–7 — so
that almost every major idea has something to touch, including the one
suggested in `index.md` (adapt it if a better design teaches the same thing).
Small focused panels (one slider, one live equation) count as much as big
sandboxes; mix both. When a visual can replace a paragraph, replace the
paragraph. Good visualisers:
- encode exactly the math the surrounding prose just stated;
- give the reader real parameters to change and something non-obvious to
  discover by changing them;
- show the equation with the reader's live numbers in an `.eqbox` where it
  makes sense;
- run real algorithms in the browser (simulate, learn, iterate) rather than
  replaying canned data, and stop animations at convergence.

Follow the reference's JS style: SVG drawn programmatically, the shared helpers
(`NS`, `el`, `T`, `inv`, `$`, `$$`) at the top of the script, one `init<Name>()`
per visualiser, all called from one `DOMContentLoaded` handler after
`renderMathInElement`, plus `initScroll()`. Panels use `.panel` / `.panel-head`
/ `.panel-title` ("Interactive · …"). Use `setInterval(…, 110)` or
`requestAnimationFrame` for animation. Use a seeded RNG if reproducibility
matters for what the prose says. Every `<svg>` gets `role="img"` and an
`aria-label`; every slider gets an `aria-label`.

A self-check that teaches is welcome (e.g. "predict, then reveal" inside an
interactive), but no generic multiple-choice quiz blocks.

# Before you finish
- Extract the `<script>` content and run `node --check` on it; fix any errors.
- Compression pass. Run `sh tools/prose-count.sh <your file>` and
  `sh tools/prose-count.sh RL.html`, and compare words per section. This is a
  diagnostic, not a cap: a chapter may legitimately need more. But if your
  sections run well above the reference's, go back through paragraph by
  paragraph and cut until each one reads like `RL.html`.
- Re-read the file top to bottom as a student would: is anything unclear,
  hand-wavy, or wrong? Fix it.
- Check every interactive control has a working handler and the layout holds
  at 640px wide.
- Confirm the shared conventions above are followed exactly.

Report back in a few lines: file name, section list, the visualisers you built,
prose word count vs. the reference, and any assumptions you made.
