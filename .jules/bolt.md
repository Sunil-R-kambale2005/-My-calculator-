# Bolt's Performance Journal

This journal documents critical performance learnings for the calculator repository.

## 2023-11-20 - Calculator Optimization and Event Delegation
**Learning:** In a static HTML page containing multiple interactive elements (such as calculator buttons), attaching individual inline event handlers (e.g. `onclick="..."`) results in redundant DOM query lookups (`document.querySelector('#display')`) and creates separate event listener instances for every single element, which wastes memory and slows execution.
**Action:** Use event delegation by attaching a single event listener to the parent container (`.btn-container`), cache DOM references like `#display` to avoid costly lookups, and use custom data attributes (`data-value`) on buttons to determine operations dynamically.
