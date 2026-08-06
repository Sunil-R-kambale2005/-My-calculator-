## 2025-02-15 - Event Delegation & DOM Caching Optimization
**Learning:** In highly interactive, vanilla DOM applications (like calculators), repeated DOM queries (`document.querySelector`) and multiple inline event handlers block the main thread and consume excessive memory. Inline handlers also prevent modern V8 optimizations.
**Action:** Always cache DOM elements used inside frequently triggered callbacks and use event delegation (attaching a single listener to the parent element) to keep memory footprint and registration overhead minimal.
