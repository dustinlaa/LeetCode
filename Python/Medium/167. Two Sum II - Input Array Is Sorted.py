"""
167. Two Sum II - Input Array Is Sorted - https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/


Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.


Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
 

Constraints:

2 <= numbers.length <= 3 * 104
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.
"""
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers)-1
        while left < right:
            currSum = numbers[left] + numbers[right]
            if currSum == target: # found target
                return [left+1, right+1]
            elif currSum < target: # need larger value
                left +=1
            else: # need smaller value
                right -=1

        ### binary search ###
        # seen = []
        # for pos in range(len(numbers)): # going through every number in numbers
        #     if numbers[pos] not in seen:
        #         seen.append(numbers[pos])
        #         # first number is going to be number[pos], second number is between all the numbers after pos (inclusive)
        #         left = pos+1 
        #         right = len(numbers)-1
        #         secondVal = target - numbers[pos] # secondVal is our new target number to find
        #         while left <= right:
        #             mid = (left+right)//2 
        #             if numbers[mid] == secondVal: # found value
        #                 return [pos+1, mid+1]
        #             elif numbers[mid] < secondVal: # need to increase value
        #                 left = mid + 1
        #             else:
        #                 right = mid - 1 # need to decrease value
            
############## LOCAL TESTING ONLY ############################   
    def __init__(self, numbers, target):
        self.twoSum(numbers, target)

s = Solution([2,3,4], 6)

"""
Runtime: 148 ms, faster than 37.87% of Python online submissions for Two Sum II - Input Array Is Sorted.
Memory Usage: 14.5 MB, less than 23.87% of Python online submissions for Two Sum II - Input Array Is Sorted.
"""

### binary search ###
"""
Runtime: 97 ms, faster than 94.10% of Python online submissions for Two Sum II - Input Array Is Sorted.
Memory Usage: 15.3 MB, less than 6.26% of Python online submissions for Two Sum II - Input Array Is Sorted.
"""