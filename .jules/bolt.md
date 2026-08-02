## 2023-11-23 - [Centralized DOM Access and DOM Query Caching]
**Learning:** Querying the DOM via `document.querySelector('#display')` on every single button click introduces overhead and layout/reflow or lookup costs. Centralizing DOM manipulation and caching the element reference reduces DOM query overhead to exactly once during initialization.
**Action:** Replace all inline event handlers that do `document.querySelector('#display')` with centralized helper functions in JS, and store the reference to `#display` in a local variable.
