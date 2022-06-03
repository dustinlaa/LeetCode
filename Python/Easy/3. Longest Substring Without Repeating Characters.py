"""
3. Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        currString = ""
        longest = 0
        for char in s:
            if char in currString:
                currString = currString[currString.index(char)+1:]
            currString += char
            if len(currString) > longest:
                longest = len(currString)
        return longest
    ##########################################
    def __init__(self, s):
        self.s = s
        self.lengthOfLongestSubstring(s)
    
s = Solution("abcabcbb")

"""
Runtime: 39 ms, faster than 93.76% of Python online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 13.8 MB, less than 54.36% of Python online submissions for Longest Substring Without Repeating Characters.
"""