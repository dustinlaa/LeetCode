"""
242. Valid Anagram - https://leetcode.com/problems/valid-anagram/


Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters
"""
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sSet = set(s)
        tSet = set(t) 
        if len(s) == len(t) and sSet == tSet:
            for char in sSet:
                if s.count(char) != t.count(char):
                    return False
            return True
        return False

############## LOCAL TESTING ONLY ############################ 
    def __init__(self, s, t):
        self.isAnagram(s, t)

s = Solution("anagram", "nagaram")

"""
Runtime: 35 ms, faster than 92.95% of Python online submissions for Valid Anagram.
Memory Usage: 14 MB, less than 57.18% of Python online submissions for Valid Anagram.
"""