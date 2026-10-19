#!/usr/bin/env python3
"""Make chapter chrome consistent across outputs/: <title>, topbar brand,
hero eyebrow, and a small reader script (arrow-key prev/next, remembers
visited chapters for the contents page). Idempotent."""
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "outputs")

# (file, full title, short title, part)
CHAPTERS = [
    ("01-what-reinforcement-learning-really-is.html", "What Reinforcement Learning Really Is", "What RL Really Is", "I"),
    ("02-multi-armed-bandits.html", "Multi-Armed Bandits", "Bandits", "I"),
    ("03-markov-decision-processes.html", "Markov Decision Processes", "MDPs", "I"),
    ("04-dynamic-programming.html", "Dynamic Programming", "Dynamic Programming", "II"),
    ("05-monte-carlo-methods.html", "Monte Carlo Methods", "Monte Carlo", "II"),
    ("06-temporal-difference-learning.html", "Temporal-Difference Learning", "TD Learning", "II"),
    ("07-n-step-bootstrapping-and-eligibility-traces.html", "n-Step Bootstrapping & Eligibility Traces", "n-Step & Traces", "II"),
    ("08-planning-and-learning-with-tabular-methods.html", "Planning & Learning with Tabular Methods", "Planning & Learning", "II"),
    ("09-function-approximation.html", "Function Approximation", "Function Approximation", "III"),
    ("10-deep-q-networks.html", "Deep Q-Networks & Value-Based Deep RL", "Deep Q-Networks", "III"),
    ("11-policy-gradient-methods.html", "Policy Gradient Methods", "Policy Gradients", "III"),
    ("12-trust-region-and-proximal-policy-optimization.html", "Trust-Region & Proximal Policy Optimization", "TRPO & PPO", "III"),
    ("13-model-based-reinforcement-learning.html", "Model-Based Reinforcement Learning", "Model-Based RL", "IV"),
    ("14-offline-reinforcement-learning.html", "Offline Reinforcement Learning", "Offline RL", "IV"),
    ("15-exploration-and-intrinsic-motivation.html", "Exploration & Intrinsic Motivation", "Exploration", "IV"),
    ("16-hierarchical-reinforcement-learning.html", "Hierarchical Reinforcement Learning", "Hierarchical RL", "IV"),
    ("17-multi-agent-reinforcement-learning.html", "Multi-Agent Reinforcement Learning", "Multi-Agent RL", "IV"),
    ("18-meta-reinforcement-learning-and-multi-task-rl.html", "Meta-RL & Multi-Task RL", "Meta-RL", "IV"),
    ("19-distributional-and-risk-sensitive-rl.html", "Distributional & Risk-Sensitive RL", "Distributional RL", "IV"),
    ("20-imitation-learning-and-inverse-rl.html", "Imitation Learning & Inverse RL", "Imitation & IRL", "IV"),
    ("21-safe-and-constrained-rl.html", "Safe & Constrained RL", "Safe RL", "IV"),
    ("22-rlhf-and-llm-alignment.html", "RLHF & LLM Alignment", "RLHF & Alignment", "IV"),
]

READER_MARK = "<!-- reader-script -->"
READER = READER_MARK + """
<script>
(function () {
  var file = location.pathname.split('/').pop();
  try { localStorage.setItem('rl-last', file); } catch (e) {}
  document.addEventListener('keydown', function (e) {
    if (e.altKey || e.ctrlKey || e.metaKey || e.shiftKey) return;
    var t = e.target;
    if (t && (t.tagName === 'INPUT' || t.tagName === 'TEXTAREA' || t.tagName === 'SELECT' || t.isContentEditable)) return;
    var a = e.key === 'ArrowLeft' ? document.querySelector('.pager .pg-prev[href]')
          : e.key === 'ArrowRight' ? document.querySelector('.pager .pg-next[href]') : null;
    if (a) location.href = a.getAttribute('href');
  });
})();
</script>
"""


def esc(s):
    return s.replace("&", "&amp;")


def main():
    for i, (fn, full, short, part) in enumerate(CHAPTERS):
        n = i + 1
        path = os.path.join(OUT, fn)
        s = open(path, encoding="utf-8").read()
        s = re.sub(r"<title>.*?</title>", "<title>Chapter %d · %s</title>" % (n, esc(full)), s, count=1)
        s = re.sub(r'(<a class="brand" href="\.\./index\.html">).*?(</a>)',
                   lambda m: m.group(1) + "Ch. %02d · %s" % (n, esc(short)) + m.group(2), s, count=1)
        s = re.sub(r'<p class="eyebrow">.*?</p>',
                   '<p class="eyebrow">Reinforcement Learning · Part %s · Chapter %d</p>' % (part, n), s, count=1)
        if READER_MARK not in s:
            s = s.replace("</body>", READER + "</body>", 1)
        open(path, "w", encoding="utf-8").write(s)
        print("ok", fn)


if __name__ == "__main__":
    main()
