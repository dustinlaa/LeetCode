"""
15. 3Sum - https://leetcode.com/problems/3sum/


Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.


Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
 

Constraints:

0 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort() # list is sorted
        output = []
        for left in range(len(nums)-2): # need at least 3, if there is less than 3,  return empty output
            if left > 0 and nums[left] == nums[left-1]: # prevents duplicates. If left is equal to 0, there are no previous elements. 
                continue
            mid = left + 1
            right = len(nums)-1
            while mid < right:
                # print(f"left: {left}")
                # print(f"mid: {mid}")
                # print(f"right: {right}")
                currSum = nums[left] + nums[mid] + nums[right]
                if currSum < 0: # need bigger number
                    mid +=1
                elif currSum > 0: # need smaller number
                    right -=1
                else:
                    # print(f"adding: {nums[left], nums[mid], nums[right]}")
                    output.append([nums[left], nums[mid], nums[right]])
                    while mid < right and nums[mid] == nums[mid+1]: # avoids duplicates, finds other combinations
                        mid +=1
                    while mid < right and nums[right] == nums[right-1]: # avoiding duplicates
                        right -= 1
                    mid +=1 # increment to new val
                    right -=1 # decrement to new val
        return output

        ### alternative solution ###
        # output = set()
        # nums.sort()
        # for i in range(len(nums)-2): # need at least 3, if there is less than 3,  return empty output
        #     target = -nums[i] # if left + right = -target, that means if they were all subtracted it would be 0
        #     left = i + 1 
        #     right = len(nums)-1
        #     while left < right:
        #         currSum = nums[left] + nums[right] 
        #         if currSum < target: # need bigger number
        #             left += 1
        #         elif currSum > target: # need smaller number
        #             right -=1
        #         else:
        #             output.add((nums[i], nums[left], nums[right])) # found answer
        #             left +=1 # increment
        #             right -=1 # decrement
        # return output
      
############## LOCAL TESTING ONLY ############################   
    def __init__(self, nums):
        self.nums = nums
        self.threeSum(nums)

s = Solution([-1,0,1,2,-1,-4])

"""
Runtime: 524 ms, faster than 88.67% of Python online submissions for 3Sum.
Memory Usage: 16.9 MB, less than 43.03% of Python online submissions for 3Sum.
"""