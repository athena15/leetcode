# https://leetcode.com/problems/valid-parentheses/solution/

class Solution:
	def isValid(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		if s == '':
			return True

		c = {')': '(', '}': '{', ']': '['}
		opened = []

		for n in s:
			if n in c.values():
				opened.append(n)
			if n in c.keys():
				if opened and c[n] == opened[-1]:
					opened.pop()
				else:
					return False

		return not opened


solution = Solution()
solution.isValid('()[]{}')
