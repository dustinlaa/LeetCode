"""
16. 3Sum Closest - https://leetcode.com/problems/3sum-closest/


Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.

 
Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
 

Constraints:

3 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
-104 <= target <= 104
"""

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closestSum = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)-2): # needs 3 elements
            left = i+1 # left pointer
            right = len(nums)-1 # right pointer
            while left < right: 
                currSum = nums[i] + nums[left] + nums[right]
                if currSum == target: 
                    return target
                if abs(currSum - target) < abs(closestSum - target): # found closer sum
                    closestSum = currSum

                if currSum < target: # need larger sum
                    left += 1
                elif currSum > target: # need smaller sum
                    right -=1
        return closestSum

############## LOCAL TESTING ONLY ############################   
    def __init__(self, nums, target):
        self.threeSumClosest(nums, target)

s = Solution([-1,2,1,-4], 1)

"""
Runtime: 284 ms, faster than 37.19% of Python online submissions for 3Sum Closest.
Memory Usage: 13.6 MB, less than 44.41% of Python online submissions for 3Sum Closest.
"""