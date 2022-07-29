"""
890. Find and Replace Pattern - https://leetcode.com/problems/find-and-replace-pattern/

Given a list of strings words and a string pattern, return a list of words[i] that match pattern. You may return the answer in any order.

A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.

 
Example 1:

Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}. 
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation, since a and b map to the same letter.
Example 2:

Input: words = ["a","b","c"], pattern = "a"
Output: ["a","b","c"]
 

Constraints:

1 <= pattern.length <= 20
1 <= words.length <= 50
words[i].length == pattern.length
pattern and words[i] are lowercase English letters.
"""
class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        output = []
        for word in words:
            newWord = ""
            translation = {}
            if len(word) == len(pattern): # pattern and word have same length (same number of letters)
                for i in range(len(pattern)):
                    if pattern[i] not in translation: # add to dictionary
                        translation[pattern[i]] = word[i] 
                    newWord += translation[pattern[i]] # recreate the word based on pattern to word translation
                if newWord == word and len(translation) == len(set(word)): # word is the same and it is the same number of letters
                    output.append(word) # add to output
        return output

############## LOCAL TESTING ONLY ############################ 
    def __init__(self, words, pattern):
        self.findAndReplacePattern(words,pattern)

s = Solution(["abc","deq","mee","aqq","dkd","ccc"], "abb")

"""
Runtime: 18 ms, faster than 93.50% of Python online submissions for Find and Replace Pattern.
Memory Usage: 13.4 MB, less than 60.16% of Python online submissions for Find and Replace Pattern.
"""