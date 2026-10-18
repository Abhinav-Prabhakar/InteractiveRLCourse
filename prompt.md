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
and new to RL. Aim for the quality of the best textbook explanations: precise,
intuitive, and economical. The reference's voice is the target: clear,
connected explanatory prose that reads as one argument rather than a list of
facts. A few habits worth keeping:
- Motivate each object before defining it (what problem it solves, what goes
  wrong without it), then give the equation, then say in plain words what it
  means.
- Bold a technical term the first time it appears.
- Derive the important results rather than stating them. Walk through each
  step, say which assumption or rule it uses, and point at the load-bearing
  one ("the fourth line is where the Markov property is spent").
- Use concrete intuition and small examples: a limiting case (γ = 0 vs γ → 1),
  a two-number counterexample, a failure mode.
- Use `.note` callouts (bold lead-in) for the few ideas that matter most.
- Give each interactive a guided walkthrough: what to try, in what order, and
  what the reader should notice. Every number you quote must match what the
  page actually computes.
- Notation follows the reference: μ for stationary/state distributions so π
  always means a policy; `\mathbb{E}`, `\mid`, `\text{}` for state names.
- Never write "in this section we will", roadmaps, learning-objective boxes,
  or bulleted key-takeaway lists. The summary table and cheat sheet do that.
  Don't pad or hedge.
- Every number in prose that comes from a computation must come from the page's
  own code (check it by running the same model in node). Don't invent results.

This chapter can be longer and deeper than the reference — it is a full
chapter, not a note — but every paragraph should earn its place.

# Interactive visualisations
These are the heart of the chapter. Build 3–5 that each make one idea click,
including the one suggested in `index.md` (adapt it if a better design teaches
the same thing). Good visualisers:
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
- Re-read the file top to bottom as a student would: is anything unclear,
  hand-wavy, or wrong? Fix it.
- Check every interactive control has a working handler and the layout holds
  at 640px wide.
- Confirm the shared conventions above are followed exactly.

Report back in a few lines: file name, section list, the visualisers you built,
and any assumptions you made.
