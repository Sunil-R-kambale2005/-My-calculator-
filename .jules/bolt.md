# Bolt's Performance Journal - Critical Learnings

## 2025-05-18 - Event Delegation & Cached DOM Selection for Vanilla JS
**Learning:** Querying the DOM with `document.querySelector` on every button click causes unnecessary DOM traversal overhead and creates inline handler duplication across elements.
**Action:** Cache element references at initialization and use event delegation on parent container elements (`.btn-container`) to handle interactions efficiently in single page vanilla HTML/JS applications.
