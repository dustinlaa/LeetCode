"""
33. Search in Rotated Sorted Array - https://leetcode.com/problems/search-in-rotated-sorted-array/

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.


Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1
 

Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104
"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target not in nums:
            return -1
        left = 0
        right =  len(nums)-1
        while left <= right:
            mid = (right+left)//2
            if nums[mid] == target: # found target
                return mid
            if nums[left] <= nums[mid]: # value to the left is less than our mid valvue
                if nums[left] <= target and target <= nums[mid]: # if left vlaue is less than target and target is less than mid, that means target is in this left half
                    right = mid - 1
                else:
                    left = mid + 1 # target is in right half
            else:
                if nums[mid] <= target and target <= nums[right]: # target is greater than mid but less than right, target is in the right half
                    left = mid + 1
                else:
                    right = mid - 1
############## LOCAL TESTING ONLY ############################   
    def __init__(self, nums, target):
        self.search(nums, target)

s = Solution([3,5,1], 3)
# s = Solution([4,5,6,7,0,1,2], 0)

"""
Runtime: 65 ms, faster than 5.37% of Python online submissions for Search in Rotated Sorted Array.
Memory Usage: 13.9 MB, less than 15.67% of Python online submissions for Search in Rotated Sorted Array.
"""