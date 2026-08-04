/* Yi Shen — portfolio interactions.
   Vanilla, no dependencies, deferred. Everything here is an enhancement:
   the page is fully readable and navigable if this file never loads. */
(function () {
  "use strict";

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

  /* ---------- Footer year ---------- */
  var year = document.querySelector("[data-year]");
  if (year) year.textContent = String(new Date().getFullYear());
})();
