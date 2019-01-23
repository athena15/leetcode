# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
	def removeDuplicates(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		unique_nums = set()
		i = 0
		while i < len(nums):
			if nums[i] in unique_nums:
				del nums[i]
			else:
				unique_nums.add(nums[i])
				i += 1

		return len(nums)


solution = Solution()
solution.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
