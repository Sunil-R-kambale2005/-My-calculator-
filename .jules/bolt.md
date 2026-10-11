## 2026-10-11 - Fast Data Attribute Lookups vs DOMStringMap Overhead
**Learning:** `getAttribute('data-*')` is ~3.7x faster than `dataset.*` property access in Chromium V8 engine because `getAttribute` directly returns string values without creating `DOMStringMap` objects. However, on human click interaction handlers (cold paths), micro-optimizations like this save negligible nanoseconds and do not significantly impact end-user experience.
**Action:** Focus performance efforts on hot rendering loops or bulk data processing rather than human-driven DOM event handler attribute lookups.
