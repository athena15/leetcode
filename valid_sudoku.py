# https://leetcode.com/problems/valid-sudoku/
from collections import Counter


class Solution:
	def isValidSudoku(self, board):
		"""
		:type board: List[List[str]]
		:rtype: bool
		"""

		def check_invalid(nums):
			c = Counter(nums)
			c.pop('.')
			for k, v in c.items():
				if v > 1:
					return True

		# Check rows
		side_len = len(board)
		for x in range(side_len):
			if check_invalid(board[x]):
				return False

			# Check columns
			column = []
			for y in range(side_len):
				column.append(board[y][x])

			if check_invalid(column):
				return False

		# Check squares
		for i in range(0, 9, 3):
			for j in range(0, 9, 3):
				square = []
				for x in range(i, i + 3):
					for y in range(j, j + 3):
						square.append(board[x][y])

				if check_invalid(square):
					return False

		return True


solution = Solution()
solution.isValidSudoku([['.', '.', '.', '1', '4', '.', '.', '2', '.'],
                        ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
                        ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
                        ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
                        ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
                        ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
                        ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
                        ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
                        ['.', '.', '.', '5', '.', '.', '.', '7', '.']])
