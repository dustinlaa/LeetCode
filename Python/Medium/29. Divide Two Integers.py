"""
29. Divide Two Integers - https://leetcode.com/problems/divide-two-integers/


Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

Return the quotient after dividing dividend by divisor.

Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.

 
Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = 3.33333.. which is truncated to 3.
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = -2.33333.. which is truncated to -2.
 

Constraints:

-231 <= dividend, divisor <= 231 - 1
divisor != 0
"""
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = 1
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0): # output should be negative because there is only 1 negative
            sign = -1
        output = 0
        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend >= divisor:
            temp = divisor
            i = 1
            while dividend >= temp: 
                # by having this second while loop, we can subtract by bigger numbers, reducing time. 
                # If temp is bigger, needs to restart otherwise it will subtract too much 
                dividend -= temp # subtracts from dividend
                output += i # increase output by i (number of times divisor (temp) is going into dividend)
                i <<= 1 # i is left shifted by 1 (multiply by 2)
                temp <<= 1 # temp is left shifted by 1 (multiply by 2)
        if sign == -1:
            output = -output
        return min(max(-2**31,output), 2**31-1) # max between negative limit and our output and minimum between our output and the positive limit)


############## LOCAL TESTING ONLY ############################ 
    def __init__(self, dividend, divisor):
        self.divide(dividend, divisor)

s = Solution(-1000, -3)
#s = Solution(-2147483648, -1)

"""
Runtime: 32 ms, faster than 43.80% of Python online submissions for Divide Two Integers.
Memory Usage: 13.5 MB, less than 42.42% of Python online submissions for Divide Two Integers.
"""