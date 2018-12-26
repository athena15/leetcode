# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        arr = [i for i, v in enumerate(nums) if v == target]

        if len(arr) > 0:
            return [min(arr), max(arr)]
        else:
            return [-1, -1]


solution = Solution()
solution.searchRange(nums=[5, 7, 7, 8, 8, 8, 8, 10], target=8)
