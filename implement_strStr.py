# https://leetcode.com/problems/implement-strstr/

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1


solution = Solution()
solution.strStr('hello', 'll')
