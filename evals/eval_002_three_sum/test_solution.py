import pytest

from .model_solution import Solution


@pytest.fixture
def solver():
    return Solution()


def normalize(triplets):
    """Put triplets in a standard order so the comparison ignores ordering."""
    return sorted(sorted(triplet) for triplet in triplets)


CASES = [
    # examples from the problem
    ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
    ([0, 1, 1], []),
    ([0, 0, 0], [[0, 0, 0]]),
    # no answer
    ([1, 2, -2, -1], []),
    ([-4, -2, -1], []),
    # several answers
    ([-2, 0, 1, 1, 2], [[-2, 0, 2], [-2, 1, 1]]),
    # duplicates: the hardest part of 3Sum
    ([0, 0, 0, 0], [[0, 0, 0]]),
    ([-2, 0, 0, 2, 2], [[-2, 0, 2]]),
    ([-1, -1, 0, 1], [[-1, 0, 1]]),
]


@pytest.mark.parametrize("nums, expected", CASES)
def test_three_sum(solver, nums, expected):
    assert normalize(solver.threeSum(nums)) == normalize(expected)