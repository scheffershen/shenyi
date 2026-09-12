/* Yi Shen — portfolio interactions.
   Vanilla, no dependencies, deferred. Everything here is an enhancement:
   the page is fully readable and navigable if this file never loads. */
(function () {
  "use strict";

  /* ---------- RAG Formation Continue shared navigation ---------- */
  var continuationPath = window.location.pathname;
  if (/\/ai-lab\/rag-formation\/continue\//.test(continuationPath) && !document.querySelector('.header')) {
    var continuationLocale = document.documentElement.lang;
    var continuationFile = continuationPath.split('/').pop() || '01-improve-your-rag.html';
    var hasLocalizedLesson = continuationFile === '01-improve-your-rag.html' || continuationFile === '02-build-your-rag-from-zero.html';
    var continuationRoot = continuationLocale === 'en' ? '../../../' : '../../../../';
    var continuationCopy = continuationLocale === 'fr'
      ? { home: 'accueil', services: 'Services', portfolio: 'Réalisations', lab: 'Laboratoire d’ingénierie IA', contact: 'Contact', change: 'Changer de langue', open: 'Ouvrir le menu', close: 'Fermer le menu', mobile: 'Navigation mobile', book: 'Réserver un appel de cadrage', hubs: 'Paris • Singapour • Shanghai', lang: 'FR', flag: '🇫🇷', en: 'English', fr: 'Français', zh: '中文' }
      : continuationLocale === 'zh-CN'
        ? { home: '首页', services: '服务', portfolio: '项目案例', lab: 'AI 工程实验室', contact: '联系', change: '切换语言', open: '打开菜单', close: '关闭菜单', mobile: '移动端导航', book: '预约需求沟通', hubs: '巴黎 • 新加坡 • 上海', lang: 'ZH', flag: '🇨🇳', en: 'English', fr: 'Français', zh: '中文' }
        : { home: 'home', services: 'Services', portfolio: 'Portfolio', lab: 'AI Engineering Lab', contact: 'Contact', change: 'Change language', open: 'Open menu', close: 'Close menu', mobile: 'Mobile navigation', book: 'Discuss a project', hubs: 'Paris • Singapore • Shanghai', lang: 'EN', flag: '🇬🇧', en: 'English', fr: 'Français', zh: '中文' };
    var languageTargets = hasLocalizedLesson
      ? { en: continuationRoot + 'ai-lab/rag-formation/continue/' + continuationFile, fr: continuationRoot + 'fr/ai-lab/rag-formation/continue/' + continuationFile, zh: continuationRoot + 'zh/ai-lab/rag-formation/continue/' + continuationFile }
      : { en: continuationRoot + 'ai-lab/rag-formation/continue/' + continuationFile, fr: continuationRoot + 'fr/ai-lab/rag-formation/', zh: continuationRoot + 'zh/ai-lab/rag-formation/' };
    var currentLanguage = continuationLocale === 'fr' ? 'fr' : continuationLocale === 'zh-CN' ? 'zh' : 'en';
    var navigation = '<a class="skip-link" href="#main">' + (continuationLocale === 'fr' ? 'Aller au contenu principal' : continuationLocale === 'zh-CN' ? '跳到主要内容' : 'Skip to content') + '</a><header class="header"><div class="wrap header-inner"><a class="brand" href="../../../" aria-label="SHEN YI — ' + continuationCopy.home + '"><span class="brand-mark" aria-hidden="true">YS</span><span class="brand-text"><span class="brand-name">SHEN YI</span><span class="brand-role">Full-Stack &amp; AI</span></span></a><p class="hubs-badge"><span class="dot" aria-hidden="true"></span>' + continuationCopy.hubs + '</p><nav class="nav-desktop" aria-label="' + continuationCopy.lab + '"><ul><li><a href="../../../#services">' + continuationCopy.services + '</a></li><li><a href="../../../#portfolio">' + continuationCopy.portfolio + '</a></li><li><a href="../../" aria-current="page">' + continuationCopy.lab + '</a></li><li><a href="../../../#contact">' + continuationCopy.contact + '</a></li></ul></nav><div class="lang"><button class="lang-toggle" type="button" aria-expanded="false" aria-controls="lang-menu"><span aria-hidden="true">' + continuationCopy.flag + '</span><span>' + continuationCopy.lang + '</span><span class="lang-caret" aria-hidden="true">⌄</span><span class="sr-only">' + continuationCopy.change + '</span></button><div class="lang-menu" id="lang-menu" role="menu"><a href="' + languageTargets.en + '" hreflang="en"' + (currentLanguage === 'en' ? ' aria-current="true"' : '') + ' role="menuitem">' + continuationCopy.en + '</a><a href="' + languageTargets.fr + '" hreflang="fr"' + (currentLanguage === 'fr' ? ' aria-current="true"' : '') + ' role="menuitem">' + continuationCopy.fr + '</a><a href="' + languageTargets.zh + '" hreflang="zh"' + (currentLanguage === 'zh' ? ' aria-current="true"' : '') + ' role="menuitem">' + continuationCopy.zh + '</a></div></div><button class="burger" type="button" aria-expanded="false" aria-controls="drawer"><span class="burger-box" aria-hidden="true"><span></span><span></span><span></span></span><span class="sr-only">' + continuationCopy.open + '</span></button></div></header><div class="drawer" id="drawer" aria-hidden="true"><div class="drawer-top"><button class="drawer-close" type="button"><span aria-hidden="true">✕</span><span class="sr-only">' + continuationCopy.close + '</span></button></div><nav aria-label="' + continuationCopy.mobile + '"><ul><li><a href="../../../#services"><i>01</i>' + continuationCopy.services + '</a></li><li><a href="../../../#portfolio"><i>02</i>' + continuationCopy.portfolio + '</a></li><li><a href="../../"><i>03</i>' + continuationCopy.lab + '</a></li><li><a href="../../../#contact"><i>04</i>' + continuationCopy.contact + '</a></li></ul></nav><div class="drawer-foot"><p class="drawer-hubs"><span class="dot" aria-hidden="true"></span>' + continuationCopy.hubs + '</p><a class="btn btn-primary btn-block" href="../../../#contact">' + continuationCopy.book + '</a></div></div>';
    navigation = navigation.replaceAll('href="../../../', 'href="' + continuationRoot);
    document.body.insertAdjacentHTML('afterbegin', navigation);
  }

  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---------- Sticky header shadow ---------- */
  var header = document.querySelector(".header");
  if (header) {
    var onScroll = function () {
      header.classList.toggle("is-stuck", window.scrollY > 8);
    };
    onScroll();
    window.addEventListener("scroll", onScroll, { passive: true });
  }

  /* ---------- Mobile drawer ---------- */
  var burger = document.querySelector(".burger");
  var drawer = document.getElementById("drawer");
  var drawerClose = document.querySelector(".drawer-close");

  function setDrawer(open) {
    if (!drawer || !burger) return;
    drawer.classList.toggle("is-open", open);
    burger.setAttribute("aria-expanded", String(open));
    drawer.setAttribute("aria-hidden", String(!open));
    // Lock the page behind the overlay without losing scroll position.
    document.body.style.overflow = open ? "hidden" : "";
    if (open) {
      var first = drawer.querySelector("a, button");
      if (first) first.focus();
    } else {
      burger.focus();
    }
  }

  if (burger) burger.addEventListener("click", function () {
    setDrawer(!drawer.classList.contains("is-open"));
  });
  if (drawerClose) drawerClose.addEventListener("click", function () { setDrawer(false); });

  // Any in-drawer navigation closes it.
  if (drawer) {
    drawer.addEventListener("click", function (e) {
      var link = e.target.closest("a");
      if (link && link.getAttribute("href") && link.getAttribute("href").charAt(0) === "#") {
        setDrawer(false);
      }
    });
  }

  /* ---------- Language switcher ---------- */
  var lang = document.querySelector(".lang");
  var langToggle = document.querySelector(".lang-toggle");

  function setLang(open) {
    if (!lang || !langToggle) return;
    lang.classList.toggle("is-open", open);
    langToggle.setAttribute("aria-expanded", String(open));
  }

  if (langToggle) {
    langToggle.addEventListener("click", function (e) {
      e.stopPropagation();
      setLang(!lang.classList.contains("is-open"));
    });
  }

  document.addEventListener("click", function (e) {
    if (lang && !lang.contains(e.target)) setLang(false);
  });

  document.addEventListener("keydown", function (e) {
    if (e.key !== "Escape") return;
    setLang(false);
    if (drawer && drawer.classList.contains("is-open")) setDrawer(false);
  });

  /* ---------- Terminal line reveal ---------- */
  var rows = document.querySelectorAll(".terminal-body .row");
  if (rows.length) {
    if (reduceMotion) {
      rows.forEach(function (r) { r.classList.add("is-in"); });
    } else {
      rows.forEach(function (row, i) {
        row.style.animationDelay = (0.18 + i * 0.14).toFixed(2) + "s";
        row.classList.add("is-in");
      });
    }
  }

  /* ---------- Scroll reveal ----------
     The stylesheet parks .reveal at opacity 0, so this code is the only thing
     that makes the page's content visible. Treat every failure mode as
     "show the content" — a missed animation is nothing, a blank page is fatal. */
  var reveals = document.querySelectorAll(".reveal");

  function revealAll() {
    reveals.forEach(function (el) { el.classList.add("is-in"); });
  }

  if (reveals.length) {
    if (reduceMotion || !("IntersectionObserver" in window)) {
      revealAll();
    } else {
      var ioFired = false;

      var io = new IntersectionObserver(function (entries) {
        ioFired = true;
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          // Slight stagger for siblings revealed in the same batch.
          var delay = parseFloat(entry.target.dataset.delay || "0");
          setTimeout(function () { entry.target.classList.add("is-in"); }, delay * 1000);
          io.unobserve(entry.target);
        });
      }, { rootMargin: "0px 0px -8% 0px", threshold: 0.08 });

      reveals.forEach(function (el) { io.observe(el); });

      // Anything already on screen at load shouldn't wait on the observer.
      reveals.forEach(function (el) {
        if (el.getBoundingClientRect().top < window.innerHeight) el.classList.add("is-in");
      });

      // Failsafe: if the observer never reports back, unhide everything rather
      // than leaving the page blank. Only counts time while the page is
      // actually visible — a tab loaded in the background legitimately gets no
      // callbacks until the user looks at it.
      var armFailsafe = function () {
        setTimeout(function () { if (!ioFired) revealAll(); }, 2000);
      };
      if (document.visibilityState === "visible") {
        armFailsafe();
      } else {
        document.addEventListener("visibilitychange", function onShow() {
          if (document.visibilityState !== "visible") return;
          document.removeEventListener("visibilitychange", onShow);
          armFailsafe();
        });
      }
    }
  }

  /* ---------- Cookie consent (GA4 Consent Mode) ---------- */
  var consentBanner = document.getElementById("consentBanner");
  if (consentBanner && window.gtag) {
    var storedConsent = localStorage.getItem("consent_analytics");
    if (storedConsent === "granted") {
      gtag("consent", "update", { analytics_storage: "granted" });
    } else if (!storedConsent) {
      consentBanner.hidden = false;
    }
    consentBanner.addEventListener("click", function (e) {
      var btn = e.target.closest("[data-consent]");
      if (!btn) return;
      var granted = btn.dataset.consent === "accept";
      gtag("consent", "update", { analytics_storage: granted ? "granted" : "denied" });
      localStorage.setItem("consent_analytics", granted ? "granted" : "denied");
      consentBanner.hidden = true;
    });
  }

  // Lets visitors reopen the banner from the footer to change an earlier choice.
  document.querySelectorAll("[data-consent-manage]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      if (consentBanner) consentBanner.hidden = false;
    });
  });

  /* ---------- RAG Formation completion and supplementary lesson ---------- */
  var path = window.location.pathname;
  var locale = document.documentElement.lang;
  if (/\/(?:fr\/|zh\/)?ai-lab\/$/.test(path)) {
    var roadmapLink = document.querySelector('a[href="rag-formation/"]');
    var courseCard = roadmapLink && roadmapLink.closest('article');
    if (courseCard) {
      var completed = locale === 'fr' ? 'Parcours terminé · 16 leçons' : locale === 'zh-CN' ? '课程已完成 · 16 节课' : 'Complete · 16 lessons';
      var status = courseCard.querySelector('.ai-lab-status');
      var flag = courseCard.querySelector('.card-flag');
      var focus = courseCard.querySelector('.card-focus');
      if (flag) flag.textContent = completed;
      if (status) { status.textContent = completed; status.classList.remove('is-future'); }
      if (focus) focus.textContent = locale === 'fr' ? 'Un parcours de 16 leçons achevé pour construire, évaluer et améliorer un chatbot RAG fiable.' : locale === 'zh-CN' ? '一套已完成的 16 节课程，学习构建、评估和改进可靠的 RAG 聊天机器人。' : 'A completed 16-lesson course for building, evaluating, and improving a reliable RAG chatbot.';
    }
  }
  if (/(?:^|\/)(?:fr\/|zh\/)?(?:index\.html)?$/.test(path)) {
    var labSection = document.getElementById('ai-lab');
    var labGrid = labSection && labSection.querySelector('.ai-lab-grid');
    if (labGrid && !document.getElementById('rag-formation-continue-card')) {
      var continuation = locale === 'fr'
        ? { status: 'Leçon complémentaire', title: 'RAG Formation Continue · 01 · Boucle d’amélioration en production', text: 'Transformer les logs d’interaction et le feedback utilisateur en plan d’amélioration RAG fondé sur les preuves, avec Claude Code ou Codex.', link: 'Ouvrir la leçon' }
        : locale === 'zh-CN'
          ? { status: '补充实战课程', title: 'RAG Formation Continue · 01 · 生产改进闭环', text: '使用 Claude Code 或 Codex，将交互日志和用户反馈转化为基于证据的 RAG 改进计划。', link: '打开课程' }
          : { status: 'Supplementary lesson', title: 'RAG Formation Continue · 01 · Production improvement loop', text: 'Turn interaction logs and user feedback into an evidence-backed RAG improvement plan with Claude Code or Codex.', link: 'Open lesson' };
      var card = document.createElement('article');
      card.id = 'rag-formation-continue-card';
      card.className = 'card ai-lab-card';
      card.innerHTML = '<span class="ai-lab-status">' + continuation.status + '</span><h3>' + continuation.title + '</h3><p class="card-focus">' + continuation.text + '</p><a class="card-link" href="ai-lab/rag-formation/continue/01-improve-your-rag.html">' + continuation.link + ' <span aria-hidden="true">→</span></a>';
      labGrid.appendChild(card);
    }
    if (labGrid && !document.getElementById('rag-formation-baseline-card')) {
      var baseline = locale === 'fr'
        ? { status: 'Leçon complémentaire', title: 'RAG Formation Continue · 02 · Construire votre chatbot RAG à partir de zéro', text: 'Construire une base RAG à quatre canaux avec réponses fondées, citations et refus honnêtes, avant le feedback et les suivis.', link: 'Ouvrir la leçon' }
        : locale === 'zh-CN'
          ? { status: '补充实战课程', title: 'RAG Formation Continue · 02 · 从零构建自己的 RAG 聊天机器人', text: '构建具备有据回答、引用和诚实拒答的四通道 RAG 基线，再加入反馈和追问处理。', link: '打开课程' }
          : { status: 'Supplementary lesson', title: 'RAG Formation Continue · 02 · Build your own RAG chatbot from zero', text: 'Build a four-channel RAG baseline with grounded answers, cited sources, and honest refusals—before adding feedback or follow-up handling.', link: 'Open lesson' };
      var baselineCard = document.createElement('article');
      baselineCard.id = 'rag-formation-baseline-card';
      baselineCard.className = 'card ai-lab-card';
      baselineCard.innerHTML = '<span class="ai-lab-status">' + baseline.status + '</span><h3>' + baseline.title + '</h3><p class="card-focus">' + baseline.text + '</p><a class="card-link" href="ai-lab/rag-formation/continue/02-build-your-rag-from-zero.html">' + baseline.link + ' <span aria-hidden="true">→</span></a>';
      labGrid.appendChild(baselineCard);
    }
  }
  if (/\/(?:fr\/|zh\/)?ai-lab\/rag-formation\/(?:index\.html)?$/.test(path) && !document.getElementById('rag-formation-continue')) {
    var lesson = locale === 'fr'
      ? { eyebrow: 'Leçon terrain complémentaire', text: 'Transformer les logs et le feedback utilisateur en plan d’amélioration RAG fondé sur les preuves, avec Claude Code ou Codex.', link: 'Ouvrir la leçon' }
      : locale === 'zh-CN'
        ? { eyebrow: '补充实战课程', text: '使用 Claude Code 或 Codex，将交互日志和用户反馈转化为基于证据的 RAG 改进计划。', link: '打开课程' }
        : { eyebrow: 'Supplementary field lesson', text: 'Turn interaction logs and user feedback into an evidence-backed RAG improvement plan with Claude Code or Codex.', link: 'Open lesson' };
    var section = document.createElement('section');
    section.id = 'rag-formation-continue';
    section.className = 'section wrap';
    section.innerHTML = '<div class="card"><p class="card-index">' + lesson.eyebrow + '</p><h2>RAG Formation Continue · 01</h2><p class="card-focus">' + lesson.text + '</p><a class="card-link" href="continue/01-improve-your-rag.html">' + lesson.link + ' <span aria-hidden="true">→</span></a></div>';
    var lessons = document.getElementById('lessons');
    if (lessons) lessons.insertAdjacentElement('afterend', section);
  }
  if (/\/(?:fr\/|zh\/)?ai-lab\/rag-formation\/(?:index\.html)?$/.test(path) && !document.getElementById('rag-formation-baseline')) {
    var baselineLesson = locale === 'fr'
      ? { eyebrow: 'Leçon terrain complémentaire', text: 'Construire une base RAG à quatre canaux avec réponses fondées, citations et refus honnêtes, avant le feedback et les suivis.', link: 'Ouvrir la leçon' }
      : locale === 'zh-CN'
        ? { eyebrow: '补充实战课程', text: '构建具备有据回答、引用和诚实拒答的四通道 RAG 基线，再加入反馈和追问处理。', link: '打开课程' }
        : { eyebrow: 'Supplementary field lesson', text: 'Build a four-channel RAG chatbot baseline with cited answers and honest refusals before adding feedback or follow-up handling.', link: 'Open lesson' };
    var continuationSection = document.getElementById('rag-formation-continue');
    var baselineSection = document.createElement('section');
    baselineSection.id = 'rag-formation-baseline';
    baselineSection.className = 'section wrap';
    baselineSection.innerHTML = '<div class="card"><p class="card-index">' + baselineLesson.eyebrow + '</p><h2>RAG Formation Continue · 02</h2><p class="card-focus">' + baselineLesson.text + '</p><a class="card-link" href="continue/02-build-your-rag-from-zero.html">' + baselineLesson.link + ' <span aria-hidden="true">→</span></a></div>';
    if (continuationSection) continuationSection.insertAdjacentElement('afterend', baselineSection);
  }

  /* ---------- Footer year ---------- */
  var year = document.querySelector("[data-year]");
  if (year) year.textContent = String(new Date().getFullYear());
})();
