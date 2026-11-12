# Eval 002 — 3Sum

**Verdict:** Correct

**Evidence:** Standard sort + two-pointer approach. For each fixed
`nums[i]`, it runs Two Sum II on the rest for target `-nums[i]`.
Duplicates are skipped for `i` (compare with the previous number) and
after each match (compare `left` and `right` with the values just used),
so each triplet of values is added once. All 9 tests pass, including
3 duplicate-heavy cases.

## Rubric check

| Criterion | Result |
| --- | --- |
| Correctness | Correct on all 9 tests, including examples, no-answer and duplicate cases |
| Edge cases | `[0,0,0]` → `[[0,0,0]]` ✓ · `[0,0,0,0]` → `[[0,0,0]]` ✓ · `[-2,0,0,2,2]` → `[[-2,0,2]]` ✓ |
| Efficiency | O(n²) time: n fixed values × an O(n) two-pointer scan, which dominates the O(n log n) sort. O(1) extra space besides the sort (Python's sort may use up to O(n)). Early `break` once `nums[i] > 0`. |
| Readability | Clear names (`left`, `right`, `total`, `result`), flat structure, no dead code. Minor: no comment explaining the duplicate-skip loops. |
| Instruction-following | Correct class, method name, input and return types |
| Security | N/A (pure function) |

## Notes

- The `right` skip loop after a match is an optimization, not required
  for correctness: after `left` moves to a new larger value, the sum
  with a duplicate `right` is > 0, so `right` moves anyway.
- `nums.sort()` modifies the caller's list. Acceptable on LeetCode,
  but worth noting for production code.

**Rating: 7 / 7** — correct on every case including duplicates, optimal
complexity, clean code; the only notes are minor and don't affect the result.