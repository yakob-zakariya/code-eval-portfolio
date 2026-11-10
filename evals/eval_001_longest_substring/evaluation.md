# Eval 001 — Longest Substring Without Repeating Characters

**Verdict:** Incorrect

**Failing input:** `"ccbbcc"` → returns `3`, expected `2`
(also `"abba"` → 3 vs 2, and `"tmmzuxt"` → 6 vs 5)

**Root cause:** The line `left = seen[ch] + 1` can move `left` backward.
`seen` keeps old positions of characters that are already outside the window.
In `"ccbbcc"`, when `c` repeats at index 4 the window starts at index 3, but
`seen["c"]` is 1, so `left` jumps back to 2. The window becomes `"bbc"`, which
contains a duplicate, and its length 3 is wrongly counted.

**Fix:**

```python
left = max(left, seen[ch] + 1)
```

`left` may only stay or move forward. See `fixed_solution.py`.

## Rubric check

| Criterion | Result |
| --- | --- |
| Correctness | Fails whenever a character repeats after the window has moved past its previous position |
| Edge cases | `""` → 0 ✓, `"a"` → 1 ✓, `" "` → 1 ✓ |
| Efficiency | O(n) time, O(min(n, k)) space — optimal |
| Readability | Clear and short; `seen` could be named `last_seen` |
| Instruction-following | Correct name, input and return type |
| Security | N/A (pure function) |

**Rating: 3 / 7** — right approach (sliding window with a dict) and optimal
complexity, but it returns wrong answers on normal inputs.

**Proof:** `test_solution.py` — the bug cases fail on the model's code and pass
on the fix.
