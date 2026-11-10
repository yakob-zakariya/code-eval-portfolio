"""Tests for eval 001.

- NORMAL_CASES pass on both solutions (the model's code is not broken everywhere).
- BUG_CASES are discriminating tests: they pass on the fixed solution and FAIL on
  the model's solution. They are marked xfail(strict=True) for the model, so the
  suite stays green while proving the bug exists. If the model's code ever passed
  them, strict mode would turn that into a failure.
"""

import pytest

from . import fixed_solution, model_solution

NORMAL_CASES = [
    ("abcabcbb", 3),
    ("bbbbb", 1),
    ("pwwkew", 3),
    ("", 0),          # empty string
    ("a", 1),         # single character
    (" ", 1),         # a space is a valid character
    ("dvdf", 3),
]

BUG_CASES = [
    ("abba", 2),      # model returns 3
    ("ccbbcc", 2),    # model returns 3
    ("tmmzuxt", 5),   # model returns 6
]


@pytest.mark.parametrize("s, expected", NORMAL_CASES + BUG_CASES)
def test_fixed_solution(s, expected):
    assert fixed_solution.length_of_longest_substring(s) == expected


@pytest.mark.parametrize("s, expected", NORMAL_CASES)
def test_model_solution_normal_cases(s, expected):
    assert model_solution.length_of_longest_substring(s) == expected


@pytest.mark.xfail(strict=True, reason="left pointer moves backward on stale repeats")
@pytest.mark.parametrize("s, expected", BUG_CASES)
def test_model_solution_bug_cases(s, expected):
    assert model_solution.length_of_longest_substring(s) == expected

