# Bolt's Performance Journal - Critical Learnings Only

This journal documents critical learnings to avoid mistakes or make better decisions for performance optimization.

## 2024-08-13 - Initial Setup
**Learning:** Found that the static HTML calculator has a highly repetitive inline click handler pattern, causing DOM query overhead on every button click.
**Action:** Replace inline event handlers with unified event delegation and cache DOM reference to the `#display` element to avoid repeated queries.

## 2024-08-13 - HTML Event Delegation & Caching Optimization
**Learning:** For a simple utility application like a calculator, embedding repeated inline `onclick` handler strings within the HTML markup creates needless DOM query overhead (`document.querySelector('#display')` triggered on every individual click), slows down initial parsing/compilation, and makes maintenance harder.
**Action:** Implement event delegation via a single event listener on the `.btn-container` parent container, and cache the `#display` element reference on script load. This reduces event handler allocation from 17 down to 1, and limits DOM lookup overhead to a single initial call.
