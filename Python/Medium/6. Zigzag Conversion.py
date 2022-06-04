"""
6. Zigzag conversion - https://leetcode.com/problems/zigzag-conversion/
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
 

Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
"""

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1: # if just 1 row, return string itself
            return s
        length = len(s)
        zig = [""]*numRows # creates an array to store each char from the zig zag
        currRow = 0 
        for i in range(length):
            zig[currRow] += s[i] # puts currennt char into correct position in  zig
            if currRow == numRows-1: #reached bottom, need to go up
                goingDown = False
            elif currRow == 0: # at top, need dto go down
                goingDown = True
            if goingDown: # going down, increase row
                currRow +=1
            else:
                currRow -=1 # going up, decrease row
            # it is storing the chars in the correct position by iterating through an array that has the numRows positions
            # for first char, it puts it in pos 0, next char in pos 1, etc til reaching the number of rows
            # then it works backwards. This creates the zigzag
        rtnString = ""
        for i in range(numRows):
            rtnString += zig[i]
        return rtnString
############## LOCAL TESTING ONLY ############################   
    def __init__(self, s, numRows):
        self.s = s
        self.numRows = numRows
        self.convert(s, numRows)

s = Solution("PAYPALISHIRING", 4)

"""
Runtime: 92 ms, faster than 46.96% of Python online submissions for Zigzag Conversion.
Memory Usage: 13.6 MB, less than 55.08% of Python online submissions for Zigzag Conversion.
"""