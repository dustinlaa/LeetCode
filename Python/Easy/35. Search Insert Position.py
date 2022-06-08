"""
35. Search Insert Position


Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
"""
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = (right+left)//2 # gets the middle
            if nums[mid] == target: # found target
                return mid
            elif nums[mid] < target: # need to go up
                left = mid + 1
            elif nums[mid] > target: # need to go down
                right = mid - 1
        return left

############## LOCAL TESTING ONLY ############################ 
    def __init__(self, nums, target):
        self.searchInsert(nums, target)

s = Solution([1,3,5,6], 5)
            
"""
Runtime: 43 ms, faster than 57.36% of Python online submissions for Search Insert Position.
Memory Usage: 14.3 MB, less than 27.22% of Python online submissions for Search Insert Position.
"""