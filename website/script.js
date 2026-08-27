/* ==========================================================================
   CD BOULANGERIE — script.js
   Tout le JavaScript du site, en un seul fichier.

   SOMMAIRE
     PARTIE 1 — Curseur farine (nuage qui suit la souris, explose au clic)
     PARTIE 2 — Loader, animations, menu, galerie, transitions de page

   Aucune librairie externe. Le site reste lisible si ce fichier ne se
   charge pas : les animations sont simplement absentes.
   ========================================================================== */

/* ==========================================================================
   PARTIE 1 — Curseur farine
   ========================================================================== */

/* ==========================================================================
   CD BOULANGERIE — flour.js
   Flour-dust cursor. Particles puff from the pointer as it moves and burst
   on click, like flour lifting off a worktop.

   - Canvas is created in JS (no markup needed), fixed & pointer-events:none
   - Object pool, capped particle count, RAF pauses when idle
   - Disabled on touch devices and when prefers-reduced-motion is set
   - Public API: window.CDFlour.burst(x, y, count) / .pause() / .resume()
   ========================================================================== */
(() => {
  'use strict';

  /* Préférence de mouvement -------------------------------------------------
     « Réduire les animations » est un réglage système très répandu (Windows,
     macOS, iOS) et il suit l'utilisateur dans TOUS ses navigateurs. Couper
     l'effet entièrement donnait l'impression d'un site cassé.
     On garde donc une version calme : moins de grains, plus lents.
     Désactivation réelle uniquement si l'utilisateur le demande :
       ?flour=0  /  ?flour=1        dans l'URL
       localStorage 'cd_flour' = '0' | '1'
  --------------------------------------------------------------------------*/
  let forced = null;
  try {
    const q = new URLSearchParams(location.search).get('flour');
    if (q === '0' || q === '1') forced = q;
    if (forced === null) {
      const ls = localStorage.getItem('cd_flour');
      if (ls === '0' || ls === '1') forced = ls;
    }
  } catch (e) {}

  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const fine    = window.matchMedia('(pointer: fine)').matches;

  // Pas de souris (tactile) => rien à suivre. Refus explicite => off.
  if (forced === '0' || (!fine && forced !== '1')) {
    window.CDFlour = { burst() {}, pause() {}, resume() {} };
    return;
  }

  // Mode calme : toujours visible, simplement plus doux.
  const CALM = reduced && forced !== '1';

  /* ---- config ---------------------------------------------------------- */
  const MAX      = 520;    // hard cap on live particles
  const GRAVITY  = 0.016;  // flour is light — barely falls
  const FRICTION = 0.955;
  const DRIFT    = 0.010;  // sideways wobble

  // Two palettes. Pale flour reads on the dark sections; on the cream
  // background we need warmer, deeper tans or the dust is invisible.
  const TONES_LIGHT_BG = [   // over cream — warm, visible
    [186, 168, 138],
    [166, 146, 114],
    [205, 190, 163],
    [146, 128, 100],
    [214, 201, 178],
  ];
  const TONES_DARK_BG = [    // over ink sections — pale flour
    [255, 253, 248],
    [246, 241, 231],
    [230, 220, 200],
    [212, 199, 175],
    [255, 255, 252],
  ];
  let TONES = TONES_LIGHT_BG;
  let onDark = false;

  /* Is the pointer over a dark-background section? */
  const darkSel = '.section--ink, .footer, .loader, .curtain, .menu, .lb, .marquee--ink, .upnext:hover';
  const checkDark = (el) => {
    if (!el || !el.closest) return false;
    return !!el.closest(darkSel);
  };

  /* ---- canvas ---------------------------------------------------------- */
  const cv  = document.createElement('canvas');
  cv.className = 'flour-canvas';
  cv.setAttribute('aria-hidden', 'true');
  const ctx = cv.getContext('2d', { alpha: true });

  let dpr = 1, W = 0, H = 0;

  const resize = () => {
    dpr = Math.min(window.devicePixelRatio || 1, 2);
    W = window.innerWidth;
    H = window.innerHeight;
    cv.width  = Math.floor(W * dpr);
    cv.height = Math.floor(H * dpr);
    cv.style.width  = W + 'px';
    cv.style.height = H + 'px';
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  };

  const mount = () => {
    if (!document.body.contains(cv)) document.body.appendChild(cv);
    resize();
  };

  /* ---- particle pool --------------------------------------------------- */
  const pool = new Array(MAX);
  for (let i = 0; i < MAX; i++) {
    pool[i] = { on: false, x: 0, y: 0, vx: 0, vy: 0, r: 0, life: 0, max: 1, tone: 0, seed: 0, spin: 0 };
  }
  let cursor = 0;
  let live = 0;

  const spawn = (x, y, vx, vy, r, life, tone) => {
    const p = pool[cursor];
    cursor = (cursor + 1) % MAX;
    if (!p.on) live++;
    p.on = true;
    p.x = x; p.y = y;
    p.vx = vx; p.vy = vy;
    p.r = r;
    p.life = 0;
    p.max = life;
    p.tone = tone !== undefined ? tone : (Math.random() * TONES.length) | 0;
    p.dark = onDark; // remember which palette this grain belongs to
    p.seed = Math.random() * Math.PI * 2;
    p.spin = (Math.random() - 0.5) * 0.06;
  };

  /* ---- emitters -------------------------------------------------------- */

  // Trail: density scales with pointer speed, so a slow drift barely dusts
  // and a fast sweep throws a proper cloud.
  const trail = (x, y, speed) => {
    const n = CALM
      ? Math.min(2, Math.round(speed / 16))     // calme : fine poussière
      : Math.min(7, Math.round(speed / 5.5));
    for (let i = 0; i < n; i++) {
      const a = Math.random() * Math.PI * 2;
      const s = Math.random() * 0.7;
      spawn(
        x + (Math.random() - 0.5) * 13,
        y + (Math.random() - 0.5) * 13,
        Math.cos(a) * s,
        Math.sin(a) * s - Math.random() * 0.35,
        Math.random() * 2.6 + 0.8,
        Math.random() * 900 + 700
      );
    }
  };

  // Click / hover burst: a radial puff
  const burst = (x, y, count = 26, power = 1) => {
    if (CALM) { count = Math.round(count * 0.4); power *= 0.6; }
    for (let i = 0; i < count; i++) {
      const a = (Math.PI * 2 * i) / count + Math.random() * 0.5;
      const s = (Math.random() * 2.6 + 0.9) * power;
      spawn(
        x + (Math.random() - 0.5) * 8,
        y + (Math.random() - 0.5) * 8,
        Math.cos(a) * s,
        Math.sin(a) * s - Math.random() * 0.7,
        Math.random() * 3.2 + 0.9,
        Math.random() * 1000 + 800
      );
    }
  };

  /* ---- loop ------------------------------------------------------------ */
  let raf = null;
  let last = performance.now();
  let paused = false;

  const frame = (now) => {
    const dt = Math.min(now - last, 48);
    last = now;

    ctx.clearRect(0, 0, W, H);

    if (live > 0 && !paused) {
      for (let i = 0; i < MAX; i++) {
        const p = pool[i];
        if (!p.on) continue;

        p.life += dt;
        if (p.life >= p.max) { p.on = false; live--; continue; }

        const t = p.life / p.max;

        p.seed += p.spin;
        p.vx = p.vx * FRICTION + Math.sin(p.seed) * DRIFT;
        p.vy = p.vy * FRICTION + GRAVITY;
        p.x += p.vx * (dt / 16.67);
        p.y += p.vy * (dt / 16.67);

        // fade in fast, out slow
        const alpha = t < 0.12 ? t / 0.12 : 1 - (t - 0.12) / 0.88;
        if (alpha <= 0) continue;

        const pal = p.dark ? TONES_DARK_BG : TONES_LIGHT_BG;
        const [r, g, b] = pal[p.tone % pal.length];
        const rad = p.r * (1 - t * 0.35);

        // soft halo + denser core = cheap "dust" look without shadowBlur
        ctx.globalAlpha = alpha * 0.30;
        ctx.fillStyle = `rgb(${r},${g},${b})`;
        ctx.beginPath();
        ctx.arc(p.x, p.y, rad * 2.4, 0, 6.283);
        ctx.fill();

        ctx.globalAlpha = alpha * 0.95;
        ctx.beginPath();
        ctx.arc(p.x, p.y, rad, 0, 6.283);
        ctx.fill();
      }
      ctx.globalAlpha = 1;
    }

    if (live > 0) {
      raf = requestAnimationFrame(frame);
    } else {
      raf = null; // sleep until the next emit
    }
  };

  const wake = () => {
    if (raf === null) { last = performance.now(); raf = requestAnimationFrame(frame); }
  };

  /* ---- pointer --------------------------------------------------------- */
  let px = 0, py = 0, has = false;

  const onMove = (e) => {
    if (paused) return;
    const x = e.clientX, y = e.clientY;
    if (!has) { px = x; py = y; has = true; return; }

    const dx = x - px, dy = y - py;
    const speed = Math.hypot(dx, dy);
    px = x; py = y;

    if (speed < 1.2) return;

    onDark = checkDark(e.target);
    trail(x, y, speed);
    wake();
  };

  const onDown = (e) => {
    if (paused) return;
    onDark = checkDark(e.target);
    burst(e.clientX, e.clientY, 34, 1.2);
    wake();
  };

  /* ---- wire up --------------------------------------------------------- */
  const start = () => {
    mount();
    window.addEventListener('resize', resize, { passive: true });
    window.addEventListener('pointermove', onMove, { passive: true });
    window.addEventListener('pointerdown', onDown, { passive: true });
    document.addEventListener('visibilitychange', () => {
      paused = document.hidden;
      if (!paused) wake();
    });
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', start);
  } else {
    start();
  }

  /* ---- public API ------------------------------------------------------ */
  window.CDFlour = {
    burst(x, y, count, power) { if (!paused) { burst(x, y, count, power); wake(); } },
    pause() { paused = true; },
    resume() { paused = false; wake(); },
  };
})();


