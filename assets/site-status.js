/* ============================================================
   SITE AVAILABILITY
   The single place to mark a page as live. Add the chapter or
   project number to the matching array, save, commit, and push.
   Everything not listed here is greyed out in the contents and
   cannot be reached through previous/next or a direct URL.
   ============================================================ */
window.RL_AVAILABILITY = {
  chapters: [1, 2],
  projects: []
};

(function () {
  var cfg = window.RL_AVAILABILITY;
  var isLive = function (kind, n) {
    return (cfg[kind] || []).indexOf(n) !== -1;
  };

  function pageNumber(url) {
    var file = url.pathname.split('/').pop() || '';
    var m = file.match(/^(\d+)-/);
    return m ? parseInt(m[1], 10) : null;
  }

  function kindFor(url) {
    return /\/projects\//.test(url.pathname) ? 'projects' : 'chapters';
  }

  var here = new URL(location.href);
  var hereNum = pageNumber(here);
  var hereKind = kindFor(here);
  var pageIsLive = hereNum === null || isLive(hereKind, hereNum);

  window.RLSite = {
    isLive: isLive,
    pageNumber: pageNumber
  };

  if (!pageIsLive) document.documentElement.classList.add('rl-page-locked');

  function injectStyle() {
    if (document.getElementById('rl-status-style')) return;
    var style = document.createElement('style');
    style.id = 'rl-status-style';
    style.textContent = [
      'html.rl-page-locked body{visibility:hidden}',
      '#rl-lock{visibility:visible;position:fixed;inset:0;z-index:2147483647;display:flex;align-items:center;justify-content:center;background:#fff;padding:24px;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Inter,Roboto,Helvetica,Arial,sans-serif;color:#111}',
      '#rl-lock .rl-lock-card{max-width:440px;text-align:center}',
      '#rl-lock .rl-lock-eyebrow{font-size:12px;font-weight:600;letter-spacing:.14em;text-transform:uppercase;color:#9ca3af;margin:0 0 16px}',
      '#rl-lock h1{font-size:28px;line-height:1.2;letter-spacing:-.022em;margin:0 0 12px}',
      '#rl-lock p{font-size:16px;line-height:1.6;color:#6b7280;margin:0 0 24px}',
      '#rl-lock a{display:inline-block;background:#111;color:#fff;text-decoration:none;font-size:14px;font-weight:600;border-radius:9px;padding:11px 18px}',
      '#rl-lock a:hover{background:#333}',
      '.pager a.pg-locked{cursor:not-allowed;opacity:.35;pointer-events:none}',
      '.pager .pg-soon{display:block;font-size:10.5px;font-weight:700;letter-spacing:.07em;text-transform:uppercase;color:#9ca3af;margin-top:4px}'
    ].join('\n');
    document.head.appendChild(style);
  }

  function lockPager() {
    var anchors = document.querySelectorAll('.pager .pg-prev[href], .pager .pg-next[href]');
    Array.prototype.forEach.call(anchors, function (a) {
      var target = new URL(a.getAttribute('href'), location.href);
      var n = pageNumber(target);
      if (n === null || isLive(kindFor(target), n)) return;
      a.removeAttribute('href');
      a.setAttribute('aria-disabled', 'true');
      a.setAttribute('title', 'Not available yet');
      a.classList.add('pg-locked');
      var tag = document.createElement('span');
      tag.className = 'pg-soon';
      tag.textContent = 'Coming soon';
      a.appendChild(tag);
    });
  }

  function guardPage() {
    if (pageIsLive || document.getElementById('rl-lock')) return;
    var isProject = hereKind === 'projects';
    var lock = document.createElement('div');
    lock.id = 'rl-lock';
    lock.setAttribute('role', 'dialog');
    lock.setAttribute('aria-modal', 'true');
    lock.innerHTML =
      '<div class="rl-lock-card">' +
        '<p class="rl-lock-eyebrow">Reinforcement Learning</p>' +
        '<h1>This ' + (isProject ? 'project' : 'chapter') + ' is not available yet.</h1>' +
        '<p>The course is being published one page at a time. The contents lists everything that is live so far.</p>' +
        '<a href="../index.html">Back to contents</a>' +
      '</div>';
    document.body.appendChild(lock);
  }

  function init() {
    injectStyle();
    lockPager();
    guardPage();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
