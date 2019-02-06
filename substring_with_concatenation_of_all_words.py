# https://leetcode.com/problems/substring-with-concatenation-of-all-words

from itertools import permutations

import regex as re


class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if words:
            targets = [''.join(i) for i in list(permutations(words, len(words)))]
        else:
            return []

        index_matches = []
        for target in targets:
            if target in s:
                regex = r'(' + target + r')'
                matches = re.finditer(regex, s, overlapped=True)
                indexes = [m.start(0) for m in matches]
                print(indexes)
                index_matches.extend(indexes)

        return list(set(index_matches))


solution = Solution()
solution.findSubstring(s='foobarfoobar', words=['foo', 'bar'])
