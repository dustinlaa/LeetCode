"""
55. Jump Game - https://leetcode.com/problems/jump-game/

You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

Return true if you can reach the last index, or false otherwise.

Example 1:

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

Constraints:

1 <= nums.length <= 104
0 <= nums[i] <= 105
"""
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxDist = 0
        length = len(nums)
        for i in range(length): # goes through ever num in the array to find the max sitance based on where it lands and what number is in that pos
            if maxDist == length: # sees if we have reached the end
                return True
            if maxDist < i: # the max distance we can go is behind where we are searching, meaning we could never reach this position
                return False
            maxDist = max(maxDist, i+nums[i]) # gets max between what the current max is and where we would land if we take our current position and move it's number of space sup
        return True
            
############## LOCAL TESTING ONLY ############################ 
    def __init__(self, nums):
        self.canJump(nums)

s = Solution([2,3,1,1,4])

"""
Runtime: 520 ms, faster than 66.36% of Python online submissions for Jump Game.
Memory Usage: 14.5 MB, less than 66.55% of Python online submissions for Jump Game.
"""