(function () {
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

  const createSection = ({ title, intro, options = {}, sectionAnchors = [] }) => {
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

    if (intro) {
      node.appendChild(el('p', 'section-intro', intro));
    }

    sectionAnchors.push({
      id,
      label: options.navLabel || title,
    });

    return node;
  };

  const createMetaRow = (items = [], kind = 'status') => {
    if (!Array.isArray(items) || !items.length) return null;
    const row = el('div', 'meta-row');
    items.forEach((item) => row.appendChild(el('span', badgeClass(kind), item)));
    return row;
  };

  const createLinksBlock = (items = [], options = {}) => {
    if (!Array.isArray(items) || !items.length) return null;
    const wrapperClass = options.wrapperClass || 'object-links';
    const linkClass = options.linkClass || 'object-link';
    const wrap = el('div', wrapperClass);
    items.forEach((item) => wrap.appendChild(link(item, linkClass)));
    return wrap;
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

  const renderRouteCard = (cardData) => {
    const cardClasses = ['card', 'route-card'];
    if (cardData.kind === 'support') {
      cardClasses.push('route-card-source');
    } else {
      cardClasses.push('route-card-claim');
    }

    const card = el('article', cardClasses.join(' '));
    const meta = createMetaRow(cardData.badges || [], cardData.kind || 'status');
    if (meta) card.appendChild(meta);
    card.appendChild(el('h3', '', cardData.title));
    card.appendChild(el('p', '', cardData.body));
    const links = createLinksBlock(cardData.links || []);
    if (links) card.appendChild(links);
    return card;
  };

  const renderStandardCard = (cardData) => {
    const card = el('article', 'card');
    const meta = createMetaRow(cardData.badges || [], cardData.kind || 'status');
    if (meta) card.appendChild(meta);
    card.appendChild(el('h3', '', cardData.title));
    card.appendChild(el('p', '', cardData.body));
    const links = createLinksBlock(cardData.links || []);
    if (links) card.appendChild(links);
    return card;
  };

  const renderStatusCard = (cardData) => {
    const card = el('article', 'card card-emphasis card-claim-status');
    const meta = createMetaRow(cardData.badges || [], 'status');
    if (meta) card.appendChild(meta);
    card.appendChild(el('h3', '', cardData.title));
    card.appendChild(el('p', '', cardData.summary));
    card.appendChild(el('p', 'card-state', `Current state: ${cardData.status}`));
    const links = createLinksBlock(cardData.links || []);
    if (links) card.appendChild(links);
    return card;
  };

  const renderTimelineItem = (item) => {
    const wrap = el('article', 'timeline-item');
    wrap.appendChild(el('div', 'timeline-year', item.year));
    wrap.appendChild(el('h3', '', item.title));
    wrap.appendChild(el('p', '', item.body));
    return wrap;
  };

  const defaultSourceLinkRoleClassifier = (entry = {}) => {
    if (typeof entry.href !== 'string') return 'object_touch';
    if (entry.href.startsWith('../sources/') || entry.href.startsWith('../references-metadata-v1.md#')) {
      return 'source_route';
    }
    return 'object_touch';
  };

  const splitSourceLinks = (links = [], classifyLinkRole = defaultSourceLinkRoleClassifier) => {
    const sourceRoutes = [];
    const objectTouches = [];

    links.forEach((entry) => {
      const role = classifyLinkRole(entry);
      if (role === 'source_route') {
        sourceRoutes.push(entry);
      } else {
        objectTouches.push(entry);
      }
    });

    return { sourceRoutes, objectTouches };
  };

  const renderSourceLinksBlock = (labelText, items = []) => {
    if (!Array.isArray(items) || !items.length) return null;
    const block = el('div', 'source-links-block');
    block.appendChild(el('div', 'source-links-label', labelText));
    const links = createLinksBlock(items);
    if (links) block.appendChild(links);
    return block;
  };

  const renderSourceItem = (item, options = {}) => {
    const toneClass = options.toneClass || '';
    const classifyLinkRole = options.classifyLinkRole || defaultSourceLinkRoleClassifier;
    const source = el('article', `source-item ${toneClass}`.trim());
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

    const { sourceRoutes, objectTouches } = splitSourceLinks(item.links || [], classifyLinkRole);
    const sourceRoutesBlock = renderSourceLinksBlock('Source routes', sourceRoutes);
    if (sourceRoutesBlock) source.appendChild(sourceRoutesBlock);
    const objectTouchesBlock = renderSourceLinksBlock('Touches objects', objectTouches);
    if (objectTouchesBlock) source.appendChild(objectTouchesBlock);

    return source;
  };

  const renderSourceGroup = ({ title, intro, items = [], renderItem, kicker = 'Grouped source surface' }) => {
    const group = el('div', 'source-group');
    const header = el('div', 'source-group-header');
    header.appendChild(el('div', 'source-group-kicker', kicker));
    header.appendChild(el('h3', 'source-group-title', title));
    header.appendChild(el('p', 'source-group-intro', intro));
    group.appendChild(header);

    const list = el('div', 'source-group-list');
    items.forEach((item) => list.appendChild(renderItem(item)));
    group.appendChild(list);
    return group;
  };

  const renderFooterCard = (footerData) => {
    const card = el('div', 'footer-card');
    if (footerData.eyebrow) {
      card.appendChild(el('div', 'footer-eyebrow', footerData.eyebrow));
    }
    if (footerData.title) {
      card.appendChild(el('h2', 'footer-title', footerData.title));
    }
    if (footerData.body) {
      card.appendChild(el('p', 'footer-copy', footerData.body));
    }
    const meta = createMetaRow(footerData.badges || [], 'status');
    if (meta) card.appendChild(meta);
    const links = createLinksBlock(footerData.links || []);
    if (links) card.appendChild(links);
    return card;
  };

  window.KnowledgeOSRendererPrimitives = {
    el,
    link,
    badgeClass,
    createSection,
    createMetaRow,
    createLinksBlock,
    renderLineageRail,
    renderRouteCard,
    renderStandardCard,
    renderStatusCard,
    renderTimelineItem,
    defaultSourceLinkRoleClassifier,
    splitSourceLinks,
    renderSourceLinksBlock,
    renderSourceItem,
    renderSourceGroup,
    renderFooterCard,
  };
})();
