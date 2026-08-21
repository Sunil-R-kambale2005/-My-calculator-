# Bolt's Journal - Critical Learnings

## 2026-03-31 - Event Delegation and DOM Caching in Vanilla JS
**Learning:** Repetitive DOM querying (`document.querySelector('#display')`) on every button click creates avoidable main-thread overhead and redundant layout/DOM element lookups. Refactoring inline handlers to event delegation on `.btn-container` and caching `#display` improves event response efficiency.
**Action:** Always cache frequently accessed DOM nodes and prefer delegated event handlers for dynamic or repeating button grids.
