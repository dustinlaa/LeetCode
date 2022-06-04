"""
8. String to Integer (atoi) - https://leetcode.com/problems/string-to-integer-atoi/

Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.
Note:

Only the space character ' ' is considered a whitespace character.
Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.
 

Example 1:

Input: s = "42"
Output: 42
Explanation: The underlined characters are what is read in, the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
           ^
The parsed integer is 42.
Since 42 is in the range [-231, 231 - 1], the final result is 42.
Example 2:

Input: s = "   -42"
Output: -42
Explanation:
Step 1: "   -42" (leading whitespace is read and ignored)
            ^
Step 2: "   -42" ('-' is read, so the result should be negative)
             ^
Step 3: "   -42" ("42" is read in)
               ^
The parsed integer is -42.
Since -42 is in the range [-231, 231 - 1], the final result is -42.
Example 3:

Input: s = "4193 with words"
Output: 4193
Explanation:
Step 1: "4193 with words" (no characters read because there is no leading whitespace)
         ^
Step 2: "4193 with words" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "4193 with words" ("4193" is read in; reading stops because the next character is a non-digit)
             ^
The parsed integer is 4193.
Since 4193 is in the range [-231, 231 - 1], the final result is 4193.
 

Constraints:

0 <= s.length <= 200
s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.
"""

class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0 # final result
        sign = 1 # sets sign to 1 for positive
        pos = 0 # position index
        length = len(s)
        while pos < length and s[pos] == " ": # space found, just continue down
            pos +=1
        if pos < length and s[pos] == "+": # plus found, make number positive
            sign = 1
            pos +=1
        elif pos < length and s[pos] == "-": # negative foud, make number negative
            sign = -1
            pos +=1
        while pos < length and s[pos].isdigit(): # only check for numbers now
            currNum = int(s[pos]) # gets current number
            # for last digit if the result is bigger than 214748364 (the limit is 2147483647) or if current result is equal to 214748364 and the next num is bigger than 7
            # if result > 214748364 or result == 214748364 and currNum > 7
            if (result > ((2**31)-1)//10) or (result == ((2**31)-1)//10  and currNum > (((2**31)-1) % 10)):
                if sign == 1:
                    return ((2**31)-1)
                else:
                    return -2**31
            else:
                result = 10*result + currNum # adds current number to result, multiplies ones place by 10 to move it to the tens place
                pos +=1
        return sign * result

############## LOCAL TESTING ONLY ############################   
    def __init__(self, s):
        self.s = s
        self.myAtoi(s)

s = Solution("2147483646")

"""
Runtime: 42 ms, faster than 22.86% of Python online submissions for String to Integer (atoi).
Memory Usage: 13.4 MB, less than 93.61% of Python online submissions for String to Integer (atoi).
"""