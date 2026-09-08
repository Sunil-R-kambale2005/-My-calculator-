## 2025-09-08 - Calculator DOM Query Caching and Event Delegation
**Learning:** Attaching inline `onclick` handlers that execute `document.querySelector` on every click causes unnecessary DOM traversals and bloats HTML. Replacing inline listeners with single event delegation on container and caching DOM references eliminates redundant DOM queries.
**Action:** Use single event listeners on parent container and cache DOM references in JS scope for element lookups.
