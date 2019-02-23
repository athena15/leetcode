from collections import defaultdict


class Solution:
	def lengthOfLongestSubstring(self, s):
		"""
		:type s: str
		:rtype: int
		"""
		d = defaultdict(int)

		start = 0
		stop = 1

		length = 0
		longest = 0

		while s[start] == s[stop]:
			stop += 1
			length += 1
			if length > longest:
				longest = length

		if s[start] == s[stop]:
			start += 1
			length = 0

		print(longest)
		return longest


solution = Solution()
solution.lengthOfLongestSubstring('pwwkew')


def test_string():
	solution = Solution()
	assert solution.lengthOfLongestSubstring('abcefabc') == 5
