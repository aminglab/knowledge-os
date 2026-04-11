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

  const CASE_SECTION_OPTIONS = Object.freeze({
    'Current visible judgment': {
      id: 'current-visible-judgment',
      tone: 'judgment',
      kicker: 'Public judgment',
      navLabel: 'Judgment',
    },
    'Why this case matters': {
      tone: 'context',
      kicker: 'Case frame',
      navLabel: 'Why it matters',
    },
    'Current object neighborhoods': {
      tone: 'neighborhoods',
      kicker: 'Object layer',
      navLabel: 'Neighborhoods',
    },
    'Public claim and source routes': {
      tone: 'routes',
      kicker: 'Public layer',
      navLabel: 'Public routes',
    },
    Timeline: {
      tone: 'timeline',
      kicker: 'Case chronology',
      navLabel: 'Timeline',
    },
    'Canonical source ids': {
      tone: 'sources',
      kicker: 'Source layer',
      navLabel: 'Sources',
    },
    'Reading path': {
      tone: 'reading',
      kicker: 'Downstream route',
      navLabel: 'Reading path',
    },
  });

  const ROUTE_SECTION_TITLE = 'Public claim and source routes';
  const SOURCE_GROUP_KICKER = 'Grouped source surface';
  const DEFAULT_READING_PATH_INTRO =
    'The page is a release surface, but it still points back to the governed object layer.';
  const SOURCE_GROUP_DEFINITIONS = [
    {
      key: 'public-circulation',
      ids: ['Early_public_amplification_context', 'TED_Corrections_2017'],
      title: 'Public circulation and retreat context',
      intro:
        'These sources show how the case moved through amplification, public correction, and narrower retreat rather than staying confined to one journal article.',
    },
    {
      key: 'core-record',
      ids: [],
      title: 'Core scientific record',
      intro:
        'These sources carry the original publication, the major empirical challenge, the internal retreat, and the methodological attack that shaped the main contested judgment surface.',
    },
  ];

  const section = (title, intro, options = {}) =>
    createSection({ title, intro, options, sectionAnchors });

  const getSectionOptions = (title) => CASE_SECTION_OPTIONS[title] || {};

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

  const classifySourceTone = (item) => {
    if (['Ranehill_et_al_2015', 'Dana_Carney_2016_statement', 'Simmons_Simonsohn_2016'].includes(item.id)) {
      return 'source-item-challenge';
    }
    if (['Early_public_amplification_context', 'TED_Corrections_2017'].includes(item.id)) {
      return 'source-item-context';
    }
    return 'source-item-support';
  };

  const buildSourceGroups = (sources) => {
    const sourcesById = new Map(sources.map((item) => [item.id, item]));
    return SOURCE_GROUP_DEFINITIONS.map((group) => {
      const items = group.ids.length
        ? group.ids.map((id) => sourcesById.get(id)).filter(Boolean)
        : sources.filter((item) => !SOURCE_GROUP_DEFINITIONS[0].ids.includes(item.id));

      return {
        key: group.key,
        title: group.title,
        intro: group.intro,
        items,
      };
    }).filter((group) => group.items.length > 0);
  };

  const renderMountedSection = ({ title, intro, mount }) => {
    const node = section(title, intro, getSectionOptions(title));
    const mounted = mount();
    if (mounted) {
      node.appendChild(mounted);
    }
    app.appendChild(node);
  };

  const renderLinkCollectionSection = ({ title, intro, links, fallbackIntro = '' }) => {
    renderMountedSection({
      title,
      intro: intro || fallbackIntro,
      mount: () => createLinksBlock(links || []),
    });
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

  const renderStatusSection = () => {
    const title = 'Current visible judgment';
    const node = section(title, data.judgmentIntro || '', getSectionOptions(title));

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

  const renderSnapshotSections = () => {
    data.sections.forEach((block) => {
      renderMountedSection({
        title: block.title,
        intro: block.intro,
        mount: () => {
          const gridClass = block.cards.length >= 3 ? 'grid grid-3' : 'grid grid-2';
          const grid = el('div', `${gridClass}${block.title === ROUTE_SECTION_TITLE ? ' route-grid' : ''}`);

          block.cards.forEach((cardData) => {
            const card = block.title === ROUTE_SECTION_TITLE ? renderRouteCard(cardData) : renderStandardCard(cardData);
            grid.appendChild(card);
          });

          return grid;
        },
      });
    });
  };

  const renderTimelineSection = () => {
    renderMountedSection({
      title: 'Timeline',
      intro: 'A compact chronological reading path for the case.',
      mount: () => {
        const timeline = el('div', 'timeline');
        data.timeline.forEach((item) => timeline.appendChild(renderTimelineItem(item)));
        return timeline;
      },
    });
  };

  const renderSourcesSection = () => {
    renderMountedSection({
      title: 'Canonical source ids',
      intro: 'The page keeps the source layer visible and now routes each source card back to its own metadata entry and the objects that use it.',
      mount: () => {
        const fragment = document.createDocumentFragment();
        buildSourceGroups(data.sources).forEach((groupData) => {
          fragment.appendChild(
            renderSourceGroup({
              title: groupData.title,
              intro: groupData.intro,
              items: groupData.items,
              kicker: SOURCE_GROUP_KICKER,
              renderItem: (item) => renderSourceItem(item, { toneClass: classifySourceTone(item) }),
            })
          );
        });
        return fragment;
      },
    });
  };

  const renderReadingPathSection = () => {
    renderLinkCollectionSection({
      title: 'Reading path',
      intro: data.readingPathIntro,
      links: data.readingPath,
      fallbackIntro: DEFAULT_READING_PATH_INTRO,
    });
  };

  const renderFooter = () => {
    if (!footer || !data.footer) return;
    footer.appendChild(renderFooterCard(data.footer));
  };

  renderHero();
  renderStatusSection();
  renderSnapshotSections();
  renderTimelineSection();
  renderSourcesSection();
  renderReadingPathSection();
  renderQuickNav();
  setupScrollSpy();
  renderFooter();
})();
