"""
377. Combination Sum IV - https://leetcode.com/problems/combination-sum-iv/

Given an array of distinct integers nums and a target integer target, return the number of possible combinations that add up to target.

The test cases are generated so that the answer can fit in a 32-bit integer.


Example 1:

Input: nums = [1,2,3], target = 4
Output: 7
Explanation:
The possible combination ways are:
(1, 1, 1, 1)
(1, 1, 2)
(1, 2, 1)
(1, 3)
(2, 1, 1)
(2, 2)
(3, 1)
Note that different sequences are counted as different combinations.
Example 2:

Input: nums = [9], target = 3
Output: 0
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 1000
All the elements of nums are unique.
1 <= target <= 1000
"""
class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        combos = [0] * (1+target) # makes an array that looks like this if target is 4: [0, 0, 0, 0, 0]
        for num in nums: # sets all the positions that are less than target to be equal to 1, used to include the number itself
            if num <= target:
                combos[num] = 1
        # this part of the code for each array pos, it adds the number of combos if the target was 0, 1, 2, etc
        for i in range(target+1): # goes through everything from 0 to target inclusive
            for num in nums:
                if i - num > 0: # if the current i minus num is greater than 0, add to combos in the ith position the previous number combo
                    combos[i] += combos[i-num]
        return combos[-1] # the very last number is the total number of combos possible

############## LOCAL TESTING ONLY ############################ 
    def __init__(self, nums, target):
        self.combinationSum4(nums, target)

s = Solution([1,2,3], 4)

"""
Runtime: 23 ms, faster than 93.08% of Python online submissions for Combination Sum IV.
Memory Usage: 13.4 MB, less than 55.60% of Python online submissions for Combination Sum IV.
"""