"""
1365. How Many Numbers Are Smaller Than the Current Number - https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/


Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.

Example 1:

Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation: 
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1). 
For nums[3]=2 there exist one smaller number than it (1). 
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).
Example 2:

Input: nums = [6,5,4,8]
Output: [2,1,0,3]
Example 3:

Input: nums = [7,7,7,7]
Output: [0,0,0,0]
 

Constraints:

2 <= nums.length <= 500
0 <= nums[i] <= 100
"""
class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        sortedList = sorted(nums) # creates a sorted copy of the nums list
        output = [] # output array
        for num in nums: # for each num in nums
            output.append(sortedList.index(num)) # adding the index of the num in the sorted list (all numbers before are smaller than current number)
        return output
############## LOCAL TESTING ONLY ############################   
    def __init__(self, nums):
        self.nums = nums
        self.smallerNumbersThanCurrent(nums)

s = Solution([6,5,4,8])
"""
Runtime: 71 ms, faster than 72.09% of Python online submissions for How Many Numbers Are Smaller Than the Current Number.
Memory Usage: 13.6 MB, less than 39.11% of Python online submissions for How Many Numbers Are Smaller Than the Current Number.
"""