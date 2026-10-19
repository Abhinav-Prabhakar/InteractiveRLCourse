#!/usr/bin/env python3
"""Normalize project chrome under projects/: <title>, topbar brand, hero
eyebrow, a Previous/Next pager, and the arrow-key reader script. Idempotent."""
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJ = os.path.join(ROOT, "projects")

# (file, full title, short title)
PROJECTS = [
    ("01-tabular-rl-from-scratch.html", "Tabular RL from Scratch", "Tabular RL"),
    ("02-deep-rl-continuous-control.html", "Deep RL on a Continuous-Control Task", "Continuous Control"),
    ("03-offline-rl-benchmark.html", "Offline RL Benchmark", "Offline RL"),
    ("04-model-based-world-model.html", "Model-Based World Model", "World Model"),
    ("05-rlhf-dpo-alignment-pipeline.html", "RLHF / DPO Alignment Pipeline", "RLHF / DPO"),
    ("06-multi-agent-coordination.html", "Multi-Agent Coordination", "Multi-Agent"),
]

PAGER_MARK = "<!-- project-pager -->"
READER_MARK = "<!-- reader-script -->"

PAGER_CSS = """/* ---------------- inter-chapter navigation ---------------- */
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

READER = READER_MARK + """
<script>
(function () {
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


def pager(i):
    prev = PROJECTS[i - 1] if i > 0 else None
    nxt = PROJECTS[i + 1] if i < len(PROJECTS) - 1 else None

    def link(cls, label, target):
        if target is None:
            return ('<a class="%s" aria-disabled="true">'
                    '<span class="pg-k">%s</span></a>' % (cls, label))
        return ('<a class="%s" href="%s"><span class="pg-k">%s</span>'
                '<span class="pg-t">%s</span></a>' % (cls, target[0], label, target[1]))

    return (PAGER_MARK + "\n"
            '<nav class="pager" aria-label="Project navigation">'
            + link("pg-prev", "Previous", prev)
            + '<a class="pg-home" href="../index.html"><span class="pg-k">Contents</span></a>'
            + link("pg-next", "Next", nxt)
            + "</nav>")


def esc(s):
    return s.replace("&", "&amp;")


def main():
    for i, (fn, full, short) in enumerate(PROJECTS):
        n = i + 1
        path = os.path.join(PROJ, fn)
        if not os.path.exists(path):
            print("MISSING", fn)
            continue
        s = open(path, encoding="utf-8").read()

        s = re.sub(r"<title>.*?</title>", "<title>Project %d · %s</title>" % (n, esc(full)), s, count=1)
        s = re.sub(r'<(?:a|span)[^>]*class="brand"[^>]*>.*?</(?:a|span)>',
                   '<a class="brand" href="../index.html">P%02d · %s</a>' % (n, esc(short)), s, count=1)
        s = re.sub(r'<p class="eyebrow">.*?</p>',
                   '<p class="eyebrow">Reinforcement Learning · Projects · Project %d</p>' % n, s, count=1)

        if ".pager{" not in s and "</style>" in s:
            s = s.replace("</style>", PAGER_CSS + "\n</style>", 1)
        if PAGER_MARK not in s and "<footer" in s:
            s = re.sub(r"<footer>", pager(i) + "\n<footer>", s, count=1)
        if READER_MARK not in s and "</body>" in s:
            s = s.replace("</body>", READER + "</body>", 1)

        open(path, "w", encoding="utf-8").write(s)
        print("ok", fn)


if __name__ == "__main__":
    main()
