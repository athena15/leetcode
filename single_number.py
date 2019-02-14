# https://leetcode.com/problems/single-number/

from collections import Counter


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = Counter(nums)
        for k, v in count.items():
            if v == 1:
                return k


solution = Solution()
solution.singleNumber([6, 1, 2, 1, 6, 4, 2])
solution.singleNumber([1])
