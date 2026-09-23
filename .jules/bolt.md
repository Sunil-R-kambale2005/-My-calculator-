## 2025-05-18 - DOM Query Caching and Event Delegation for Static Calculator
**Learning:** In simple vanilla HTML calculators, attaching inline handlers that repeatedly perform `document.querySelector()` causes unnecessary DOM tree searches on every button interaction.
**Action:** Cache top-level element references (like `#display`) and delegate click events to the parent container (`.btn-container`) using `event.target.closest()`.
