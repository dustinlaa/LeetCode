"""
9. Palindrome Number.py - https://leetcode.com/problems/palindrome-number/


Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.
 
Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
"""
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x > 0 and x%10 == 0): # if x is negative or if x is positive and the last digit is a 0 --> can't be a palindrome
            return False
        result = 0 
        while x > result:
            result = result*10 + x%10 # reverses number by adding the current one's place and multiplying result by 10 to move the ones place to the tens place
            x = x//10 # removes one place
        if result == x or x == result//10:
            return True
        return False
############## LOCAL TESTING ONLY ############################   
    def __init__(self, x):
        self.x = x
        self.isPalindrome(x)

s = Solution(121)

"""
Runtime: 75 ms, faster than 59.28% of Python online submissions for Palindrome Number.
Memory Usage: 13.3 MB, less than 86.51% of Python online submissions for Palindrome Number.
"""