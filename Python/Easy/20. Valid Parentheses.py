"""
20. Valid Parentheses - https://leetcode.com/problems/valid-parentheses/


Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for char in s:
            if char == "(" or char == "{" or char == "[":
                stack.append(char)
            else:
                if len(stack) < 1:
                    return False
                if char == ")":
                    if stack.pop() != "(":
                        return False
                elif char == "}":
                    if stack.pop() != "{":
                        return False
                elif char == "]":
                    if stack.pop() != "[":
                        return False
        if len(stack) == 0:
            return True
        return False

############## LOCAL TESTING ONLY ############################        
    def __init__(self, s):
        self.isValid(s)

s = Solution("()")


"""
Runtime: 28 ms, faster than 42.87% of Python online submissions for Valid Parentheses.
Memory Usage: 13.6 MB, less than 33.86% of Python online submissions for Valid Parentheses.
"""