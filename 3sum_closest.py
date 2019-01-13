from itertools import combinations


class Solution:
	def threeSumClosest(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: int
		"""

		closest = 9999
		value = None
		for i in combinations(nums, 3):
			sum_i = sum(i)
			if sum_i == target:
				return sum_i
			else:
				if abs(sum_i - target) < closest:
					closest = abs(sum_i - target)
					value = sum_i

		return value


solution = Solution()
solution.threeSumClosest(nums=[-1, 2, 1, -4], target=1)
