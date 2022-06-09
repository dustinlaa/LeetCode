"""
31. Next Permutation - https://leetcode.com/problems/next-permutation/

A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are considered permutations of arr: [1,2,3], [1,3,2], [3,1,2], [2,3,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.


Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]
Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]
Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100
"""
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        ### explanation: https://www.nayuki.io/page/next-lexicographical-permutation-algorithm ###

        i = len(nums)-1
        while i > 0 and nums[i-1] >= nums[i]: # find the largest number by going right to left
            i -=1
        if i == 0: # list is in decending order
            nums = nums[::-1] # reverse list
            return
        k = i - 1 # get pivot point (the position after the largest number found)
        j = len(nums)-1
        while nums[j] <= nums[k]: # find number bigger than pivot point
            j -=1

        # swap pivot and the bigger value
        temp = nums[j]
        nums[j] = nums[k]
        nums[k] = temp

        left = k+1
        right = len(nums)-1
        while left < right: # reverse remaining everything after the pivot
            temp = nums[left]
            nums[left] = nums[right]
            nums[right] = temp
            left += 1
            right -=1

############## LOCAL TESTING ONLY ############################   
    def __init__(self, nums):
        self.nextPermutation(nums)

s = Solution([3,2,1])

"""
Runtime: 57 ms, faster than 9.45% of Python online submissions for Next Permutation.
Memory Usage: 13.3 MB, less than 70.49% of Python online submissions for Next Permutation.
"""