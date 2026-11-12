# Code Evaluation Portfolio

Written evaluations of AI-generated code. Each one has the task, the model's
solution kept unedited, a corrected solution, tests that prove the verdict,
and a written evaluation scored with the rubric below.

## Run the tests

```bash
pip install -r requirements.txt
pytest -v
```

Or with Docker:

```bash
docker build -t code-eval .
docker run --rm code-eval
```

## Evaluations

| # | Task | Verdict | Rating |
| --- | --- | --- | --- |
| [001](evals/eval_001_longest_substring/evaluation.md) | Longest Substring Without Repeating Characters | Incorrect — `left` moves backward | 3/7 |
| [002](evals/eval_002_three_sum/evaluation.md) | 3Sum | Correct — sort + two pointers, duplicates skipped | 7/7 |

## Folder layout per evaluation

```
evals/eval_NNN_name/
├── task.md             # the problem
├── model_solution.py   # AI output, unedited
├── fixed_solution.py   # smallest correct change (only if the verdict is Incorrect)
├── test_solution.py    # tests that prove the verdict
└── evaluation.md       # verdict, failing input, root cause, fix, rating
```

## Rubric

1. **Correctness** — Right output for the examples and for inputs I invent?
   Can I find one input where it fails?
2. **Edge cases** — Smallest input (empty / one item), duplicates, negatives
   and zero, largest size in the constraints. For each: input → expected → handled?
3. **Efficiency** — Real time and space complexity? Does it match the claim?
   Is there a known better approach?
4. **Readability** — Meaningful names? Any dead code, debug prints or
   duplicated lines? Understandable without running it?
5. **Instruction-following** — Required name, inputs and return type?
   Every constraint respected (e.g. O(1) extra space, no division, output order)?
6. **Security** — Trusts input it shouldn't (missing validation, unverified
   signatures, SQL built from strings)? N/A for pure DSA problems.

### Rating (1–7) — correctness sets the ceiling

| Score | Meaning |
| --- | --- |
| 7 | Correct, edge cases handled, optimal, accurate claims, clean |
| 6 | Correct and optimal; small readability or naming issues only |
| 5 | Correct, but suboptimal or with a wrong complexity claim |
| 4 | Works on normal inputs but fails an edge case |
| 3 | Fails some normal inputs; right idea, wrong execution |
| 2 | Wrong approach; passes examples only by luck |
| 1 | Doesn't run, ignores the task, or wrong on basic examples |
