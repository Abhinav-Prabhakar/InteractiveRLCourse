#!/usr/bin/env python3
"""Inject inter-chapter navigation (index brand link + prev/next pager) into
every chapter file under outputs/. Idempotent: re-running is a no-op."""
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "outputs")

CHAPTERS = [
    ("01-what-reinforcement-learning-really-is.html", "What RL Really Is"),
    ("02-multi-armed-bandits.html", "Multi-Armed Bandits"),
    ("03-markov-decision-processes.html", "Markov Decision Processes"),
    ("04-dynamic-programming.html", "Dynamic Programming"),
    ("05-monte-carlo-methods.html", "Monte Carlo Methods"),
    ("06-temporal-difference-learning.html", "Temporal-Difference Learning"),
    ("07-n-step-bootstrapping-and-eligibility-traces.html", "n-Step Bootstrapping"),
    ("08-planning-and-learning-with-tabular-methods.html", "Planning and Learning"),
    ("09-function-approximation.html", "Function Approximation"),
    ("10-deep-q-networks.html", "Deep Q-Networks"),
    ("11-policy-gradient-methods.html", "Policy Gradient Methods"),
    ("12-trust-region-and-proximal-policy-optimization.html", "TRPO & PPO"),
    ("13-model-based-reinforcement-learning.html", "Model-Based RL"),
    ("14-offline-reinforcement-learning.html", "Offline RL"),
    ("15-exploration-and-intrinsic-motivation.html", "Exploration & Curiosity"),
    ("16-hierarchical-reinforcement-learning.html", "Hierarchical RL"),
    ("17-multi-agent-reinforcement-learning.html", "Multi-Agent RL"),
    ("18-meta-reinforcement-learning-and-multi-task-rl.html", "Meta-RL & Multi-Task RL"),
    ("19-distributional-and-risk-sensitive-rl.html", "Distributional & Risk-Sensitive RL"),
    ("20-imitation-learning-and-inverse-rl.html", "Imitation & Inverse RL"),
    ("21-safe-and-constrained-rl.html", "Safe & Constrained RL"),
    ("22-rlhf-and-llm-alignment.html", "RLHF & LLM Alignment"),
]

MARKER = "<!-- inter-chapter-nav -->"

CSS = """/* ---------------- inter-chapter navigation ---------------- */
.brand{text-decoration:none}
.pager{max-width:720px;margin:64px auto 0;padding:0 24px;display:flex;gap:14px;align-items:stretch}
.pager a{flex:1 1 0;min-width:0;text-decoration:none;color:inherit;border:1px solid #ececec;border-radius:12px;padding:12px 16px;transition:border-color .12s,background .12s}
.pager a:hover{border-color:#dcdcdc;background:#fafafa}
.pager a.pg-home{flex:0 0 auto;text-align:center;display:flex;flex-direction:column;justify-content:center}
.pager a.pg-next{text-align:right}
.pager .pg-k{display:block;font-size:11px;font-weight:600;letter-spacing:.08em;text-transform:uppercase;color:#9ca3af}
.pager .pg-t{display:block;font-weight:600;font-size:14.5px;margin-top:3px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.pager a[aria-disabled="true"]{opacity:.35;pointer-events:none}
@media(max-width:640px){.pager{flex-wrap:wrap}.pager .pg-t{white-space:normal}.pager a.pg-home{order:3;width:100%}}
"""


def pager(i):
    prev = CHAPTERS[i - 1] if i > 0 else None
    nxt = CHAPTERS[i + 1] if i < len(CHAPTERS) - 1 else None

    def link(cls, label, target):
        if target is None:
            return ('<a class="%s" aria-disabled="true">'
                    '<span class="pg-k">%s</span></a>' % (cls, label))
        return ('<a class="%s" href="%s"><span class="pg-k">%s</span>'
                '<span class="pg-t">%s</span></a>' % (cls, target[0], label, target[1]))

    return (MARKER + "\n"
            '<nav class="pager" aria-label="Chapter navigation">'
            + link("pg-prev", "Previous", prev)
            + '<a class="pg-home" href="../index.html"><span class="pg-k">Contents</span></a>'
            + link("pg-next", "Next", nxt)
            + "</nav>")


def main():
    changed = 0
    for i, (fn, _title) in enumerate(CHAPTERS):
        path = os.path.join(OUT, fn)
        with open(path, encoding="utf-8") as f:
            s = f.read()
        if MARKER in s:
            print("skip (already injected):", fn)
            continue
        # brand -> link to index
        s = re.sub(r'<span class="brand">(.*?)</span>',
                   r'<a class="brand" href="../index.html">\1</a>', s, count=1)
        # nav CSS before the closing style tag
        s = s.replace("</style>", CSS + "\n</style>", 1)
        # pager before the footer
        s = s.replace("<footer>", pager(i) + "\n<footer>", 1)
        with open(path, "w", encoding="utf-8") as f:
            f.write(s)
        changed += 1
        print("updated:", fn)
    print("done; %d file(s) updated" % changed)


if __name__ == "__main__":
    main()
