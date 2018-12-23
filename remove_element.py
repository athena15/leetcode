# https://leetcode.com/problems/remove-element/

class Solution:
	def removeElement(self, nums, val):
		"""
		:type nums: List[int]
		:type val: int
		:rtype: int
		"""

		while val in nums:
			nums.remove(val)

		return len(nums)


def test():
	solution = Solution()
	assert solution.removeElement([1, 0, 1, 1, 0, 1, 0], 1) == 3
