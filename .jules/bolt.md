# Bolt's Journal - Critical Learnings

## 2025-05-10 - Event Delegation and DOM Query Caching
**Learning:** Avoid repeated DOM queries (`document.querySelector`) and multiple inline handler initializations on every button click in vanilla JavaScript apps. Event delegation with cached DOM references drastically reduces DOM traversal overhead and garbage collection.
**Action:** Cache DOM elements upon page load and attach single event listener to container elements using event delegation.
