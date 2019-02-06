# https://leetcode.com/problems/reverse-integer/

class Solution:
	def reverse(self, x):
		"""
		:type x: int
		:rtype: int
		"""
		x = str(x)
		if x[0] == '-':
			r = int('-' + x[:0:-1])
		else:
			r = int(x[::-1])

		if abs(r) > 2 ** 31:
			return 0
		else:
			return r


solution = Solution()
solution.reverse(-123)
