"""
1695. Maximum Erasure Value - https://leetcode.com/problems/maximum-erasure-value/


You are given an array of positive integers nums and want to erase a subarray containing unique elements. The score you get by erasing the subarray is equal to the sum of its elements.

Return the maximum score you can get by erasing exactly one subarray.

An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).

 
Example 1:

Input: nums = [4,2,4,5,6]
Output: 17
Explanation: The optimal subarray here is [2,4,5,6].
Example 2:

Input: nums = [5,2,1,2,5,2,1,2,5]
Output: 8
Explanation: The optimal subarray here is [5,2,1] or [1,2,5].
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 104
"""
class Solution(object):
    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        setArr = set(nums)
        if len(setArr) == len(nums):
            return sum(nums)
        maxSum = 0
        currSum = 0
        currSet = set()
        currPos = 0
        for i, num in enumerate(nums):
            if num not in currSet: # new element
                currSet.add(num) # add to set
                currSum += num # add it to the current sum
                continue
            maxSum = max(maxSum, currSum) # get current max
            while nums[currPos] != nums[i]: # remove all elements leading up to the first occurence of the num
                currSum -= nums[currPos] # remove from sum
                currSet.remove(nums[currPos])
                currPos += 1 # change current position
            currPos += 1 
        return max(maxSum, currSum) # return max based on last iteration
            
        ### solution based on #3; but very very slow ###
        # setArr = set(nums)
        # if len(setArr) == len(nums):
        #     return sum(nums)
        # currArr = []
        # currSum = 0
        # for num in nums:
        #     if num in currArr:
        #         currSum
                
                
                
        #          = max(currSum, sum(currArr))
        #         currArr = currArr[currArr.index(num)+1:]
        #     currArr.append(num)
        # currSum = max(currSum, sum(currArr))
        # return currSum

############## LOCAL TESTING ONLY ############################ 
    def __init__(self, nums):
        self.maximumUniqueSubarray(nums)

s = Solution([4,2,4,5,6])
"""
Runtime: 952 ms, faster than 100.00% of Python online submissions for Maximum Erasure Value.
Memory Usage: 24.7 MB, less than 59.52% of Python online submissions for Maximum Erasure Value.
"""