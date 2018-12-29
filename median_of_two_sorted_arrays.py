# https://leetcode.com/problems/median-of-two-sorted-arrays/submissions/

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = sorted(nums1 + nums2)

        halfway_index = len(nums) // 2

        if len(nums) % 2 != 0:
            return nums[halfway_index]
        else:
            return (nums[halfway_index] + nums[halfway_index - 1]) / 2


solution = Solution()
solution.findMedianSortedArrays([1, 3], [2])
