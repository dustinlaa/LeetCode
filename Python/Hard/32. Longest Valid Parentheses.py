"""
32. Longest Valid Parentheses - https://leetcode.com/problems/longest-valid-parentheses/


Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.


Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 3 * 104
s[i] is '(', or ')'.

"""
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [-1]
        valid = 0
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i) # stores position of open which represents potential valid parentheses
            else: # if there are 2 elements in stack here, that means a valid parentheses was made
                stack.pop() # removes the last valid parentheses position if it exists, otherwise it would empty the stack
                if not stack: # if stack is empty, that means we have no valid parentheses and need to restart the streak
                    stack.append(i) # stores position of close (restarts valid parentheses because the streak is over)
                else:
                    #print(str(stack[-1]))
                    valid = max(valid, i-stack[-1]) # gets the maximum value between the current highest valid and i-stack[-1]
                                                    # stack[-1] represents the last valid streak beginning
                                                    # i represents current position
        return valid

############## LOCAL TESTING ONLY ############################   
    def __init__(self, s):
        self.longestValidParentheses(s)

s = Solution(")()())()")

"""
Runtime: 42 ms, faster than 59.75% of Python online submissions for Longest Valid Parentheses.
Memory Usage: 14.1 MB, less than 48.78% of Python online submissions for Longest Valid Parentheses.
"""