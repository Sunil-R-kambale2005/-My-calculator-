## 2025-05-18 - Cache DOM Selectors and Event Delegation for Static HTML Applications
**Learning:** In simple vanilla HTML/JS applications, repetitive inline handlers re-query the DOM on every single user interaction (`document.querySelector('#display')`), causing redundant DOM traversal overhead and inflating initial HTML payload size.
**Action:** Always cache frequently accessed DOM elements at initialization and prefer event delegation over individual inline event handlers on repeated interactive elements.
