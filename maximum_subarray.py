# https://leetcode.com/problems/maximum-subarray/

class Solution:
	def maxSubArray(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		maximum, current = 0, 0
		for n in nums:
			current += n
			if current < 0:
				current = 0
				continue
			if current > maximum:
				maximum = current

		if maximum == 0:
			return max(nums)

		return maximum


solution = Solution()
# solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
solution.maxSubArray([-1])
