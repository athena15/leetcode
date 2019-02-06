from itertools import combinations


class Solution:
	def threeSum(self, nums):
		"""
		:type nums: List[int]
		:rtype: List[List[int]]
		"""
		x = ([i for i in list(combinations(nums, 3)) if sum(i) == 0])
		y = []

		for i in x:
			if sorted(i) not in y:
				y.append(sorted(i))
		return y


solution = Solution()
solution.threeSum([-1, 0, 1, 2, -1, -4])
