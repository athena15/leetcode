from collections import defaultdict


class Solution:
	def maxArea(self, height):
		"""
		:type height: List[int]
		:rtype: int
		"""

		indices = defaultdict(list)
		for i, v in enumerate(height):
			indices[v].append(i)

		def get_min_index(num):
			return min(indices[num])

		def get_last_index(num):
			return max(indices[num])

		def calculate_water(num_1, num_2):
			h = min([num_1, num_2])
			w = get_last_index(num_2) - get_min_index(num_1)
			return h * w

		d = defaultdict(int)
		highest = 0

		height.sort(reverse=True)
		print(height)

		i, j = 0, len(height) - 1
		water = 0
		while i < j:
			amt = min([i, j]) * (j - i)

		# for i in range(len(height)):
		# 	for j in range(len(height)):
		# 		amount = calculate_water(height[i], height[j])
		# 		if amount > highest:
		# 			highest = amount

		print(highest)
		return highest


solution = Solution()
solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
