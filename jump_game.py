# https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        while nums[0] < len(nums):

            jump_length = nums[0]

            if jump_length == 0:
                return False

            elif jump_length >= len(nums):
                return True

            else:
                nums = nums[jump_length:]

        return True


solution = Solution()
solution.canJump([2, 3, 1, 1, 4])
