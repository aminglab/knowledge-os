(function () {
  const data = window.POWER_POSING_PAGE_DATA;
  const hero = document.getElementById('hero');
  const app = document.getElementById('app');

  if (!data || !hero || !app) {
    return;
  }

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

  const section = (title, intro) => {
    const node = el('section', 'section');
    node.appendChild(el('h2', '', title));
    if (intro) node.appendChild(el('p', 'section-intro', intro));
    return node;
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

  const renderStatusCards = () => {
    const node = section('Current visible judgment', data.judgmentIntro || '');
    if (data.judgmentLinks && data.judgmentLinks.length) {
      const links = el('div', 'object-links');
      data.judgmentLinks.forEach((item) => links.appendChild(link(item)));
      node.appendChild(links);
    }
    const grid = el('div', 'grid grid-2');

    data.statusCards.forEach((cardData) => {
      const card = el('article', 'card');
      const meta = el('div', 'meta-row');
      cardData.badges.forEach((item) => meta.appendChild(el('span', 'badge badge-status', item)));
      card.appendChild(meta);
      card.appendChild(el('h3', '', cardData.title));
      card.appendChild(el('p', '', cardData.summary));
      card.appendChild(el('p', '', `Current state: ${cardData.status}`));

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
      const node = section(block.title, block.intro);
      const gridClass = block.cards.length >= 3 ? 'grid grid-3' : 'grid grid-2';
      const grid = el('div', gridClass);

      block.cards.forEach((cardData) => {
        const card = el('article', 'card');
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
    const node = section('Timeline', 'A compact chronological reading path for the case.');
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
    const node = section('Canonical source ids', 'The page keeps the source layer visible. These ids match the current case-level reference map.');
    const list = el('div', 'source-list');

    data.sources.forEach((item) => {
      const source = el('article', 'source-item');
      source.appendChild(el('div', 'source-id', item.id));
      source.appendChild(el('p', '', item.role));
      source.appendChild(el('p', '', `Object usage: ${item.usage}`));
      const links = el('div', 'inline-links');
      links.appendChild(link({ label: 'Open references.md', href: '../references.md' }));
      source.appendChild(links);
      list.appendChild(source);
    });

    node.appendChild(list);
    app.appendChild(node);
  };

  const renderReadingPath = () => {
    const node = section('Reading path', 'The page is a release surface, but it still points back to the governed object layer.');
    const links = el('div', 'object-links');
    data.readingPath.forEach((item) => links.appendChild(link(item)));
    node.appendChild(links);
    app.appendChild(node);
  };

  renderHero();
  renderStatusCards();
  renderSections();
  renderTimeline();
  renderSources();
  renderReadingPath();
})();
