class Solution:
	def fib(self, n):
		if n == 0:
			return 0
		elif n == 1:
			return 1
		else:
			return self.fib(n - 1) + self.fib(n - 2)


solution = Solution()
solution.fib(10)


class Solution_2:
	def fib(self, n):
		a, b = 0, 1
		for _ in range(n):
			a, b = b, (a + b)
		print(a)
		return a


solution_2 = Solution_2()
solution_2.fib(10)
