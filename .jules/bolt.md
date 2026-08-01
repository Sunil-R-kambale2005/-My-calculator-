# Bolt's Performance Journal - Critical Learnings Only

## 2024-08-01 - DOM Performance Optimization in Calculator App
**Learning:** Querying the DOM via `document.querySelector` on every single button press/click is highly inefficient and incurs a layout or querying cost. Inline attributes like `onclick="..."` on individual buttons clutter the HTML, lead to larger transfer sizes, and prevent taking advantage of efficient event delegation.
**Action:** Cache the DOM display input selector globally, and replace individual button click listeners with event delegation at the button container parent level, identifying actions via dataset attributes.
