# https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x):
        return int(str(x ** .5).split('.')[0])


solution = Solution()
solution.mySqrt(64)
