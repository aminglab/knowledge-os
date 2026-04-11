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
    createSection,
    createLinksBlock,
    renderLineageRail,
    renderRouteCard,
    renderStandardCard,
    renderStatusCard,
    renderTimelineItem,
    renderSourceItem,
    renderSourceGroup,
    renderFooterCard,
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
    data.statusCards.forEach((cardData) => grid.appendChild(renderStatusCard(cardData)));
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
        grid.appendChild(renderStandardCard(cardData));
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
    data.timeline.forEach((item) => timeline.appendChild(renderTimelineItem(item)));
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
      node.appendChild(
        renderSourceGroup({
          title: groupData.title,
          intro: groupData.intro,
          items: groupData.items,
          renderItem: (item) => renderSourceItem(item, { toneClass: classifySourceTone(item) }),
        })
      );
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
    footer.appendChild(renderFooterCard(data.footer));
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
