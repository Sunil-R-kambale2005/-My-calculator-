## 2025-05-18 - Event Delegation & DOM Caching for Static HTML Calculator
**Learning:** In simple vanilla HTML apps, replacing repetitive inline `onclick` event handlers with single-container event delegation and caching target DOM node queries eliminates repeated `document.querySelector` executions per user action and reduces event listener overhead.
**Action:** When working on legacy static HTML projects, refactor inline DOM event handlers to delegated container listeners and cache DOM references outside handler functions.
