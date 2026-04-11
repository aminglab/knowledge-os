(function () {
  const data = window.POWER_POSING_PAGE_DATA;
  const primitives = window.KnowledgeOSRendererPrimitives;
  const hero = document.getElementById('hero');
  const pageNav = document.getElementById('page-nav');
  const app = document.getElementById('app');
  const footer = document.getElementById('footer');

  if (!data || !primitives || !hero || !app) {
    return;
  }

  const {
    el,
    link,
    badgeClass,
    createSection,
    createMetaRow,
    createLinksBlock,
    renderLineageRail,
    renderRouteCard,
    splitSourceLinks,
    renderSourceLinksBlock,
  } = primitives;

  const sectionAnchors = [];
  const navLinkById = new Map();

  const section = (title, intro, options = {}) =>
    createSection({ title, intro, options, sectionAnchors });

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

  const renderHero = () => {
    const card = el('div', 'hero-card');
    card.appendChild(el('div', 'eyebrow', 'Knowledge OS · Living Knowledge Case'));
    if (data.shortTitle) {
      card.appendChild(el('div', 'eyebrow', data.shortTitle));
    }
    card.appendChild(el('h1', '', data.title));
    card.appendChild(el('p', '', data.description));

    const links = createLinksBlock(data.links, { wrapperClass: 'hero-links', linkClass: 'link-chip' });
    if (links) card.appendChild(links);
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

    const judgmentLinks = createLinksBlock(data.judgmentLinks || []);
    if (judgmentLinks) node.appendChild(judgmentLinks);

    const lineageRail = renderLineageRail(data.statusCards);
    if (lineageRail) {
      node.appendChild(lineageRail);
    }

    const grid = el('div', 'grid grid-2');

    data.statusCards.forEach((cardData) => {
      const card = el('article', 'card card-emphasis card-claim-status');
      const meta = createMetaRow(cardData.badges || [], 'status');
      if (meta) card.appendChild(meta);
      card.appendChild(el('h3', '', cardData.title));
      card.appendChild(el('p', '', cardData.summary));
      card.appendChild(el('p', 'card-state', `Current state: ${cardData.status}`));

      const links = createLinksBlock(cardData.links || []);
      if (links) card.appendChild(links);
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
        if (block.title === 'Public claim and source routes') {
          grid.appendChild(renderRouteCard(cardData));
          return;
        }

        const card = el('article', 'card');
        const meta = createMetaRow(cardData.badges || [], cardData.kind || 'status');
        if (meta) card.appendChild(meta);
        card.appendChild(el('h3', '', cardData.title));
        card.appendChild(el('p', '', cardData.body));
        const links = createLinksBlock(cardData.links || []);
        if (links) card.appendChild(links);
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
        const meta = createMetaRow(item.badges || [], 'status');
        if (meta) source.appendChild(meta);
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
        const sourceRoutesBlock = renderSourceLinksBlock('Source routes', sourceRoutes);
        if (sourceRoutesBlock) source.appendChild(sourceRoutesBlock);
        const objectTouchesBlock = renderSourceLinksBlock('Touches objects', objectTouches);
        if (objectTouchesBlock) source.appendChild(objectTouchesBlock);

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
    const links = createLinksBlock(data.readingPath || []);
    if (links) node.appendChild(links);
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
    const meta = createMetaRow(data.footer.badges || [], 'status');
    if (meta) card.appendChild(meta);
    const links = createLinksBlock(data.footer.links || []);
    if (links) card.appendChild(links);
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
