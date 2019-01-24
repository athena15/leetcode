class Solution:
	def plusOne(self, digits):
		"""
		:type digits: List[int]
		:rtype: List[int]
		"""
		return [int(i) for i in str(int(''.join([str(i) for i in digits])) + 1)]


solution = Solution()
solution.plusOne([4, 3, 2, 1])