/* ==========================================================================
   PARTIE 2 — Loader, animations, menu, galerie, transitions
   ========================================================================== */

/* ==========================================================================
   CD BOULANGERIE — main.js
   Zero dependencies. Progressive enhancement: everything works without JS,
   this layer only adds motion and interaction polish.
   ========================================================================== */
(() => {
  'use strict';

  const $  = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => Array.from(r.querySelectorAll(s));
  /* Préférence de mouvement du système.
     On distingue deux niveaux :
       SOFT  = l'utilisateur veut moins de mouvement -> on garde des
               apparitions douces (fondu), on retire parallaxe/rideau.
       RM    = refus total, uniquement si demandé explicitement
               (?motion=0 ou localStorage cd_motion='0').
     Avant, « réduire les animations » coupait absolument tout : le site
     semblait figé et cassé. */
  let motionForced = null;
  try {
    const q = new URLSearchParams(location.search).get('motion');
    if (q === '0' || q === '1') motionForced = q;
    if (motionForced === null) {
      const ls = localStorage.getItem('cd_motion');
      if (ls === '0' || ls === '1') motionForced = ls;
    }
  } catch (e) {}

  const SYS_REDUCED = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const SOFT = (SYS_REDUCED && motionForced !== '1') || motionForced === '0';
  const RM = motionForced === '0';   // coupure totale : sur demande seulement
  if (RM) document.documentElement.classList.add('no-motion');

  /* ---------------------------------------------------------------------
     1. LOADER — first visit only, session-scoped
  --------------------------------------------------------------------- */
  const initLoader = () => {
    // The loader lives in an inert <template>; we only inject it once we know
    // JavaScript is running. No JS -> no loader -> the site is simply visible.
    const tpl = $('#loaderTpl');
    if (!tpl || !tpl.content) return;

    /* Quand l'écran de chargement se joue-t-il ?

       Il s'affiche à l'ARRIVÉE sur le site, puis se tait pendant toute la
       navigation interne (personne n'a envie de le revoir à chaque clic).
       Si le visiteur revient plus tard — nouvel onglet, ou après quelques
       minutes d'absence — il se rejoue : c'est une vitrine, elle doit
       accueillir. Avant, il ne se montrait qu'une seule fois par session,
       ce qui donnait l'impression qu'il avait disparu.

         ?intro=1  -> force l'affichage (démonstration client)
         ?intro=0  -> le saute
         LOADER_ALWAYS = true -> à chaque chargement de page              */
    const LOADER_ALWAYS = false;
    const REPLAY_AFTER = 30 * 60 * 1000;   // 30 minutes

    // sessionStorage throws in sandboxed iframes / strict privacy modes.
    // Never let that kill the loader — fall back to "not seen".
    const store = {
      get(k) { try { return sessionStorage.getItem(k); } catch (e) { return null; } },
      set(k, v) { try { sessionStorage.setItem(k, v); } catch (e) {} },
    };

    let q = null;
    try { q = new URLSearchParams(location.search).get('intro'); } catch (e) {}

    /* "Déjà vu" = l'intro a été jouée il y a moins de REPLAY_AFTER.
       On s'appuie uniquement sur l'horodatage : le referrer n'est pas
       fiable (vide en file://, masqué par certaines politiques). Toute
       navigation interne tombe forcément dans la fenêtre des 30 minutes,
       donc l'intro ne se rejoue pas ; un visiteur qui revient plus tard,
       lui, la revoit. */
    const last = parseInt(store.get('cd_seen_at') || '0', 10);
    let seen = !!last && (Date.now() - last) < REPLAY_AFTER;
    if (q === '1') seen = false;                 // force
    if (q === '0') seen = true;                  // saute
    if (LOADER_ALWAYS && q !== '0') seen = false;

    if (seen || RM) {
      // Never inject it at all — nothing to hide, nothing to unlock.
      store.set('cd_seen_at', String(Date.now()));
      document.body.classList.remove('is-locked');
      startEntrance();
      return;
    }

    // JS is alive and the intro should play: only now do we build the loader.
    document.body.insertBefore(tpl.content.cloneNode(true), document.body.firstChild);
    const el = $('#loader');
    if (!el) { startEntrance(); return; }

    document.body.classList.add('is-locked');

    /* Failsafe: whatever happens, never leave the page locked. */
    const failsafe = setTimeout(() => {
      el.classList.add('is-done');
      document.body.classList.remove('is-locked');
      store.set('cd_seen_at', String(Date.now()));
      startEntrance();
      setTimeout(() => el.remove(), 1000);
    }, 7000);

    const fill = $('#loaderFill');
    const pct  = $('#loaderPct');
    const step = $('#loaderStep');
    const ring = $('#loaderRing');
    // Circonférence de l'anneau : 2 × π × r, avec r = 46 dans le SVG.
    // On réduit le pointillé au fur et à mesure : le cercle se referme.
    const RING_LEN = 2 * Math.PI * 46;
    if (ring) {
      ring.style.strokeDasharray = RING_LEN.toFixed(1);
      ring.style.strokeDashoffset = RING_LEN.toFixed(1);
    }

    // Étapes du fournil — traduites, lues depuis data-steps (FR/EN/PL)
    const LABELS = (step && step.dataset.steps)
      ? step.dataset.steps.split(' · ')
      : ['Pétrissage', 'Pointage', 'Façonnage', 'Enfournement', 'Sortie du four'];
    const MARKS = [0, 28, 52, 74, 92];
    const STEPS = MARKS.map((m, i) => [m, LABELS[i] || LABELS[LABELS.length - 1]]);

    let v = 0;

    const tick = () => {
      /* Progression par paliers : la barre avance vite, marque un temps
         d'arrêt à chaque étape du fournil, puis repart. C'est ce rythme
         irrégulier qui donne l'impression que quelque chose travaille,
         plutôt qu'une barre qui glisse mécaniquement. */
      const nextMark = MARKS.find((m) => m > v);
      const ceiling = nextMark !== undefined ? nextMark : 100;
      const gap = ceiling - v;

      v += Math.max(0.6, gap * 0.18) + Math.random() * 1.4;
      if (v > ceiling) v = ceiling;
      if (v >= 99.4) v = 100;

      if (fill) fill.style.width = v + '%';
      if (ring) ring.style.strokeDashoffset = (RING_LEN * (1 - v / 100)).toFixed(1);
      if (pct)  pct.textContent  = String(Math.floor(v)).padStart(3, '0');
      if (step) {
        const s = STEPS.filter((x) => v >= x[0]).pop();
        if (s && step.textContent !== s[1]) {
          step.textContent = s[1];
          // relance l'animation de bascule
          step.classList.remove('is-swap');
          void step.offsetWidth;
          step.classList.add('is-swap');
          // une bouffée de farine à chaque étape franchie
          if (window.CDFlour) {
            const r = step.getBoundingClientRect();
            window.CDFlour.burst(r.left + r.width / 2, r.top, 14, 0.7);
          }
        }
      }

      if (v < 100) {
        // pause plus longue quand on atteint un palier
        const atMark = MARKS.includes(Math.round(v));
        setTimeout(tick, atMark ? 210 + Math.random() * 130 : 45 + Math.random() * 55);
      } else {
        setTimeout(() => {
          clearTimeout(failsafe);
          el.classList.add('is-done');
          document.body.classList.remove('is-locked');
          store.set('cd_seen_at', String(Date.now()));
          startEntrance();

          // puff of flour as the panels part
          if (window.CDFlour) {
            const cx = window.innerWidth / 2, cy = window.innerHeight / 2;
            for (let i = 0; i < 5; i++) {
              setTimeout(() => window.CDFlour.burst(
                cx + (Math.random() - 0.5) * window.innerWidth * 0.55,
                cy + (Math.random() - 0.5) * 90, 22, 1.5
              ), i * 65);
            }
          }
          setTimeout(() => el.remove(), 1100);   // > 0.95s d'ouverture
        }, 340);
      }
    };
    setTimeout(tick, 240);
  };

  /* Hero entrance once loader is gone */
  function startEntrance() {
    $$('[data-entrance]').forEach((el, i) => {
      setTimeout(() => el.classList.add('is-in', 'split-in'), 90 * i);
    });
  }

  /* ---------------------------------------------------------------------
     2. SPLIT TEXT — wrap words in masks for the reveal
  --------------------------------------------------------------------- */
  const initSplit = () => {
    $$('[data-split]').forEach((el) => {
      if (el.dataset.splitDone) return;
      const stagger = parseInt(el.dataset.split, 10) || 55;
      let i = 0;

      const walk = (node) => {
        const kids = Array.from(node.childNodes);
        kids.forEach((n) => {
          if (n.nodeType === 3) {
            const txt = n.textContent;
            if (!txt.trim()) return;
            const frag = document.createDocumentFragment();
            txt.split(/(\s+)/).forEach((chunk) => {
              if (!chunk) return;
              if (/^\s+$/.test(chunk)) { frag.appendChild(document.createTextNode(chunk)); return; }
              const w = document.createElement('span');
              w.className = 'word';
              const inner = document.createElement('span');
              inner.className = 'word__i';
              inner.style.setProperty('--wd', (i++ * stagger) + 'ms');
              inner.textContent = chunk;
              w.appendChild(inner);
              frag.appendChild(w);
            });
            node.replaceChild(frag, n);
          } else if (n.nodeType === 1 && !n.classList.contains('word')) {
            walk(n);
          }
        });
      };

      walk(el);
      el.dataset.splitDone = '1';
    });
  };

  /* ---------------------------------------------------------------------
     3. REVEAL ON SCROLL
  --------------------------------------------------------------------- */
  const initReveal = () => {
    const items = $$('[data-reveal], .rule, .mask, [data-split]')
      .filter((el) => !el.hasAttribute('data-entrance'));

    if (RM || !('IntersectionObserver' in window)) {
      items.forEach((el) => el.classList.add('is-in', 'split-in'));
      return;
    }

    const io = new IntersectionObserver((entries) => {
      entries.forEach((e) => {
        if (!e.isIntersecting) return;
        e.target.classList.add('is-in', 'split-in');
        io.unobserve(e.target);
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -8% 0px' });

    items.forEach((el) => io.observe(el));

    /* Stagger children of a group */
    $$('[data-stagger]').forEach((group) => {
      const step = parseInt(group.dataset.stagger, 10) || 90;
      Array.from(group.children).forEach((child, i) => {
        const t = child.matches('[data-reveal]') ? child : $('[data-reveal]', child);
        if (t) t.style.setProperty('--rd', (i * step) + 'ms');
      });
    });
  };

  /* ---------------------------------------------------------------------
     4. HEADER — sticky, auto-hide on scroll down
  --------------------------------------------------------------------- */
  const initHeader = () => {
    const h = $('#header');
    if (!h) return;
    let last = window.scrollY;
    let ticking = false;

    const update = () => {
      const y = window.scrollY;
      h.classList.toggle('is-stuck', y > 40);
      if (!document.body.classList.contains('is-menu-open')) {
        h.classList.toggle('is-hidden', y > last && y > 340);
      }
      last = y;
      ticking = false;
    };

    window.addEventListener('scroll', () => {
      if (!ticking) { requestAnimationFrame(update); ticking = true; }
    }, { passive: true });
    update();
  };

  /* ---------------------------------------------------------------------
     5. SCROLL PROGRESS
  --------------------------------------------------------------------- */
  const initProgress = () => {
    const bar = $('#prog');
    if (!bar) return;
    let ticking = false;
    const run = () => {
      const max = document.documentElement.scrollHeight - window.innerHeight;
      bar.style.transform = `scaleX(${max > 0 ? window.scrollY / max : 0})`;
      ticking = false;
    };
    window.addEventListener('scroll', () => {
      if (!ticking) { requestAnimationFrame(run); ticking = true; }
    }, { passive: true });
    run();
  };

  /* ---------------------------------------------------------------------
     6. MOBILE MENU
  --------------------------------------------------------------------- */
  const initMenu = () => {
    const burger = $('#burger');
    const menu = $('#menu');
    if (!burger || !menu) return;

    const links = $$('.menu__link', menu);
    links.forEach((l, i) => l.style.transitionDelay = (0.14 + i * 0.07) + 's');

    /* Le menu fermé doit sortir COMPLÈTEMENT de l'ordre de tabulation.
       Sinon l'utilisateur au clavier tabule dans des liens invisibles.
       `inert` fait cela nativement ; tabindex=-1 sert de repli. */
    const focusables = () => $$('a, button, input, textarea, select', menu);

    const setInert = (off) => {
      if ('inert' in HTMLElement.prototype) {
        menu.inert = off;
      } else {
        focusables().forEach((el) => {
          if (off) {
            if (!el.hasAttribute('data-ti')) el.setAttribute('data-ti', el.getAttribute('tabindex') || '');
            el.setAttribute('tabindex', '-1');
          } else {
            const prev = el.getAttribute('data-ti');
            if (prev) el.setAttribute('tabindex', prev); else el.removeAttribute('tabindex');
            el.removeAttribute('data-ti');
          }
        });
      }
    };

    const setOpen = (on) => {
      document.body.classList.toggle('is-menu-open', on);
      document.body.classList.toggle('is-locked', on);
      menu.classList.toggle('is-open', on);
      burger.setAttribute('aria-expanded', String(on));
      menu.setAttribute('aria-hidden', String(!on));
      setInert(!on);
      if (on) {
        $('#header')?.classList.remove('is-hidden');
        // le focus entre dans le menu
        setTimeout(() => focusables()[0]?.focus(), 320);
      } else {
        burger.focus();
      }
    };

    setInert(true);   // état initial : menu fermé

    /* Piège de focus : Tab boucle à l'intérieur du menu ouvert. */
    menu.addEventListener('keydown', (e) => {
      if (e.key !== 'Tab' || !menu.classList.contains('is-open')) return;
      const f = focusables().filter((el) => el.offsetParent !== null);
      if (!f.length) return;
      const first = f[0], last = f[f.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    });

    burger.addEventListener('click', () => setOpen(!menu.classList.contains('is-open')));
    links.forEach((l) => l.addEventListener('click', () => setOpen(false)));
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && menu.classList.contains('is-open')) setOpen(false);
    });
    window.addEventListener('resize', () => {
      if (window.innerWidth > 1024 && menu.classList.contains('is-open')) setOpen(false);
    });
  };

  /* ---------------------------------------------------------------------
     7. PAGE TRANSITIONS — curtain wipe between pages
  --------------------------------------------------------------------- */
  /* Noms des pages pour le rideau de transition.
     Lus depuis le menu de la page : donc déjà dans la bonne langue. */
  const PAGE_NAMES = (() => {
    const map = {};
    $$('.menu__link, .nav__link').forEach((a) => {
      const file = (a.getAttribute('href') || '').split('/').pop();
      if (!file) return;
      const label = (a.querySelector('.nav__flip span') || a).textContent
        .replace(/^\s*0\d\s*/, '').trim();
      if (file && label && !map[file]) map[file] = label;
    });
    return map;
  })();

  const initTransitions = () => {
    const curtain = $('#curtain');
    if (!curtain) return;

    const titleEl = $('#curtainTitle');

    if (RM) { curtain.style.display = 'none'; return; }
    /* Durées calées sur le CSS :
         .is-out  0.50s  (le rideau monte et couvre)
         .is-in   0.55s  (il continue vers le haut et découvre)
       On navigue à 520ms, donc APRÈS la fin des 500ms : l'écran ne change
       plus au milieu du mouvement. Avant, on partait à 700ms alors que
       l'animation durait 820ms — d'où l'impression de saccade. */
    const OUT_MS = 500;
    const IN_MS = 550;
    const HOLD = SOFT ? 260 : OUT_MS + 20;

    // Arrivée : on repart d'un état propre. Si la page a été restaurée
    // depuis le cache du navigateur, la classe `is-out` de la page
    // précédente pouvait subsister : le rideau recouvrait alors la
    // nouvelle page au lieu de la découvrir.
    curtain.classList.remove('is-out');
    void curtain.offsetWidth;               // force la reprise de l'animation
    curtain.classList.add('is-in');
    setTimeout(() => curtain.classList.remove('is-in'), IN_MS + 60);

    const here = window.location.pathname.split('/').pop() || 'index.html';

    const isInternal = (a) => {
      if (!a || a.target === '_blank' || a.hasAttribute('download')) return false;
      const href = a.getAttribute('href') || '';
      if (!href) return false;
      if (/^(mailto:|tel:|#|https?:)/i.test(href)) return false;
      return /\.html?($|[?#])/i.test(href) || !href.includes('.');
    };

    document.addEventListener('click', (e) => {
      const a = e.target.closest('a');
      if (!a || !isInternal(a)) return;
      if (e.metaKey || e.ctrlKey || e.shiftKey || e.altKey || e.button !== 0) return;

      const url = a.getAttribute('href');
      const file = url.split('/').pop().split('#')[0].split('?')[0];
      if (file === here) return; // already here

      e.preventDefault();

      // Name the destination so the wait feels intentional
      if (titleEl) titleEl.textContent = PAGE_NAMES[file] || 'CD Boulangerie';

      // Flour puff from the click point
      if (window.CDFlour) window.CDFlour.burst(e.clientX, e.clientY, 34, 1.3);

      curtain.classList.remove('is-in');
      curtain.classList.add('is-out');

      // close the mobile menu behind the curtain
      document.body.classList.remove('is-menu-open');
      $('#menu')?.classList.remove('is-open');

      setTimeout(() => { window.location.href = url; }, HOLD);
    });

    // bfcache restore (back button) — reset the curtain
    window.addEventListener('pageshow', (e) => {
      if (e.persisted) {
        curtain.classList.remove('is-out');
        curtain.classList.add('is-in');
        document.body.classList.remove('is-locked');
        setTimeout(() => curtain.classList.remove('is-in'), 940);
      }
    });
  };

  /* ---------------------------------------------------------------------
     7b. MAGNETIC BUTTONS + TILT
  --------------------------------------------------------------------- */
  const initMagnetic = () => {
    if (SOFT || !window.matchMedia('(pointer: fine)').matches) return;

    /* Buttons pull toward the cursor */
    $$('.btn, .upnext__ico, .totop, .lb__btn').forEach((el) => {
      el.classList.add('magnetic');
      const strength = el.classList.contains('upnext__ico') ? 0.45 : 0.34;

      el.addEventListener('pointermove', (e) => {
        const r = el.getBoundingClientRect();
        const mx = (e.clientX - (r.left + r.width / 2)) * strength;
        const my = (e.clientY - (r.top + r.height / 2)) * strength;
        el.style.setProperty('--mx', mx.toFixed(2) + 'px');
        el.style.setProperty('--my', my.toFixed(2) + 'px');
      });

      el.addEventListener('pointerleave', () => {
        el.style.setProperty('--mx', '0px');
        el.style.setProperty('--my', '0px');
      });
    });

    /* Frames tilt in 3D */
    $$('.feat__media .frame, .hero__visual .frame, .gal__i .frame').forEach((el) => {
      el.classList.add('tilt');
      const wrap = el.parentElement;

      wrap.addEventListener('pointermove', (e) => {
        const r = el.getBoundingClientRect();
        const px = (e.clientX - r.left) / r.width - 0.5;
        const py = (e.clientY - r.top) / r.height - 0.5;
        el.style.setProperty('--ry', (px * 12).toFixed(2) + 'deg');
        el.style.setProperty('--rx', (-py * 12).toFixed(2) + 'deg');
      });

      wrap.addEventListener('pointerleave', () => {
        el.style.setProperty('--rx', '0deg');
        el.style.setProperty('--ry', '0deg');
      });
    });

    /* Flour puffs off interactive things on hover */
    const puff = (el, count, power) => {
      el.addEventListener('pointerenter', () => {
        if (!window.CDFlour) return;
        const r = el.getBoundingClientRect();
        window.CDFlour.burst(r.left + r.width / 2, r.top + r.height / 2, count, power);
      });
    };

    const mark = $('.brand__mark');
    if (mark) puff(mark, 26, 1.0);
    $$('.btn').forEach((el) => puff(el, 24, 0.95));
    $$('.pill, .qa__i').forEach((el) => puff(el, 18, 0.8));
    $$('.gal__i, .card').forEach((el) => puff(el, 20, 0.85));
  };

  /* ---------------------------------------------------------------------
     8. MARQUEE — duplicate track for a seamless loop
  --------------------------------------------------------------------- */
  const initMarquee = () => {
    $$('.marquee').forEach((m) => {
      const track = $('.marquee__track', m);
      if (!track) return;

      // Nettoyage (utile si la fonction est rejouée au redimensionnement)
      $$('.marquee__track', m).forEach((t, i) => { if (i > 0) t.remove(); });

      const base = parseInt(m.dataset.speed, 10) || 34;

      const build = () => {
        $$('.marquee__track[data-clone]', m).forEach((c) => c.remove());

        const w = track.scrollWidth;
        if (!w) return;

        // Il faut au moins 2 pistes ; davantage si l'écran est plus large
        // qu'une piste, sinon un trou apparaît pendant le défilement.
        const need = Math.max(2, Math.ceil(window.innerWidth / w) + 1);
        for (let i = 1; i < need; i++) {
          const c = track.cloneNode(true);
          c.setAttribute('aria-hidden', 'true');
          c.setAttribute('data-clone', '');
          m.appendChild(c);
        }

        // Vitesse constante en pixels/seconde : les bandeaux courts ne
        // filent pas plus vite que les longs.
        const PPS = 62;
        const dur = Math.max(12, Math.round(w / PPS));
        m.style.setProperty('--mq', dur + 's');
        void m.offsetWidth; // relance l'animation proprement
      };

      build();

      // Recalcul si la largeur change (rotation mobile, fenêtre redimensionnée)
      let t = null;
      window.addEventListener('resize', () => {
        clearTimeout(t);
        t = setTimeout(build, 220);
      }, { passive: true });

      // Les polices modifient la largeur une fois chargées
      if (document.fonts && document.fonts.ready) {
        document.fonts.ready.then(build).catch(() => {});
      }
    });
  };

  /* ---------------------------------------------------------------------
     9. PARALLAX — subtle depth on scroll
  --------------------------------------------------------------------- */
  const initParallax = () => {
    const items = $$('[data-para]');
    if (!items.length || SOFT) return;
    let ticking = false;

    const run = () => {
      const vh = window.innerHeight;
      items.forEach((el) => {
        const r = el.getBoundingClientRect();
        if (r.bottom < -200 || r.top > vh + 200) return;
        const amt = parseFloat(el.dataset.para) || 12;
        const prog = (r.top + r.height / 2 - vh / 2) / vh;
        el.style.transform = `translate3d(0, ${(-prog * amt).toFixed(2)}%, 0)`;
      });
      ticking = false;
    };

    window.addEventListener('scroll', () => {
      if (!ticking) { requestAnimationFrame(run); ticking = true; }
    }, { passive: true });
    window.addEventListener('resize', run, { passive: true });
    run();
  };

  /* ---------------------------------------------------------------------
     10. COUNTERS
  --------------------------------------------------------------------- */
  const initCounters = () => {
    const nums = $$('[data-count]');
    if (!nums.length) return;

    const run = (el) => {
      const target = parseFloat(el.dataset.count);
      const dec = (el.dataset.count.split('.')[1] || '').length;
      const suffix = el.dataset.suffix || '';
      if (SOFT) { el.textContent = target.toFixed(dec) + suffix; return; }
      const dur = 1500;
      const t0 = performance.now();
      const step = (t) => {
        const p = Math.min((t - t0) / dur, 1);
        const e = 1 - Math.pow(1 - p, 3);
        el.textContent = (target * e).toFixed(dec) + suffix;
        if (p < 1) requestAnimationFrame(step);
      };
      requestAnimationFrame(step);
    };

    if (!('IntersectionObserver' in window)) { nums.forEach(run); return; }
    const io = new IntersectionObserver((es) => {
      es.forEach((e) => { if (e.isIntersecting) { run(e.target); io.unobserve(e.target); } });
    }, { threshold: 0.5 });
    nums.forEach((n) => io.observe(n));
  };

  /* ---------------------------------------------------------------------
     11. ACCORDION
  --------------------------------------------------------------------- */
  const initAccordion = () => {
    $$('.acc').forEach((acc) => {
      const btns = $$('.acc__b', acc);
      btns.forEach((btn) => {
        const panel = document.getElementById(btn.getAttribute('aria-controls'));
        if (!panel) return;

        btn.addEventListener('click', () => {
          const open = btn.getAttribute('aria-expanded') === 'true';

          // close siblings
          btns.forEach((o) => {
            if (o === btn) return;
            const p = document.getElementById(o.getAttribute('aria-controls'));
            o.setAttribute('aria-expanded', 'false');
            if (p) p.style.height = '0px';
          });

          btn.setAttribute('aria-expanded', String(!open));
          panel.style.height = open ? '0px' : panel.scrollHeight + 'px';
        });
      });

      window.addEventListener('resize', () => {
        btns.forEach((b) => {
          if (b.getAttribute('aria-expanded') !== 'true') return;
          const p = document.getElementById(b.getAttribute('aria-controls'));
          if (p) p.style.height = p.scrollHeight + 'px';
        });
      }, { passive: true });
    });
  };

  /* ---------------------------------------------------------------------
     12. GALLERY FILTER + LIGHTBOX
  --------------------------------------------------------------------- */
  const initGallery = () => {
    const gal = $('#gal');
    const filters = $$('[data-filter]');

    if (gal && filters.length) {
      filters.forEach((f) => {
        f.addEventListener('click', () => {
          const cat = f.dataset.filter;
          filters.forEach((o) => o.setAttribute('aria-pressed', String(o === f)));
          $$('.gal__i', gal).forEach((item, i) => {
            const show = cat === 'all' || item.dataset.cat === cat;
            item.style.transitionDelay = (i * 22) + 'ms';
            item.classList.toggle('is-out', !show);
          });
        });
      });
    }

    /* Lightbox */
    const lb = $('#lb');
    if (!lb) return;
    const box = $('#lbBox');
    const cap = $('#lbCap');
    const idx = $('#lbIdx');
    let items = [];
    let cur = 0;

    const render = () => {
      const it = items[cur];
      if (!it) return;
      const img = it.querySelector('img');
      const label = it.dataset.cap || it.querySelector('.frame__cap')?.textContent.trim() || '';
      box.innerHTML = img
        ? `<figure class="frame frame--3x2"><img class="frame__img" src="${img.src}" alt="${img.alt}"></figure>`
        : `<figure class="frame frame--3x2"><div class="frame__ph">
             <span class="frame__ico">${plusIcon}</span>
             <span class="frame__cap">${label || 'Emplacement photo'}</span>
           </div></figure>`;
      if (cap) cap.textContent = label;
      if (idx) idx.textContent = `${String(cur + 1).padStart(2, '0')} / ${String(items.length).padStart(2, '0')}`;
    };

    let opener = null;   // vignette d'origine, pour y ramener le focus

    const open = (i) => {
      items = $$('.gal__i:not(.is-out)');
      cur = i;
      opener = items[i] || document.activeElement;
      render();
      lb.classList.add('is-open');
      lb.setAttribute('aria-hidden', 'false');
      lb.removeAttribute('inert');
      lb.inert = false;              // certains navigateurs gardent la propriété
      document.body.classList.add('is-locked');
      // `visibility` passe de hidden à visible via une transition : tant
      // qu'elle n'a pas basculé, l'élément refuse le focus. On réessaie
      // jusqu'à ce que ça prenne (max ~10 frames).
      let tries = 0;
      const grab = () => {
        const btn = $('#lbClose');
        if (!btn) return;
        btn.focus({ preventScroll: true });
        if (document.activeElement !== btn && ++tries < 10) {
          requestAnimationFrame(grab);
        }
      };
      requestAnimationFrame(grab);
    };
    const close = () => {
      lb.classList.remove('is-open');
      lb.setAttribute('aria-hidden', 'true');
      lb.setAttribute('inert', '');
      lb.inert = true;
      document.body.classList.remove('is-locked');
      // le focus retourne là où l'utilisateur l'avait laissé
      if (opener && document.body.contains(opener)) opener.focus();
      opener = null;
    };

    lb.setAttribute('inert', '');   // fermée au départ
    lb.inert = true;

    /* Piège de focus dans la visionneuse */
    lb.addEventListener('keydown', (e) => {
      if (e.key !== 'Tab' || !lb.classList.contains('is-open')) return;
      const f = $$('button, a', lb).filter((el) => el.offsetParent !== null);
      if (!f.length) return;
      const first = f[0], last = f[f.length - 1];
      if (e.shiftKey && document.activeElement === first) { e.preventDefault(); last.focus(); }
      else if (!e.shiftKey && document.activeElement === last) { e.preventDefault(); first.focus(); }
    });
    const move = (d) => { cur = (cur + d + items.length) % items.length; render(); };

    document.addEventListener('click', (e) => {
      const t = e.target.closest('.gal__i');
      if (t) { open($$('.gal__i:not(.is-out)').indexOf(t)); }
    });
    $('#lbClose')?.addEventListener('click', close);
    $('#lbPrev')?.addEventListener('click', () => move(-1));
    $('#lbNext')?.addEventListener('click', () => move(1));
    lb.addEventListener('click', (e) => { if (e.target === lb || e.target.id === 'lbStage') close(); });
    document.addEventListener('keydown', (e) => {
      if (!lb.classList.contains('is-open')) return;
      if (e.key === 'Escape') close();
      if (e.key === 'ArrowLeft') move(-1);
      if (e.key === 'ArrowRight') move(1);
    });

    /* swipe */
    let x0 = null;
    lb.addEventListener('touchstart', (e) => { x0 = e.changedTouches[0].clientX; }, { passive: true });
    lb.addEventListener('touchend', (e) => {
      if (x0 === null) return;
      const dx = e.changedTouches[0].clientX - x0;
      if (Math.abs(dx) > 60) move(dx > 0 ? -1 : 1);
      x0 = null;
    }, { passive: true });
  };

  const plusIcon = '<svg width="16" height="16" viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.2"><path d="M8 1v14M1 8h14"/></svg>';

  /* ---------------------------------------------------------------------
     13. FORM
  --------------------------------------------------------------------- */
  const initForm = () => {
    const form = $('#contactForm');
    if (!form) return;
    const msg = $('#formMsg');

    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const data = new FormData(form);
      const name = (data.get('nom') || '').toString().trim();
      const tel  = (data.get('tel') || '').toString().trim();
      const body = (data.get('message') || '').toString().trim();

      // Libellés fournis par le HTML => traduits automatiquement
      const D = form.dataset;

      const fName = $('#f-nom');
      const fBody = $('#f-msg');

      if (!name || !body) {
        // marque les champs fautifs pour les lecteurs d'écran…
        [[fName, !name], [fBody, !body]].forEach(([el, bad]) => {
          if (el) el.setAttribute('aria-invalid', bad ? 'true' : 'false');
        });
        if (msg) {
          msg.textContent = D.err || 'Merci de renseigner votre nom et votre message.';
          msg.style.color = '#99412F';
          msg.classList.add('is-on');
        }
        // …et amène l'utilisateur directement au premier champ à corriger
        const first = !name ? fName : fBody;
        if (first) { first.focus(); first.scrollIntoView({ block: 'center', behavior: SOFT ? 'auto' : 'smooth' }); }
        return;
      }

      [fName, fBody].forEach((el) => el && el.setAttribute('aria-invalid', 'false'));

      const to = D.mail || 'contact@cdboulangerie.fr';
      const subject = encodeURIComponent(`${D.subject || 'Demande de'} ${name}`);
      const lines = [name, tel, '', body].filter(Boolean);
      const mailto = `mailto:${to}?subject=${subject}&body=${encodeURIComponent(lines.join('\n'))}`;

      if (msg) {
        msg.textContent = D.opening || 'Ouverture de votre messagerie…';
        msg.style.color = '';
        msg.classList.add('is-on');
      }
      setTimeout(() => { window.location.href = mailto; }, 420);
    });
  };

  /* ---------------------------------------------------------------------
     14. BACK TO TOP
  --------------------------------------------------------------------- */
  /* ---------------------------------------------------------------------
     13b. SÉLECTEUR DE LANGUE
     Menu déroulant accessible : clic, Échap, clic extérieur, clavier.
     Dans le menu mobile la liste est toujours ouverte (pas de bouton).
  --------------------------------------------------------------------- */
  const initLang = () => {
    const boxes = $$('[data-lang]');
    if (!boxes.length) return;

    const closeAll = (except) => {
      boxes.forEach((b) => {
        if (b === except) return;
        b.classList.remove('is-open');
        const btn = $('.lang__btn', b);
        if (btn) btn.setAttribute('aria-expanded', 'false');
      });
    };

    boxes.forEach((box) => {
      const btn = $('.lang__btn', box);
      if (!btn) return;

      // Dans le menu plein écran, la liste est déjà visible.
      if (box.closest('.menu')) {
        btn.style.display = 'none';
        return;
      }

      btn.addEventListener('click', (e) => {
        e.stopPropagation();
        const open = box.classList.contains('is-open');
        closeAll(box);
        box.classList.toggle('is-open', !open);
        btn.setAttribute('aria-expanded', String(!open));
      });

      // Navigation clavier dans la liste
      box.addEventListener('keydown', (e) => {
        const items = $$('.lang__item', box);
        const i = items.indexOf(document.activeElement);
        if (e.key === 'Escape') {
          box.classList.remove('is-open');
          btn.setAttribute('aria-expanded', 'false');
          btn.focus();
        } else if (e.key === 'ArrowDown' && items.length) {
          e.preventDefault();
          if (!box.classList.contains('is-open')) {
            box.classList.add('is-open');
            btn.setAttribute('aria-expanded', 'true');
          }
          items[(i + 1) % items.length].focus();
        } else if (e.key === 'ArrowUp' && items.length) {
          e.preventDefault();
          items[(i - 1 + items.length) % items.length].focus();
        }
      });
    });

    document.addEventListener('click', () => closeAll(null));
  };

  /* ---------------------------------------------------------------------
     13c. BARRE SOCIALE FLOTTANTE
     Apparaît une fois le héros dépassé, se cache près du pied de page
     pour ne jamais chevaucher son contenu.
  --------------------------------------------------------------------- */
  const initSocialRail = () => {
    const rail = $('#socialRail');
    if (!rail) return;

    const footer = $('.footer');
    let ticking = false;

    const run = () => {
      const y = window.scrollY;
      let show = y > window.innerHeight * 0.6;
      if (show && footer) {
        const top = footer.getBoundingClientRect().top;
        if (top < window.innerHeight - 60) show = false;
      }
      rail.classList.toggle('is-on', show);
      ticking = false;
    };

    window.addEventListener('scroll', () => {
      if (!ticking) { requestAnimationFrame(run); ticking = true; }
    }, { passive: true });
    window.addEventListener('resize', run, { passive: true });
    run();
  };

  const initTop = () => {
    const b = $('#toTop');
    if (!b) return;
    let ticking = false;
    const run = () => { b.classList.toggle('is-on', window.scrollY > 700); ticking = false; };
    window.addEventListener('scroll', () => {
      if (!ticking) { requestAnimationFrame(run); ticking = true; }
    }, { passive: true });
    b.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: SOFT ? 'auto' : 'smooth' });
    });
    run();
  };

  /* ---------------------------------------------------------------------
     15. ANCHOR OFFSET (account for fixed header)
  --------------------------------------------------------------------- */
  const initAnchors = () => {
    document.addEventListener('click', (e) => {
      const a = e.target.closest('a[href^="#"]');
      if (!a) return;
      const id = a.getAttribute('href');
      if (!id || id === '#') return;
      const t = document.querySelector(id);
      if (!t) return;
      e.preventDefault();
      const top = t.getBoundingClientRect().top + window.scrollY - 78;
      window.scrollTo({ top, behavior: SOFT ? 'auto' : 'smooth' });
    });
  };

  /* ---------------------------------------------------------------------
     16. CURRENT YEAR
  --------------------------------------------------------------------- */
  const initYear = () => {
    $$('[data-year]').forEach((el) => el.textContent = new Date().getFullYear());
  };

  /* ---------------------------------------------------------------------
     BOOT
  --------------------------------------------------------------------- */
  const boot = () => {
    // Run each module in isolation: if one throws (blocked API, odd browser),
    // the rest of the page still works and nothing stays frozen.
    const run = (name, fn) => {
      try { fn(); }
      catch (err) { console.warn('[CD] ' + name + ' failed:', err); }
    };

    run('split', initSplit);
    run('reveal', initReveal);
    run('header', initHeader);
    run('progress', initProgress);
    run('menu', initMenu);
    run('transitions', initTransitions);
    run('magnetic', initMagnetic);
    run('marquee', initMarquee);
    run('parallax', initParallax);
    run('counters', initCounters);
    run('accordion', initAccordion);
    run('gallery', initGallery);
    run('form', initForm);
    run('lang', initLang);
    run('socialRail', initSocialRail);
    run('toTop', initTop);
    run('anchors', initAnchors);
    run('year', initYear);
    run('loader', initLoader);

    // Absolute last-resort guard: whatever happened above, the page must be
    // scrollable and the content visible.
    setTimeout(() => {
      document.body.classList.remove('is-locked');
      const l = document.getElementById('loader');
      if (l && !l.classList.contains('is-done')) l.remove();
      document.querySelectorAll('[data-reveal], .mask, [data-split]').forEach((el) => {
        const r = el.getBoundingClientRect();
        if (r.top < window.innerHeight * 1.2) el.classList.add('is-in', 'split-in');
      });
    }, 8000);
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();
