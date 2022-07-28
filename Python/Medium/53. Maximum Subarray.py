"""
53. Maximum Subarray - https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currSum = 0
        maxSum = nums[0]
        for digit in nums:
            if currSum < 0:
                currSum = 0
            currSum += digit
            maxSum = max(maxSum, currSum)
        return maxSum

############## LOCAL TESTING ONLY ############################ 
    def __init__(self, s):
        self.maxSubArray(s)

s = Solution([-2,1,-3,4,-1,2,1,-5,4])

"""
Runtime: 35 ms, faster than 92.95% of Python online submissions for Valid Anagram.
Memory Usage: 14 MB, less than 57.18% of Python online submissions for Valid Anagram.
"""