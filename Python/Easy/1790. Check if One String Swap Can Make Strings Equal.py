"""
1790. Check if One String Swap Can Make Strings Equal - https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/


You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings. Otherwise, return false.

 
Example 1:

Input: s1 = "bank", s2 = "kanb"
Output: true
Explanation: For example, swap the first character with the last character of s2 to make "bank".
Example 2:

Input: s1 = "attack", s2 = "defend"
Output: false
Explanation: It is impossible to make them equal with one string swap.
Example 3:

Input: s1 = "kelb", s2 = "kelb"
Output: true
Explanation: The two strings are already equal, so no string swap operation is required.
 

Constraints:

1 <= s1.length, s2.length <= 100
s1.length == s2.length
s1 and s2 consist of only lowercase English letters.
"""

class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == s2: # strings are equal
            return True
        diffs = 0
        pos1 = 0
        pos2 = 0
        for i in range(len(s1)): # goes through each char
            if s1[i] != s2[i]: # difference spotted
                diffs +=1
                if diffs == 1: # only one difference, save first index
                    pos1 = i
                else: # second difference spotted, save second index
                    pos2 = i
                if diffs > 2: # more than two differences, return false
                    return False
        if diffs == 2 and s1[pos1] == s2[pos2] and s1[pos2] == s2[pos1]: # if there are only 2 differences and the characters match, it is a one swap
            return True
        return False
    
############## LOCAL TESTING ONLY ############################        
    def __init__(self, s1, s2):
        self.areAlmostEqual(s1, s2)

s = Solution("bank","kanb")

"""
Runtime: 21 ms, faster than 73.87% of Python online submissions for Check if One String Swap Can Make Strings Equal.
Memory Usage: 13.7 MB, less than 11.41% of Python online submissions for Check if One String Swap Can Make Strings Equal.
"""