# Task: 3Sum

Source: [LeetCode 15](https://leetcode.com/problems/3sum/)

Given an integer array `nums`, return all triplets `[nums[i], nums[j], nums[k]]`
such that `i`, `j` and `k` are distinct indices and
`nums[i] + nums[j] + nums[k] == 0`. The answer must not contain duplicate
triplets. The order of the triplets, and of the numbers inside each triplet,
does not matter.

| Input                   | Output                      | Why                                          |
| ----------------------- | --------------------------- | -------------------------------------------- |
| `[-1, 0, 1, 2, -1, -4]` | `[[-1, -1, 2], [-1, 0, 1]]` | `[-1, 0, 1]` occurs twice but is listed once |
| `[0, 1, 1]`             | `[]`                        | The only triplet sums to 2                   |
| `[0, 0, 0]`             | `[[0, 0, 0]]`               | The only triplet sums to 0                   |

Constraints: `3 <= len(nums) <= 3000`; `-10^5 <= nums[i] <= 10^5`.

Required signature:

```python
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]: ...
```
