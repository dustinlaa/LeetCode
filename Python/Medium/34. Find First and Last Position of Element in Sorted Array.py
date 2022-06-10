"""
34. Find First and Last Position of Element in Sorted Array - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/


Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 
Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
Accepted
1,124,190
Submissions
2,792
"""
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0 or target not in nums:
            return [-1, -1]
        mid = self.binarySearch(nums, target, 0, len(nums)) # finds the value using a binary search
        if mid == -1:
            return [-1, -1]
        else:
            left = self.searchLeft(nums, target, 0, mid) # finds the beginning
            right = self.searchRight(nums, target, mid, len(nums)-1) # finds the end
            return [left, right]
    def binarySearch(self, nums, target, left, right): # binary search to find the target
        while left <= right:
            mid = (right+left)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    def searchLeft(self, nums, target, left, right): # searches on the left half to find the beginning value
        while left <= right:
            mid = (right+left)//2
            if nums[mid] < target:
                left = mid + 1 # increments left when we are smaller than target
            else:
                right = mid - 1
        return left
    def searchRight(self, nums, target, left, right): # searches on the right half to find the end value
        while left <= right:
            mid = (right+left)//2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1 # decrement right when we are larger than target
        return right

############## LOCAL TESTING ONLY ############################   
    def __init__(self, nums, target):
        self.searchRange(nums, target)

s = Solution([5,7,7,8,8,10], 8)

"""
Runtime: 63 ms, faster than 91.10% of Python online submissions for Find First and Last Position of Element in Sorted Array.
Memory Usage: 14.5 MB, less than 85.58% of Python online submissions for Find First and Last Position of Element in Sorted Array.
"""