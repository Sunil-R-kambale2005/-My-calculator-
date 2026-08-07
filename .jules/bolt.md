## 2025-08-07 - Refactoring Calculator Event Handlers & Caching DOM Elements
**Learning:** In a vanilla HTML calculator, attaching 17 individual inline `onclick` attributes is highly inefficient and creates substantial DOM overhead. Furthermore, executing `document.querySelector('#display')` on every button click triggers costly DOM queries.
**Action:** Use event delegation by registering a single click listener on `.btn-container` and caching the `#display` element reference in a local JS variable to achieve O(1) element retrieval.
