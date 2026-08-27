# Bolt's Journal - Critical Learnings

## 2025-05-18 - DOM Query Caching and Event Delegation in Vanilla JS Calculators
**Learning:** Repetitive `document.querySelector` DOM searches inside click handlers and multiple inline `onclick` attributes create unnecessary DOM queries and memory overhead for event listeners.
**Action:** Cache DOM elements once on load and use event delegation on parent container for clean, high-performance UI interaction.
