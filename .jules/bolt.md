## 2025-05-18 - Cached DOM Lookups and Event Delegation
**Learning:** Inline `onclick` attributes cause DOM query selector overhead on every user interaction (`document.querySelector('#display')`) and duplicate handler closures.
**Action:** Cache DOM elements once on script load and use event delegation on parent containers to handle user inputs efficiently.
