"""
17. Letter Combinations of a Phone Number - https://leetcode.com/problems/letter-combinations-of-a-phone-number/


Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
 

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].
"""
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        numToLetter = { # translates num to letters
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        output = []
        if len(digits) == 0: # no digits
            return output
        self.findCombo(digits, 0, numToLetter, "", output)
        return output

    def findCombo(self, digits, index, numToLetter, path, output): # finds all the possible combinations
        if index >= len(digits): # index is bigger than the number of digits (found end of combination)
            output.append(path)
            return
        currString = numToLetter[digits[index]] # gets the string of a number (if digits[2], then it goes to 2 and gets "abc")
        for letter in currString: # goes through each letter in that string
            self.findCombo(digits, index+1, numToLetter, path + letter, output) # adds to path to add to combination and increments index to grab next letter

   ############## LOCAL TESTING ONLY ############################        
    def __init__(self, digits):
        self.letterCombinations(digits)

s = Solution("236")

"""
Runtime: 35 ms, faster than 12.15% of Python online submissions for Letter Combinations of a Phone Number.
Memory Usage: 13.6 MB, less than 15.53% of Python online submissions for Letter Combinations of a Phone Number.
"""