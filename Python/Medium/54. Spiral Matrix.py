"""
54. Spiral Matrix - https://leetcode.com/problems/spiral-matrix/

Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        output = []
        top = 0
        bottom = len(matrix) # bottom level
        left = 0
        right = len(matrix[0]) # right level
        
        while left < right and top < bottom: # while in bounds
            for i in range(left, right): # moving to the left
                output.append(matrix[top][i])
            top += 1 # done with top most layer
            for i in range(top, bottom): # moving down
                output.append(matrix[i][right-1]) # -1 to stay in bounds
            right -= 1 # done with right most layer
            if not (left < right and top < bottom): # in case we reach the end 
                break
            for i in range(right-1, left-1, -1): # moving right
                output.append(matrix[bottom-1][i]) # -1 to stay in bounds
            bottom -=1 # done with bottom most layer
            for i in range(bottom-1, top-1, -1): # moving up
                output.append(matrix[i][left])
            left += 1
        return output

############## LOCAL TESTING ONLY ############################ 
    def __init__(self, matrix):
        self.spiralOrder(matrix)

s = Solution([[1,2,3,4],[5,6,7,8],[9,10,11,12]])