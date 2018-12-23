class Solution:
	def two_sum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		remainders = []
		for index, num in enumerate(nums):
			if num in remainders:
				return nums.index(target - num), index
			else:
				remainders.append(target - num)
		print(remainders)


solution = Solution()
solution.two_sum(nums=[3, 3], target=6)
