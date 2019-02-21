"""
https://leetcode.com/problems/contains-duplicate-ii/

Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array
such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""


class Solution:
    def containsNearbyDuplicate(self, nums: list, k: int) -> 'bool':
        seen_nums = {}
        for i, v in enumerate(nums):
            if v not in seen_nums.keys():
                seen_nums[v] = i
            else:
                if i - seen_nums[v] <= k:
                    return True
                seen_nums[v] = i

        return False


solution = Solution()
solution.containsNearbyDuplicate(nums=[1, 0, 1, 1], k=1)
