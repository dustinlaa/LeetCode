"""
11. Container With Most Water - https://leetcode.com/problems/container-with-most-water/


You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1

Constraints:

n == height.length
2 <= n <= 105
0 <= height[i] <= 104
"""

from matplotlib.font_manager import json_load


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea = 0
        left = 0  # left end
        right = len(height)-1 # right end
        while left != right: # continue until i == j
            if height[right] > height[left]: # left is the bottleneck
                area = height[left] * (right-left)  
                left += 1
            else: # j is the bottleneck
                area = height[right] * (right-left)
                right -= 1
            maxArea = max(maxArea, area) # get the bigger area
        return maxArea # return biggest area

############## LOCAL TESTING ONLY ############################   
    def __init__(self, height):
        self.height = height
        self.maxArea(height)

s = Solution([1,8,6,2,5,4,8,3,7])

"""
Runtime: 565 ms, faster than 94.57% of Python online submissions for Container With Most Water.
Memory Usage: 23.9 MB, less than 53.32% of Python online submissions for Container With Most Water.
"""