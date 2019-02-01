# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

from itertools import product


# Concise method using cartesian product
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


# Verbose method using backtracking, less concise, but faster runtime
class Solution_2:
	def letterCombinations(self, digits):
		"""
		:type digits: str
		:rtype: List[str]
		"""

		if not digits:
			return []

		d = {'2': ['a', 'b', 'c'],
		     '3': ['d', 'e', 'f'],
		     '4': ['g', 'h', 'i'],
		     '5': ['j', 'k', 'l'],
		     '6': ['m', 'n', 'o'],
		     '7': ['p', 'q', 'r', 's'],
		     '8': ['t', 'u', 'v'],
		     '9': ['w', 'x', 'y', 'z']}

		results = []

		def backtrack(remaining_digits, current_string):
			if len(remaining_digits) == 1:
				for n in d[remaining_digits]:
					results.append(current_string + n)
			else:
				for n in d[remaining_digits[0]]:
					backtrack(remaining_digits[1:], current_string + n)

			return results

		return backtrack(digits, '')


solution = Solution()
solution.letterCombinations('239')

solution_2 = Solution_2()
solution_2.letterCombinations('239')
