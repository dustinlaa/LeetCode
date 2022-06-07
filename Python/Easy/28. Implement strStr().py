"""
28. Implement strStr() - https://leetcode.com/problems/implement-strstr/


Implement strStr().

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
 

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
 

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack) - len(needle)+1): # finds everything up to the last possible starting point
            if haystack[i:i+len(needle)] == needle: # if selection is needle
                return i
        return -1

        # if needle in haystack:
        #     return haystack.index(needle)
        # return -1

############## LOCAL TESTING ONLY ############################   
    def __init__(self, haystack, needle):
        self.strStr(haystack, needle)

s = Solution("heoll", "ll")

"""
Runtime: 17 ms, faster than 80.23% of Python online submissions for Implement strStr().
Memory Usage: 13.7 MB, less than 10.64% of Python online submissions for Implement strStr().
"""