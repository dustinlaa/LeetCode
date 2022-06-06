"""
14. Longest Common Prefix - https://leetcode.com/problems/longest-common-prefix/

Write a function to find the longest common prefix string amongst an array of strings.


If there is no common prefix, return an empty string "".

 
Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
"""
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0: # no strings
            return ""
        smallestWord = min(strs, key=len) # finds smallest word
        for i in range((len(smallestWord))): # indexing through the smallest word
            for words in strs: # comparing to all the other words
                if words[i] != smallestWord[i]: # if a word doesnt have the same char as the smallestWord in the same pos, then return
                    return smallestWord[:i] # return everything up to this position
        return smallestWord # reached end, return the whole version of the smallest word

############## LOCAL TESTING ONLY ############################   
    def __init__(self, strs):
        self.strs = strs
        self.longestCommonPrefix(strs)

s = Solution(["flower","flow","flight"])

"""
Runtime: 19 ms, faster than 90.18% of Python online submissions for Longest Common Prefix.
Memory Usage: 13.7 MB, less than 62.57% of Python online submissions for Longest Common Prefix.
"""