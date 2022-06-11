"""
283. Move Zeroes - https://leetcode.com/problems/move-zeroes/

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        lastNonZeroPos = 0
        for i in range(len(nums)):
            if nums[i] != 0: # found non zero
                nums[i], nums[lastNonZeroPos] = nums[lastNonZeroPos], nums[i] # swap number with last non zero position
                                                                              # if a zero is detected, the loop continues
                                                                              # then when a number is detected, it swaps the number with the correct position (where the zero was detected because nonZeroPos did not increment)
                lastNonZeroPos += 1

############## LOCAL TESTING ONLY ############################ 
    def __init__(self, nums):
        self.moveZeroes(nums)

s = Solution([0,1,0,3,12])

"""
Runtime: 137 ms, faster than 86.38% of Python online submissions for Move Zeroes.
Memory Usage: 14.7 MB, less than 60.48% of Python online submissions for Move Zeroes.
"""