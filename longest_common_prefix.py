# https://leetcode.com/problems/longest-common-prefix/submissions/
# 36 ms, faster than 99.62% of submissions

class Solution:
	def longestCommonPrefix(self, strs):
		"""
		:type strs: List[str]
		:rtype: str
		"""
		if not strs:
			return ''

		i = 0
		for letter in zip(*strs):
			if len(set(letter)) > 1:
				return strs[0][:i]
			i += 1
		return strs[0][:i]


solution = Solution()
solution.longestCommonPrefix(["flower", "flow", "flight"])
solution.longestCommonPrefix(["aa", "aaa"])
