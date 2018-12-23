# https://leetcode.com/problems/palindrome-number/

class Solution:
	def isPalindrome(self, x):
		"""
		:type x: int
		:rtype: bool
		"""
		x = str(x)
		return x[::-1] == x


solution = Solution()
solution.isPalindrome(101)


def test_true():
	assert solution.isPalindrome(18981) == True


def test_false():
	assert solution.isPalindrome(123) == False
