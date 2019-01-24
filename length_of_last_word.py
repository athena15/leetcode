# https://leetcode.com/problems/length-of-last-word/submissions/

class Solution:
	def lengthOfLastWord(self, s):
		"""
		:type s: str
		:rtype: int
		"""

		if s:
			return len(s.rstrip().split(' ')[-1])
		else:
			return 0


solution = Solution()
solution.lengthOfLastWord("a    b  c")
