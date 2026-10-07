/* Parc des Expositions d’Abidjan — comportements partagés (maquette) : menu mobile, filtres, visite 360°, formulaire de devis */
(function () {
  // Textes générés par le script, selon la langue de la page
  var EN = document.documentElement.lang === 'en';
  var calmMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var T = EN ? {
    pause: 'Pause the slideshow', play: 'Resume the slideshow', thousands: ',',
    logosPause: 'Pause scrolling', logosPlay: 'Resume scrolling', morePhotos: 'Show more photos',
    recap: { type: 'Event type', espace: 'Venue', dates: 'Dates', none: 'To be confirmed', to: ' to ' },
    location: 'Abidjan Exhibition Center, Boulevard de l’aéroport, Abidjan'
  } : {
    pause: 'Mettre le diaporama en pause', play: 'Relancer le diaporama', thousands: '\u00a0',
    logosPause: 'Mettre le défilement en pause', logosPlay: 'Relancer le défilement', morePhotos: 'Afficher plus de photos',
    recap: { type: 'Type d’événement', espace: 'Espace', dates: 'Dates', none: 'À préciser', to: ' au ' },
    location: 'Parc des Expositions d’Abidjan, Boulevard de l’aéroport, Abidjan'
  };
  // ---------- Menu mobile ----------
  var toggle = document.querySelector('.menu-toggle');
  var nav = document.getElementById('nav-principale');
  if (toggle && nav) {
    var isOpen = function () { return toggle.getAttribute('aria-expanded') === 'true'; };
    var setOpen = function (open) {
      toggle.setAttribute('aria-expanded', String(open));
      nav.classList.toggle('is-open', open);
    };
    toggle.addEventListener('click', function () { setOpen(!isOpen()); });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && isOpen()) { setOpen(false); toggle.focus(); }
    });
    // Le menu se referme quand le focus quitte le bouton et le panneau
    document.addEventListener('focusin', function (e) {
      if (isOpen() && !nav.contains(e.target) && e.target !== toggle) setOpen(false);
    });
    window.matchMedia('(min-width: 70em)').addEventListener('change', function () { setOpen(false); });
  }

  // ---------- Filtres ----------
  // Chaque groupe [data-filters="cible"][data-key="clé"] filtre les enfants de #cible
  // selon leur attribut data-<clé> (liste de valeurs séparées par des espaces).
  var groups = document.querySelectorAll('[data-filters]');
  var applyFilters = function (targetId) {
    var target = document.getElementById(targetId);
    if (!target) return;
    var active = [];
    document.querySelectorAll('[data-filters="' + targetId + '"]').forEach(function (g) {
      var pressed = g.querySelector('[aria-pressed="true"]');
      var value = pressed ? pressed.getAttribute('data-value') : '';
      if (value) active.push({ key: g.getAttribute('data-key'), value: value });
    });
    var shown = 0;
    var heading = null;
    var headingHasItems = false;
    var closeHeading = function () { if (heading) heading.hidden = !headingHasItems; };
    Array.prototype.forEach.call(target.children, function (item) {
      // Les intertitres (data-heading, ex. les mois de l’agenda) restent visibles s’ils ont au moins un élément affiché
      if (item.hasAttribute('data-heading')) {
        closeHeading();
        heading = item;
        headingHasItems = false;
        return;
      }
      var ok = active.every(function (f) {
        return (item.getAttribute('data-' + f.key) || '').split(' ').indexOf(f.value) !== -1;
      });
      item.hidden = !ok;
      if (ok) { shown++; headingHasItems = true; }
    });
    closeHeading();
    var status = document.querySelector('[data-status-for="' + targetId + '"]');
    var empty = document.querySelector('[data-empty-for="' + targetId + '"]');
    if (status) {
      var noun = status.getAttribute('data-noun') || status.textContent.replace(/^\d+\s+/, '').replace(/s$/, '');
      status.setAttribute('data-noun', noun);
      status.textContent = shown + ' ' + noun + (shown > 1 ? 's' : '');
    }
    if (empty) empty.hidden = shown !== 0;
    target.dispatchEvent(new CustomEvent('filtered'));
  };
  groups.forEach(function (group) {
    group.addEventListener('click', function (e) {
      var btn = e.target.closest('button');
      if (!btn) return;
      group.querySelectorAll('button').forEach(function (b) {
        b.setAttribute('aria-pressed', String(b === btn));
      });
      applyFilters(group.getAttribute('data-filters'));
    });
  });

  // ---------- Agenda : repère du prochain événement (selon la date du jour) ----------
  var today = new Date().toISOString().slice(0, 10);
  var next = Array.prototype.find.call(document.querySelectorAll('.tl-item[data-end]'), function (item) {
    return item.getAttribute('data-end') >= today;
  });
  if (next) {
    next.classList.add('is-next');
    var label = next.querySelector('.tl-card__next');
    if (label) label.hidden = false;
  }

  // ---------- Visite virtuelle Matterport : chargée seulement au clic (façade) ----------
  var launch = document.querySelector('[data-tour-src]');
  if (launch) {
    launch.addEventListener('click', function (e) {
      e.preventDefault();
      var stage = launch.parentElement;
      var frame = document.createElement('iframe');
      frame.src = launch.getAttribute('data-tour-src');
      frame.title = launch.getAttribute('data-tour-title');
      frame.allow = 'autoplay; fullscreen; web-share; xr-spatial-tracking';
      frame.setAttribute('allowfullscreen', '');
      stage.classList.add('is-live');
      stage.replaceChildren(frame);
      frame.focus();
    });
  }

  // ---------- En-tête transparent (toutes les pages) : fond blanc dès qu'on défile ou que le menu est ouvert ----------
  var overlay = document.querySelector('.topbar--overlay');
  if (overlay) {
    var menuBtn = overlay.querySelector('.menu-toggle');
    var syncHeader = function () {
      var open = menuBtn && menuBtn.getAttribute('aria-expanded') === 'true';
      overlay.classList.toggle('is-solid', window.scrollY > 8 || open);
    };
    window.addEventListener('scroll', syncHeader, { passive: true });
    if (menuBtn) new MutationObserver(syncHeader).observe(menuBtn, { attributes: true, attributeFilter: ['aria-expanded'] });
    syncHeader();
  }

  // ---------- Apparition au défilement (très discrète) ----------
  // Fondu + montée de 12 px, une seule fois, uniquement pour ce qui est encore sous la ligne de flottaison au chargement
  // (rien ne clignote au-dessus du pli). Un bloc dépassé d'un coup (touche Fin, ancre) est révélé aussi : on teste
  // « haut du bloc au-dessus de 92 % de l'écran » plutôt qu'une intersection. Rien avec « réduire les animations ».
  if (!window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    var ITEMS = '.figure, .space, .service, .event, .tl-item, .gallery__item, .wall__tile, .destination-grid > *, .commitments > *, .support__list > *';
    var targets = [];
    document.querySelectorAll('main section:not(.hero):not(.page-hero) > .wrap > *').forEach(function (block) {
      var items = block.matches(ITEMS) ? [] : block.querySelectorAll(ITEMS);
      if (items.length) items.forEach(function (it) { targets.push(it); });
      else targets.push(block);
    });
    var pending = [];
    var line = function () { return window.innerHeight * 0.92; };
    targets.forEach(function (el) {
      if (el.getBoundingClientRect().top < line()) return;   // déjà visible au chargement
      var sibs = Array.prototype.filter.call(el.parentElement.children, function (c) { return targets.indexOf(c) > -1; });
      el.style.setProperty('--reveal-delay', Math.min(sibs.indexOf(el) % 4, 3) * 70 + 'ms');
      el.classList.add('reveal');
      pending.push(el);
    });
    var ticking = false;
    var check = function () {
      ticking = false;
      pending = pending.filter(function (el) {
        var r = el.getBoundingClientRect();
        if (r.top >= line() || (!r.width && !r.height)) return true;   // encore sous le pli, ou masqué par un filtre
        el.classList.add('is-in');
        // On rend ensuite la main aux transitions propres de l'élément (survols)
        window.setTimeout(function () { el.classList.remove('reveal', 'is-in'); el.style.removeProperty('--reveal-delay'); }, 700 + (parseInt(el.style.getPropertyValue('--reveal-delay'), 10) || 0));
        return false;
      });
      if (!pending.length) { window.removeEventListener('scroll', onRevealScroll); window.removeEventListener('resize', onRevealScroll); }
    };
    var onRevealScroll = function () { if (!ticking) { ticking = true; window.requestAnimationFrame(check); } };
    if (pending.length) {
      window.addEventListener('scroll', onRevealScroll, { passive: true });
      window.addEventListener('resize', onRevealScroll, { passive: true });
      document.addEventListener('click', function () { window.setTimeout(onRevealScroll, 50); });   // filtres qui affichent d'autres cartes
    }
  }

  // ---------- Retour en haut : visible après un écran de défilement ----------
  var toTop = document.querySelector('.to-top');
  if (toTop) {
    var onScroll = function () { toTop.classList.toggle('is-visible', window.scrollY > window.innerHeight * 0.8); };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  // ---------- Consentement : bandeau cookies et contenus tiers ----------
  var CONSENT_KEY = 'pea-consent';
  var readConsent = function () {
    try { return window.localStorage.getItem(CONSENT_KEY); } catch (err) { return null; }
  };
  var writeConsent = function (value) {
    try { window.localStorage.setItem(CONSENT_KEY, value); } catch (err) { /* stockage indisponible : le choix vaut pour la page */ }
  };
  var banner = document.getElementById('cookie-consent');
  // Intégrations tierces (carte, fil Facebook) : chargées après accord ou à la demande
  var loadEmbed = function (box) {
    if (!box || box.querySelector('iframe')) return;
    var frame = document.createElement('iframe');
    frame.src = box.getAttribute('data-embed-src');
    frame.title = box.getAttribute('data-embed-title');
    frame.loading = 'lazy';
    frame.referrerPolicy = 'no-referrer-when-downgrade';
    frame.setAttribute('allowfullscreen', '');
    box.replaceChildren(frame);
  };
  var applyConsent = function (value) {
    if (value === 'accepted') document.querySelectorAll('[data-embed-src]').forEach(loadEmbed);
  };
  // Hauteur du bandeau exposée au CSS : le bouton « retour en haut » reste au-dessus
  var syncBanner = function () {
    document.documentElement.style.setProperty('--banner-h', banner && !banner.hidden ? banner.offsetHeight + 'px' : '0px');
  };
  if (banner) {
    var current = readConsent();
    if (!current) banner.hidden = false;
    syncBanner();
    window.addEventListener('resize', syncBanner);
    applyConsent(current);
    banner.addEventListener('click', function (e) {
      var btn = e.target.closest('[data-consent]');
      if (!btn) return;
      var value = btn.getAttribute('data-consent');
      writeConsent(value);
      banner.hidden = true;
      syncBanner();
      applyConsent(value);
    });
    document.querySelectorAll('[data-consent-open]').forEach(function (btn) {
      btn.addEventListener('click', function () {
        banner.hidden = false;
        syncBanner();
        banner.querySelector('[data-consent]').focus();
      });
    });
  }
  document.querySelectorAll('[data-embed-load]').forEach(function (btn) {
    btn.addEventListener('click', function () { loadEmbed(btn.closest('[data-embed-src]')); });
  });

  // ---------- Événements : fenêtre de détails ----------
  var dialog = document.getElementById('event-dialog');
  if (dialog && typeof dialog.showModal === 'function') {
    var dlgBody = dialog.querySelector('.event-dialog__body');
    var currentItem = null;
    var openEvent = function (item) {
      currentItem = item;
      dialog.querySelector('.event-dialog__type').textContent = item.querySelector('.tl-card__type').firstChild.textContent;
      dialog.querySelector('.event-dialog__title').textContent = item.querySelector('.tl-card__title').textContent;
      dialog.querySelector('.event-dialog__when').textContent = item.querySelector('.tl-card__when').textContent;
      var cardImg = item.querySelector('.tl-card__media img');
      var dlgImg = dialog.querySelector('.event-dialog__img');
      if (dlgImg) {
        dlgImg.hidden = !cardImg;
        if (cardImg) dlgImg.src = cardImg.currentSrc || cardImg.src;
      }
      dlgBody.replaceChildren();
      Array.prototype.forEach.call(item.querySelector('[data-event-more]').children, function (child) {
        dlgBody.appendChild(child.cloneNode(true));
      });
      if (!dialog.open) dialog.showModal();
      history.replaceState(null, '', '#' + item.id);
    };
    document.querySelectorAll('[data-event-open]').forEach(function (btn) {
      btn.addEventListener('click', function () { openEvent(btn.closest('.tl-item')); });
    });
    // Toutes les fermetures passent par closeEvent : bouton, fond assombri, touche Échap
    var closeEvent = function () {
      if (dialog.open) dialog.close();
      history.replaceState(null, '', window.location.pathname + window.location.search);
      var opener = currentItem && currentItem.querySelector('[data-event-open]');
      if (opener) opener.focus();
    };
    dialog.querySelector('.event-dialog__close').addEventListener('click', closeEvent);
    dialog.addEventListener('click', function (e) { if (e.target === dialog) closeEvent(); });
    dialog.addEventListener('cancel', function (e) { e.preventDefault(); closeEvent(); });
    // Ajout à l'agenda du visiteur (.ics, événement sur la journée entière)
    dialog.querySelector('[data-event-ics]').addEventListener('click', function () {
      if (!currentItem) return;
      var day = function (iso, add) {
        var d = new Date(iso + 'T00:00:00Z');
        d.setUTCDate(d.getUTCDate() + (add || 0));
        return d.toISOString().slice(0, 10).replace(/-/g, '');
      };
      var esc = function (t) { return t.replace(/([,;\\])/g, '\\$1').replace(/\n/g, '\\n'); };
      var title = currentItem.querySelector('.tl-card__title').textContent;
      var desc = currentItem.querySelector('.ev-desc').textContent;
      var ics = [
        'BEGIN:VCALENDAR', 'VERSION:2.0', 'PRODID:-//Parc des Expositions d’Abidjan//Agenda//FR', 'BEGIN:VEVENT',
        'UID:' + currentItem.id + '@parcdesexpositionsabidjan',
        'DTSTAMP:' + new Date().toISOString().replace(/[-:]/g, '').slice(0, 15) + 'Z',
        'DTSTART;VALUE=DATE:' + day(currentItem.getAttribute('data-start')),
        'DTEND;VALUE=DATE:' + day(currentItem.getAttribute('data-end'), 1),
        'SUMMARY:' + esc(title), 'DESCRIPTION:' + esc(desc),
        'LOCATION:' + esc(T.location),
        'END:VEVENT', 'END:VCALENDAR'
      ].join('\r\n');
      var link = document.createElement('a');
      link.href = URL.createObjectURL(new Blob([ics], { type: 'text/calendar' }));
      link.download = currentItem.id + '.ics';
      document.body.appendChild(link);
      link.click();
      link.remove();
    });
    // Lien direct : agenda.html#concert-tayc ouvre la fiche de l'événement
    var target = window.location.hash && document.getElementById(window.location.hash.slice(1));
    if (target && target.classList.contains('tl-item')) openEvent(target);
  }

  // ---------- Chiffres-clés : comptage à l'apparition (la valeur finale reste lue par les lecteurs d'écran) ----------
  var counters = document.querySelectorAll('[data-count]');
  if (counters.length && 'IntersectionObserver' in window && !window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
    var format = function (n) { return String(n).replace(/\B(?=(\d{3})+(?!\d))/g, T.thousands); };
    var animate = function (el) {
      var target = Number(el.getAttribute('data-count'));
      var t0 = null;
      var step = function (t) {
        if (t0 === null) t0 = t;
        var p = Math.min((t - t0) / 1600, 1);
        el.textContent = format(Math.round(target * (1 - Math.pow(1 - p, 3))));
        if (p < 1) window.requestAnimationFrame(step);
      };
      window.requestAnimationFrame(step);
    };
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        io.unobserve(entry.target);
        animate(entry.target);
      });
    }, { threshold: 0.6 });
    counters.forEach(function (el) { el.textContent = '0'; io.observe(el); });
  }

  // ---------- Diaporama Ken Burns de l'accueil ----------
  var hero = document.querySelector('[data-slider]');
  if (hero) {
    var slides = hero.querySelectorAll('.slider__slide');
    var dots = hero.querySelectorAll('.slider__dot');
    var toggleBtn = hero.querySelector('.slider__toggle');
    var index = 0;
    var timer = null;
    var userPaused = false; // défilement automatique ; le bouton Pause permet de l'arrêter (WCAG 2.2.2)
    var show = function (i) {
      slides[index].classList.remove('is-active');
      slides[index].classList.add('was-active');
      var prev = slides[index];
      window.setTimeout(function () { prev.classList.remove('was-active'); }, 1500);
      dots[index].removeAttribute('aria-current');
      index = (i + slides.length) % slides.length;
      var img = slides[index].querySelector('img');
      if (img && img.loading === 'lazy') img.loading = 'eager';
      slides[index].classList.add('is-active');
      // Couleur des boutons accordée à l'image (attributs calculés à la génération)
      hero.style.setProperty('--slide-accent', slides[index].getAttribute('data-accent'));
      hero.style.setProperty('--slide-accent-hover', slides[index].getAttribute('data-accent-hover'));
      hero.style.setProperty('--slide-title', slides[index].getAttribute('data-accent-title'));
      dots[index].setAttribute('aria-current', 'true');
    };
    var stop = function () { window.clearInterval(timer); timer = null; };
    var start = function () { if (!timer && !userPaused) timer = window.setInterval(function () { show(index + 1); }, 7000); };
    var setPaused = function (paused) {
      userPaused = paused;
      hero.classList.toggle('is-paused', paused);
      toggleBtn.setAttribute('aria-pressed', String(paused));
      toggleBtn.setAttribute('aria-label', paused ? T.play : T.pause);
      if (paused) stop(); else start();
    };
    toggleBtn.addEventListener('click', function () { setPaused(!userPaused); });
    dots.forEach(function (dot) {
      dot.addEventListener('click', function () { show(Number(dot.getAttribute('data-slide'))); stop(); start(); });
    });
    // Onglet masqué : on suspend, puis on reprend au retour
    document.addEventListener('visibilitychange', function () { if (document.hidden) stop(); else start(); });
    setPaused(userPaused);
  }

  // ---------- Références : carrousel de logos (page suivante toutes les 5 s, Pause, flèches) ----------
  var logos = document.querySelector('[data-logos]');
  if (logos) {
    var track = logos.querySelector('.logos__track');
    var zone = logos.closest('section');
    var lToggle = zone.querySelector('.logos__toggle');
    var smooth = window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth';
    var lTimer = null;
    var lPaused = false;
    var turn = function (dir) {
      var max = track.scrollWidth - track.clientWidth;
      var x = track.scrollLeft + dir * track.clientWidth;
      if (dir > 0 && track.scrollLeft >= max - 4) x = 0;          // fin : retour au début
      if (dir < 0 && track.scrollLeft <= 4) x = max;               // début : vers la fin
      track.scrollTo({ left: x, behavior: smooth });
    };
    var lStop = function () { window.clearInterval(lTimer); lTimer = null; };
    var lStart = function () { if (!lTimer && !lPaused && !document.hidden) lTimer = window.setInterval(function () { turn(1); }, 5000); };
    zone.querySelector('[data-logos-prev]').addEventListener('click', function () { turn(-1); lStop(); lStart(); });
    zone.querySelector('[data-logos-next]').addEventListener('click', function () { turn(1); lStop(); lStart(); });
    lToggle.addEventListener('click', function () {
      lPaused = !lPaused;
      lToggle.setAttribute('aria-pressed', String(lPaused));
      lToggle.setAttribute('aria-label', lPaused ? T.logosPlay : T.logosPause);
      if (lPaused) lStop(); else lStart();
    });
    // Pause temporaire au survol des logos et quand le focus est dans la section
    logos.addEventListener('mouseenter', lStop);
    logos.addEventListener('mouseleave', lStart);
    zone.addEventListener('focusin', lStop);
    zone.addEventListener('focusout', function (e) { if (!zone.contains(e.relatedTarget)) lStart(); });
    document.addEventListener('visibilitychange', function () { if (document.hidden) lStop(); else lStart(); });
    lStart();
  }

  // ---------- Galeries : masonry + chargement par lots de 6 (au défilement, ou bouton « Afficher plus ») ----------
  // Grille à rangées de 2 px : chaque photo s'étend sur le nombre de rangées correspondant à son format (attributs
  // width/height), placée dans l'ordre, de gauche à droite : les photos déjà vues ne bougent pas quand un lot arrive.
  // Les photos du lot suivant sont en display:none, donc leurs images ne sont pas téléchargées avant d'être affichées.
  var BATCH = 6;
  document.querySelectorAll('.gallery, .photo-grid').forEach(function (grid) {
    var items = Array.prototype.slice.call(grid.querySelectorAll('.gallery__item'));
    var more = document.createElement('button');
    more.type = 'button';
    more.className = 'btn btn--secondary gallery-more';
    grid.insertAdjacentElement('afterend', more);
    var limit = BATCH;
    var layout = function () {
      var gap = parseFloat(window.getComputedStyle(grid).columnGap) || 8;
      items.forEach(function (it) {
        if (it.hidden || it.classList.contains('is-deferred')) return;
        var img = it.querySelector('img');
        var ratio = (+img.getAttribute('height') || 3) / (+img.getAttribute('width') || 4);
        it.style.gridRowEnd = 'span ' + Math.ceil((it.getBoundingClientRect().width * ratio + gap) / 2);
      });
    };
    var render = function (fresh) {
      var visible = items.filter(function (it) { return !it.hidden; });
      visible.forEach(function (it, i) {
        var deferred = i >= limit;
        var appearing = fresh && !deferred && it.classList.contains('is-deferred');
        it.classList.toggle('is-deferred', deferred);
        if (appearing && !calmMotion) {
          it.classList.add('reveal');
          window.requestAnimationFrame(function () { window.requestAnimationFrame(function () { it.classList.add('is-in'); }); });
          window.setTimeout(function () { it.classList.remove('reveal', 'is-in'); }, 700);
        }
      });
      var rest = visible.length - Math.min(limit, visible.length);
      more.hidden = rest <= 0;
      more.textContent = T.morePhotos + ' (' + rest + ')';
      layout();
    };
    var loadMore = function () { limit += BATCH; render(true); };
    more.addEventListener('click', loadMore);
    // Au défilement : lot suivant quand le bouton approche du bas de l'écran (jamais au chargement)
    var scrolled = false;
    window.addEventListener('scroll', function () {
      if (scrolled || more.hidden) return;
      scrolled = true;
      window.requestAnimationFrame(function () {
        scrolled = false;
        if (!more.hidden && more.getBoundingClientRect().top < window.innerHeight + 120) loadMore();
      });
    }, { passive: true });
    grid.addEventListener('filtered', function () { limit = BATCH; render(false); });
    var resizeT = null;
    window.addEventListener('resize', function () { window.clearTimeout(resizeT); resizeT = window.setTimeout(layout, 120); });
    grid.classList.add('is-masonry');
    render(false);
  });

  // ---------- Visionneuse de photos (galeries des espaces, photothèque) ----------
  var lightbox = document.getElementById('lightbox');
  if (lightbox && typeof lightbox.showModal === 'function') {
    var lbImg = lightbox.querySelector('.lightbox__img');
    var lbCaption = lightbox.querySelector('.lightbox__caption');
    var lbCount = lightbox.querySelector('.lightbox__count');
    var lbItems = [];
    var lbIndex = 0;
    var lbOpener = null;
    var render = function () {
      var item = lbItems[lbIndex];
      lbImg.src = item.getAttribute('href');
      lbImg.alt = item.getAttribute('data-caption');
      lbCaption.textContent = item.getAttribute('data-caption');
      lbCount.textContent = (lbIndex + 1) + ' / ' + lbItems.length;
    };
    var closeLightbox = function () {
      if (lightbox.open) lightbox.close();
      if (lbOpener) lbOpener.focus();
    };
    document.querySelectorAll('[data-lightbox]').forEach(function (gallery) {
      gallery.addEventListener('click', function (e) {
        var link = e.target.closest('[data-lightbox-item]');
        if (!link) return;
        e.preventDefault();
        // Seules les photos visibles (selon les filtres) font partie du parcours
        lbItems = Array.prototype.filter.call(gallery.querySelectorAll('[data-lightbox-item]'), function (el) { return !el.hidden; });
        lbIndex = lbItems.indexOf(link);
        lbOpener = link;
        render();
        lightbox.showModal();
      });
    });
    lightbox.querySelector('.lightbox__prev').addEventListener('click', function () { lbIndex = (lbIndex - 1 + lbItems.length) % lbItems.length; render(); });
    lightbox.querySelector('.lightbox__next').addEventListener('click', function () { lbIndex = (lbIndex + 1) % lbItems.length; render(); });
    lightbox.querySelector('.lightbox__close').addEventListener('click', closeLightbox);
    lightbox.addEventListener('cancel', function (e) { e.preventDefault(); closeLightbox(); });
    lightbox.addEventListener('click', function (e) { if (e.target === lightbox) closeLightbox(); });
    lightbox.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowLeft') { lbIndex = (lbIndex - 1 + lbItems.length) % lbItems.length; render(); }
      if (e.key === 'ArrowRight') { lbIndex = (lbIndex + 1) % lbItems.length; render(); }
    });
  }

  // ---------- Formulaire de devis ----------
  var form = document.querySelector('[data-quote-form]');
  if (!form) return;

  // Pré-sélection de l'espace : contact-devis.html?espace=hall
  var params = new URLSearchParams(window.location.search);
  var espace = document.getElementById('espace');
  if (espace && params.get('espace')) espace.value = params.get('espace');

  // La date de fin ne peut pas précéder la date de début
  var debut = document.getElementById('date-debut');
  var fin = document.getElementById('date-fin');
  if (debut && fin) debut.addEventListener('change', function () { fin.min = debut.value; });

  var setError = function (input, show) {
    var error = document.getElementById(input.id + '-error');
    input.setAttribute('aria-invalid', String(show));
    if (error) {
      error.hidden = !show;
      if (show) input.setAttribute('aria-describedby', error.id);
      else input.removeAttribute('aria-describedby');
    }
  };
  var required = form.querySelectorAll('[required]');
  required.forEach(function (input) {
    input.addEventListener(input.type === 'checkbox' || input.tagName === 'SELECT' ? 'change' : 'blur', function () {
      if (input.getAttribute('aria-invalid') === 'true' || input.value) setError(input, !input.checkValidity());
    });
  });

  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var firstInvalid = null;
    required.forEach(function (input) {
      var invalid = !input.checkValidity();
      setError(input, invalid);
      if (invalid && !firstInvalid) firstInvalid = input;
    });
    if (firstInvalid) { firstInvalid.focus(); return; }
    // Maquette : envoi simulé. Le traitement réel est à brancher sur un webform Drupal.
    var ok = document.getElementById('devis-ok');
    // Récapitulatif de la demande dans le message de succès
    var recap = ok.querySelector('[data-recap]');
    if (recap) {
      var opt = function (id) { var el = document.getElementById(id); return el && el.value ? el.options[el.selectedIndex].text : T.recap.none; };
      var d1 = debut && debut.value, d2 = fin && fin.value;
      var dates = d1 ? new Date(d1).toLocaleDateString(document.documentElement.lang) + (d2 ? T.recap.to + new Date(d2).toLocaleDateString(document.documentElement.lang) : '') : T.recap.none;
      recap.replaceChildren();
      [[T.recap.type, opt('type')], [T.recap.espace, opt('espace')], [T.recap.dates, dates]].forEach(function (row) {
        var div = document.createElement('div');
        var dt = document.createElement('dt'); dt.textContent = row[0];
        var dd = document.createElement('dd'); dd.textContent = row[1];
        div.append(dt, dd); recap.appendChild(div);
      });
    }
    form.hidden = true;
    ok.hidden = false;
    ok.focus();
  });
})();
