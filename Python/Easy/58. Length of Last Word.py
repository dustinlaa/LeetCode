"""
58. Length of Last Word - https://leetcode.com/problems/length-of-last-word/


Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.


Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
 

Constraints:

1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.
"""
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s) # length of word
        count = 0
        wordFound = False
        for i in range(length-1, -1, -1): # work backwards 
            if s[i] != " ": # word found, repeat until end of word
                count += 1
                wordFound = True
                continue
            if wordFound == True: # word found, return true
                break
        return count

############## LOCAL TESTING ONLY ############################ 
    def __init__(self, s):
        self.lengthOfLastWord(s)

s = Solution("Hello World")

"""
Runtime: 23 ms, faster than 65.73% of Python online submissions for Length of Last Word.
Memory Usage: 13.9 MB, less than 6.99% of Python online submissions for Length of Last Word.
"""