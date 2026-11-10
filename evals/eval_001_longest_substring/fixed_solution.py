"""Corrected solution: the smallest change that makes the model's code correct."""


def length_of_longest_substring(s: str) -> int:
    # Approach: sliding window; `last_seen` stores each character's latest index.
    #   On a repeat, move `left` past that index — but never backward.
    # Complexity: O(n) time — each index is visited once by `right`;
    #   O(min(n, k)) space, k = size of the character set.
    # Edge case: "" → 0 → yes: the loop never runs, returns 0.
    last_seen = {}
    left = 0
    best = 0
    for right, ch in enumerate(s):
        if ch in last_seen:
            left = max(left, last_seen[ch] + 1)  # the fix
        last_seen[ch] = right
        best = max(best, right - left + 1)
    return best
