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

  const renderSourceLinksBlock = (labelText, items = []) => {
    if (!Array.isArray(items) || !items.length) return null;
    const block = el('div', 'source-links-block');
    block.appendChild(el('div', 'source-links-label', labelText));
    const links = createLinksBlock(items);
    if (links) block.appendChild(links);
    return block;
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
    splitSourceLinks,
    renderSourceLinksBlock,
  };
})();
