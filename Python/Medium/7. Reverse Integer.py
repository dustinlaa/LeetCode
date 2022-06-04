"""
7. Reverse Integer - https://leetcode.com/problems/reverse-integer/

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = 1
        if x < 0:
            sign = -1
            x = x * sign
        result = 0
        while x > 0:
            print("x: " + str(x))
            result = result * 10 + x % 10 #  gets next digit and adds it to result. If result is not empty, result is multiplied by 10 to move the current ones place to the tens place
            print("currResult: " + str(result))
            if (result <= -2 ** 31 or result >= 2 **31):
                return 0
            x = x//10 # removes the ones place
        return sign * result

############## LOCAL TESTING ONLY ############################   
    def __init__(self, x):
        self.x = x
        self.reverse(x)

s = Solution(120)

"""
Runtime: 31 ms, faster than 40.65% of Python online submissions for Reverse Integer.
Memory Usage: 13.3 MB, less than 64.14% of Python online submissions for Reverse Integer.
"""