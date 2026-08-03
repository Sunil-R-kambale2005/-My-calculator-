# Bolt Performance Journal

This is Bolt's performance journal for critical learnings.

## 2024-08-03 - [Initial Analysis of Static Calculator]
**Learning:** Found a static HTML calculator that relies heavily on inline onclick handlers, multiple duplicate `document.querySelector('#display')` calls, and `eval()` for computation. Each button click performs a DOM query (`document.querySelector('#display')`), which is an O(N) operation on the DOM tree and slows down interaction.
**Action:** Optimize event handling by caching the DOM query for `#display` and replacing inline `onclick` attributes with an efficient, single event delegation listener or standardized JavaScript functions to reduce inline JS overhead, improve readability, and boost event dispatch performance.
