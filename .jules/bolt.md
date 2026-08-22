## 2026-08-22 - Event Delegation and DOM Caching in Vanilla HTML Calculator
**Learning:** Inlining `onclick` attributes and executing `document.querySelector` on every button click creates unnecessary DOM tree traversals and duplicate event handler initializations across HTML elements. Using event delegation on a parent container with a cached DOM query significantly reduces DOM lookup overhead and memory allocation.
**Action:** Replace inline event handlers with a single delegated event listener on parent container and cache DOM element references upon page load.
