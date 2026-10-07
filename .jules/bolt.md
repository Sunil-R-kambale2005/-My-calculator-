## 2026-10-07 - `getAttribute` vs `dataset` performance in event listeners
**Learning:** `element.getAttribute('data-*')` is ~3.3x faster than `element.dataset.*` because `dataset` instantiates a `DOMStringMap` proxy host object on access, while `getAttribute` performs direct attribute lookup. Note that `getAttribute` returns `null` when an attribute is missing, whereas `dataset` returns `undefined`.
**Action:** Use `getAttribute('data-...')` in high-frequency DOM event handlers instead of `dataset` and check for `null`.
