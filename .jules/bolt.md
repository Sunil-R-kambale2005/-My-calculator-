## 2026-03-03 - DOM Caching and Event Delegation in Vanilla JS Calculator
**Learning:** Replacing inline HTML event attributes (`onclick="..."`) and redundant DOM selector queries (`document.querySelector('#display')`) with event delegation on the parent container and a single cached DOM element reference removes repeated DOM tree traversals and reduces event listener overhead.
**Action:** Always check vanilla HTML/JS code for inline event handlers and repetitive DOM queries, refactoring to single-listener event delegation and cached DOM references where applicable.
