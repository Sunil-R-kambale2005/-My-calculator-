## 2026-09-28 - DOM Query Caching & Event Delegation in Static HTML
**Learning:** In simple vanilla HTML/CSS applications, inline onclick handlers trigger repeated DOM queries (`document.querySelector`) on every interaction, adding unnecessary DOM traversal and memory allocations.
**Action:** Always cache DOM references during initialization and leverage event delegation on common parent containers.
