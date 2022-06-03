"""
2. Add Two Numbers.py - https://leetcode.com/problems/add-two-numbers/

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]

Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = ""
        num2 = ""
        while l1.next != None: # gets every value out of l1
            num1 += str(l1.val)
            l1 = l1.next
        num1 += str(l1.val)
        while l2.next != None: # gets every value out of l2
            num2 += str(l2.val)
            l2 = l2.next
        num2 += str(l2.val)

        num1 = num1[::-1] # reverses l1
        num1 = int(num1)
        num2 = num2[::-1] # reverses l2
        num2 = int(num2)

        sum = num1 + num2 # adds reversed l1 and reversed l2
        sum = str(sum)
        sum[::-1] # reverses sum
        length = len(sum)
        rtnList = ListNode()
        for i in range(length): # for every digit
            if i == length-1: # very last one, make the last node have this value
                rtnList.val = sum[i]
            else:
                temp = ListNode() # adds nodes in reverse
                temp.val = sum[i] # temp node gets the val and its next node points to the previous node's next
                temp.next = rtnList.next
                rtnList.next = temp # makes the temp node the next node 
        print(str(rtnList))
        return rtnList
    ##########################################
    def __init__(self, l1, l2):
        self.l1 = ListNode()
        self.l1 = l1
        self.l2 = ListNode()
        self.l2 = l2
        self.addTwoNumbers(l1, l2)

s = Solution([9,9,9,9,9,9,9], [9,9,9,9])

"""
Runtime: 88 ms, faster than 31.90% of Python online submissions for Add Two Numbers.
Memory Usage: 13.6 MB, less than 18.65% of Python online submissions for Add Two Numbers.
"""