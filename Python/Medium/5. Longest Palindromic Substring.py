"""
5. Longest Plaindromic Substring - https://leetcode.com/problems/longest-palindromic-substring/
Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        longest = ""
        def palindrome(string, i, j): # receives two numbers and spreads out until end of string is reached or no matching character
            while (i >= 0 and j < len(s) and s[i] == s[j]): 
                i -=1
                j +=1
            return string[i+1:j] # returns palindrome
        for i in range(len(s)): # gets all possible palindromes
            print("i: " + str(i))
            s1 = palindrome(s, i, i) # odd length string
            print("s1: " + s1)
            s2 = palindrome(s, i, i+1) # even length string, need an even length string in case the palindrome has an even length and not an odd length
            print("s2: " + s2)
            if len(longest) < len(s1):
                longest = s1
            if len(longest)  < len(s2):
                longest = s2
        return longest

############## LOCAL TESTING ONLY ############################ 
    def __init__(self, s):
        self.s = s
        self.longestPalindrome(s)

s = Solution("babadbbaabb")