# https://leetcode.com/problems/group-anagrams/solution/

from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        deconstructed_words = defaultdict(list)
        for word in strs:
            deconstructed_words[''.join(sorted([i for i in word]))].append(word)

        return list(deconstructed_words.values())


solution = Solution()
solution.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
