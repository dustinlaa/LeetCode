"""
315. Count of Smaller Numbers After Self - https://leetcode.com/problems/count-of-smaller-numbers-after-self/


You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].


Example 1:

Input: nums = [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Example 2:

Input: nums = [-1]
Output: [0]
Example 3:

Input: nums = [-1,-1]
Output: [0,0]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
"""
import bisect
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        output = []
        sortedList = []
        for num in nums[::-1]: # goes right to left
            # print(f"num: {num}")
            pos = bisect.bisect_left(sortedList, num) # finds correct position to insert the num based on sortedList
            # print(f"pos: {pos}")
            output.append(pos) # this position is then added to the array because this position represents how many elements to the right are smaller
            # print(f"output: {output}")
            sortedList.insert(pos, num) # properly inserts the num into the sortedList
            # print(f"sortedList: {sortedList}")
        return output[::-1] # returns reversed output to properly match with original array

        # ### doesn't work for really large lists
        # output = []
        # if len(nums) == 1:
        #     return [0]
        # for i in range(len(nums)):
        #     window = sorted(nums[i:])
        #     output.append(window.index(nums[i]))
        # return output

############## LOCAL TESTING ONLY ############################   
    def __init__(self, nums):
        self.nums = nums
        self.countSmaller(nums)

s = Solution([5,2,6,1])

"""
Runtime: 3396 ms, faster than 50.48% of Python online submissions for Count of Smaller Numbers After Self.
Memory Usage: 31.8 MB, less than 88.94% of Python online submissions for Count of Smaller Numbers After Self.
"""