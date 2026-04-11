(function () {
  const data = window.POWER_POSING_PAGE_DATA;
  const hero = document.getElementById('hero');
  const pageNav = document.getElementById('page-nav');
  const app = document.getElementById('app');
  const footer = document.getElementById('footer');

  if (!data || !hero || !app) {
    return;
  }

  const sectionAnchors = [];
  const navLinkById = new Map();

  const el = (tag, className, text) => {
    const node = document.createElement(tag);
    if (className) node.className = className;
    if (typeof text === 'string') node.textContent = text;
    return node;
  };

  const link = ({ label, href }, className = 'object-link') => {
    const a = el('a', className, label);
    a.href = href;
    return a;
  };

  const badgeClass = (kind) => {
    if (kind === 'dissent') return 'badge badge-dissent';
    if (kind === 'support') return 'badge badge-support';
    return 'badge badge-status';
  };

  const slugify = (text) =>
    text
      .toLowerCase()
      .replace(/[^a-z0-9]+/g, '-')
      .replace(/^-+|-+$/g, '');

  const setActiveNav = (activeId) => {
    navLinkById.forEach((node, id) => {
      const isActive = id === activeId;
      node.classList.toggle('is-active', isActive);
      if (isActive) {
        node.setAttribute('aria-current', 'true');
      } else {
        node.removeAttribute('aria-current');
      }
    });
  };

  const section = (title, intro, options = {}) => {
    const classes = ['section'];
    if (options.tone) {
      classes.push(`section-${options.tone}`);
    }
    const node = el('section', classes.join(' '));
    const id = options.id || slugify(title);
    node.id = id;

    const header = el('div', 'section-header');
    if (options.kicker) {
      header.appendChild(el('div', 'section-kicker', options.kicker));
    }
    header.appendChild(el('h2', '', title));
    node.appendChild(header);

    if (intro) node.appendChild(el('p', 'section-intro', intro));

    sectionAnchors.push({
      id,
      label: options.navLabel || title,
    });

    return node;
  };

  const renderLineageRail = (cards) => {
    if (!Array.isArray(cards) || cards.length < 2) return null;

    const rail = el('div', 'lineage-rail');

    cards.forEach((cardData, index) => {
      const stop = el('div', 'lineage-stop');
      stop.appendChild(el('div', 'lineage-stop-label', cardData.title));
      stop.appendChild(el('div', 'lineage-stop-state', cardData.status));
      rail.appendChild(stop);

      if (index < cards.length - 1) {
        const connector = el('div', 'lineage-connector');
        connector.appendChild(el('span', 'lineage-connector-line'));
        connector.appendChild(el('span', 'lineage-connector-label', 'narrows into descendant path'));
        rail.appendChild(connector);
      }
    });

    return rail;
  };

  const classifySourceGroup = (item) => {
    if (['Early_public_amplification_context', 'TED_Corrections_2017'].includes(item.id)) {
      return {
        key: 'public-circulation',
        title: 'Public circulation and retreat context',
        intro:
          'These sources show how the case moved through amplification, public correction, and narrower retreat rather than staying confined to one journal article.',
      };
    }

    return {
      key: 'core-record',
      title: 'Core scientific record',
      intro:
        'These sources carry the original publication, the major empirical challenge, the internal retreat, and the methodological attack that shaped the main contested judgment surface.',
    };
  };

  const classifySourceTone = (item) => {
    if (['Ranehill_et_al_2015', 'Dana_Carney_2016_statement', 'Simmons_Simonsohn_2016'].includes(item.id)) {
      return 'source-item-challenge';
    }
    if (['Early_public_amplification_context', 'TED_Corrections_2017'].includes(item.id)) {
      return 'source-item-context';
    }
    return 'source-item-support';
  };

  const splitSourceLinks = (links = []) => {
    const sourceRoutes = [];
    const objectTouches = [];

    links.forEach((entry) => {
      if (entry.label.startsWith('Open source')) {
        sourceRoutes.push(entry);
      } else {
        objectTouches.push(entry);
      }
    });

    return { sourceRoutes, objectTouches };
  };

  const renderHero = () => {
    const card = el('div', 'hero-card');
    card.appendChild(el('div', 'eyebrow', 'Knowledge OS · Living Knowledge Case'));
    if (data.shortTitle) {
      card.appendChild(el('div', 'eyebrow', data.shortTitle));
    }
    card.appendChild(el('h1', '', data.title));
    card.appendChild(el('p', '', data.description));

    const links = el('div', 'hero-links');
    data.links.forEach((item) => links.appendChild(link(item, 'link-chip')));
    card.appendChild(links);
    hero.appendChild(card);
  };

  const renderQuickNav = () => {
    if (!pageNav || !sectionAnchors.length) return;

    const shell = el('div', 'page-nav-card');
    shell.appendChild(el('div', 'page-nav-kicker', 'On this page'));
    const links = el('div', 'page-nav-links');

    sectionAnchors.forEach((item) => {
      const navLink = link({ label: item.label, href: `#${item.id}` }, 'page-nav-link');
      navLink.dataset.sectionId = item.id;
      navLink.addEventListener('click', () => setActiveNav(item.id));
      navLinkById.set(item.id, navLink);
      links.appendChild(navLink);
    });

    shell.appendChild(links);
    pageNav.appendChild(shell);
    if (sectionAnchors.length) {
      setActiveNav(sectionAnchors[0].id);
    }
  };

  const setupScrollSpy = () => {
    if (!navLinkById.size || !sectionAnchors.length) {
      return;
    }

    const sections = sectionAnchors
      .map((item) => document.getElementById(item.id))
      .filter(Boolean);

    if (!sections.length) {
      return;
    }

    const update = () => {
      const threshold = window.scrollY + 180;
      let activeId = sections[0].id;

      sections.forEach((node) => {
        if (node.offsetTop <= threshold) {
          activeId = node.id;
        }
      });

      setActiveNav(activeId);
    };

    update();
    window.addEventListener('scroll', update, { passive: true });
    window.addEventListener('resize', update);
  };

  const renderStatusCards = () => {
    const node = section('Current visible judgment', data.judgmentIntro || '', {
      id: 'current-visible-judgment',
      tone: 'judgment',
      kicker: 'Public judgment',
      navLabel: 'Judgment',
    });
    if (data.judgmentLinks && data.judgmentLinks.length) {
      const links = el('div', 'object-links');
      data.judgmentLinks.forEach((item) => links.appendChild(link(item)));
      node.appendChild(links);
    }

    const lineageRail = renderLineageRail(data.statusCards);
    if (lineageRail) {
      node.appendChild(lineageRail);
    }

    const grid = el('div', 'grid grid-2');

    data.statusCards.forEach((cardData) => {
      const card = el('article', 'card card-emphasis card-claim-status');
      const meta = el('div', 'meta-row');
      cardData.badges.forEach((item) => meta.appendChild(el('span', 'badge badge-status', item)));
      card.appendChild(meta);
      card.appendChild(el('h3', '', cardData.title));
      card.appendChild(el('p', '', cardData.summary));
      card.appendChild(el('p', 'card-state', `Current state: ${cardData.status}`));

      const links = el('div', 'object-links');
      cardData.links.forEach((item) => links.appendChild(link(item)));
      card.appendChild(links);
      grid.appendChild(card);
    });

    node.appendChild(grid);
    app.appendChild(node);
  };

  const renderSections = () => {
    data.sections.forEach((block) => {
      const toneMap = {
        'Why this case matters': { tone: 'context', kicker: 'Case frame', navLabel: 'Why it matters' },
        'Current object neighborhoods': { tone: 'neighborhoods', kicker: 'Object layer', navLabel: 'Neighborhoods' },
        'Public claim and source routes': { tone: 'routes', kicker: 'Public layer', navLabel: 'Public routes' },
      };
      const options = toneMap[block.title] || {};
      const node = section(block.title, block.intro, options);
      const gridClass = block.cards.length >= 3 ? 'grid grid-3' : 'grid grid-2';
      const grid = el('div', `${gridClass}${block.title === 'Public claim and source routes' ? ' route-grid' : ''}`);

      block.cards.forEach((cardData) => {
        const cardClasses = ['card'];
        if (block.title === 'Public claim and source routes') {
          cardClasses.push('route-card');
          if (cardData.kind === 'support') {
            cardClasses.push('route-card-source');
          } else {
            cardClasses.push('route-card-claim');
          }
        }

        const card = el('article', cardClasses.join(' '));
        const meta = el('div', 'meta-row');
        (cardData.badges || []).forEach((item) => meta.appendChild(el('span', badgeClass(cardData.kind), item)));
        if (meta.childNodes.length > 0) card.appendChild(meta);
        card.appendChild(el('h3', '', cardData.title));
        card.appendChild(el('p', '', cardData.body));
        if (cardData.links && cardData.links.length) {
          const links = el('div', 'object-links');
          cardData.links.forEach((item) => links.appendChild(link(item)));
          card.appendChild(links);
        }
        grid.appendChild(card);
      });

      node.appendChild(grid);
      app.appendChild(node);
    });
  };

  const renderTimeline = () => {
    const node = section('Timeline', 'A compact chronological reading path for the case.', {
      tone: 'timeline',
      kicker: 'Case chronology',
      navLabel: 'Timeline',
    });
    const timeline = el('div', 'timeline');

    data.timeline.forEach((item) => {
      const wrap = el('article', 'timeline-item');
      wrap.appendChild(el('div', 'timeline-year', item.year));
      wrap.appendChild(el('h3', '', item.title));
      wrap.appendChild(el('p', '', item.body));
      timeline.appendChild(wrap);
    });

    node.appendChild(timeline);
    app.appendChild(node);
  };

  const renderSources = () => {
    const node = section(
      'Canonical source ids',
      'The page keeps the source layer visible and now routes each source card back to its own metadata entry and the objects that use it.',
      {
        tone: 'sources',
        kicker: 'Source layer',
        navLabel: 'Sources',
      }
    );

    const grouped = [];
    const groupByKey = new Map();

    data.sources.forEach((item) => {
      const groupMeta = classifySourceGroup(item);
      if (!groupByKey.has(groupMeta.key)) {
        const record = { ...groupMeta, items: [] };
        groupByKey.set(groupMeta.key, record);
        grouped.push(record);
      }
      groupByKey.get(groupMeta.key).items.push(item);
    });

    grouped.forEach((groupData) => {
      const group = el('div', 'source-group');
      const header = el('div', 'source-group-header');
      header.appendChild(el('div', 'source-group-kicker', 'Grouped source surface'));
      header.appendChild(el('h3', 'source-group-title', groupData.title));
      header.appendChild(el('p', 'source-group-intro', groupData.intro));
      group.appendChild(header);

      const list = el('div', 'source-group-list');

      groupData.items.forEach((item) => {
        const source = el('article', `source-item ${classifySourceTone(item)}`);
        source.appendChild(el('div', 'source-id', item.id));
        if (item.title) {
          source.appendChild(el('h3', '', item.title));
        }
        if (item.badges && item.badges.length) {
          const meta = el('div', 'meta-row');
          item.badges.forEach((badge) => meta.appendChild(el('span', 'badge badge-status', badge)));
          source.appendChild(meta);
        }
        if (item.role) {
          source.appendChild(el('p', '', item.role));
        }
        if (item.locator) {
          source.appendChild(el('p', 'source-locator', `Canonical locator: ${item.locator}`));
        }
        if (item.usage) {
          source.appendChild(el('p', '', `Object usage: ${item.usage}`));
        }

        const { sourceRoutes, objectTouches } = splitSourceLinks(item.links || []);

        if (sourceRoutes.length) {
          const routeBlock = el('div', 'source-links-block');
          routeBlock.appendChild(el('div', 'source-links-label', 'Source routes'));
          const links = el('div', 'object-links');
          sourceRoutes.forEach((entry) => links.appendChild(link(entry)));
          routeBlock.appendChild(links);
          source.appendChild(routeBlock);
        }

        if (objectTouches.length) {
          const objectBlock = el('div', 'source-links-block');
          objectBlock.appendChild(el('div', 'source-links-label', 'Touches objects'));
          const links = el('div', 'object-links');
          objectTouches.forEach((entry) => links.appendChild(link(entry)));
          objectBlock.appendChild(links);
          source.appendChild(objectBlock);
        }

        list.appendChild(source);
      });

      group.appendChild(list);
      node.appendChild(group);
    });

    app.appendChild(node);
  };

  const renderReadingPath = () => {
    const node = section(
      'Reading path',
      data.readingPathIntro || 'The page is a release surface, but it still points back to the governed object layer.',
      {
        tone: 'reading',
        kicker: 'Downstream route',
        navLabel: 'Reading path',
      }
    );
    const links = el('div', 'object-links');
    data.readingPath.forEach((item) => links.appendChild(link(item)));
    node.appendChild(links);
    app.appendChild(node);
  };

  const renderFooter = () => {
    if (!footer || !data.footer) return;

    const card = el('div', 'footer-card');
    if (data.footer.eyebrow) {
      card.appendChild(el('div', 'footer-eyebrow', data.footer.eyebrow));
    }
    if (data.footer.title) {
      card.appendChild(el('h2', 'footer-title', data.footer.title));
    }
    if (data.footer.body) {
      card.appendChild(el('p', 'footer-copy', data.footer.body));
    }
    if (data.footer.badges && data.footer.badges.length) {
      const meta = el('div', 'meta-row');
      data.footer.badges.forEach((item) => meta.appendChild(el('span', 'badge badge-status', item)));
      card.appendChild(meta);
    }
    if (data.footer.links && data.footer.links.length) {
      const links = el('div', 'object-links');
      data.footer.links.forEach((item) => links.appendChild(link(item)));
      card.appendChild(links);
    }
    footer.appendChild(card);
  };

  renderHero();
  renderStatusCards();
  renderSections();
  renderTimeline();
  renderSources();
  renderReadingPath();
  renderQuickNav();
  setupScrollSpy();
  renderFooter();
})();
