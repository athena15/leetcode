# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

from itertools import product


class Solution:
	def letterCombinations(self, digits):
		"""
		:type digits: str
		:rtype: List[str]
		"""
		numbers = ['2', '3', '4', '5', '6', '7', '8', '9']
		alphabet = [i for i in 'abc def ghi jkl mno pqrs tuv wxyz'.split()]
		nums_map = dict(zip(numbers, alphabet))

		if not digits:
			return []

		possibilities = [list(nums_map[i]) for i in digits]

		print([''.join(_) for _ in product(*possibilities)])
		return [''.join(_) for _ in product(*possibilities)]


solution = Solution()
solution.letterCombinations('239')
