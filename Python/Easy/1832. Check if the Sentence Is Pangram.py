"""
1832. Check if the Sentence Is Pangram - https://leetcode.com/problems/check-if-the-sentence-is-pangram/

A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

 

Example 1:

Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.
Example 2:

Input: sentence = "leetcode"
Output: false
 

Constraints:

1 <= sentence.length <= 1000
sentence consists of lowercase English letters.
"""
class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        if len(sentence) < 26:
            return False
        alphabet = []
        for char in sentence:
            if char not in alphabet:
                alphabet.append(char)
            if len(alphabet) == 26:
                return True
        return False

    ### alt solution ###
    # return len(set(sentence)) == 26
    
############## LOCAL TESTING ONLY ############################   
    def __init__(self, s):
        self.checkIfPangram(s)

s = Solution("thequickbrownfoxjumpsoverthelazydog")


"""
Runtime: 16 ms, faster than 86.92% of Python online submissions for Check if the Sentence Is Pangram.
Memory Usage: 13.4 MB, less than 62.31% of Python online submissions for Check if the Sentence Is Pangram.
"""