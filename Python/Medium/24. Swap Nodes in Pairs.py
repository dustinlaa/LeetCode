"""
24. Swap Nodes in Pairs - https://leetcode.com/problems/swap-nodes-in-pairs/


Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.
 

Example 1:

Input: head = [1,2,3,4]
Output: [2,1,4,3]
Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [1]
Output: [1]
 

Constraints:

The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: # not enough nodes
            return head
        prev = ListNode() # stores previuos node
        prev.next = head
        curr = prev
        while curr.next and curr.next.next: # while we can swap
            first = curr.next # stores the next node
            second = curr.next.next  # stores the following node
            curr.next = second # sets the following node next
            first.next = second.next # makes the original node point to everything after the following node
            second.next = first # puts the original node after the following node
            curr = curr.next.next # continues
        return prev.next
        
        ### recursion solution ###
        # if head == None or head.next == None:
        #     return head
        # temp = ListNode()
        # temp = head.next
        # head.next = self.swapPairs(head.next.next)
        # temp.next = head
        # return temp

############## LOCAL TESTING ONLY ############################   
    def __init__(self, l1):
        self.swapPairs(l1)

class ListNode(object): # linked list object
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __repr__(self):
        output = []
        while self.next != None:
            output.append(int(self.val))
            self = self.next
        output.append(int(self.val))
        return str(output)

def create_linked_lst(lst): # creates linked lists from array
    linked_lst = None
    for item in reversed(lst):
        linked_lst = ListNode(item, linked_lst)
    return linked_lst
        
l1arr = [1,2,3,4]
l1 = create_linked_lst(l1arr)

s = Solution(l1)

"""
Runtime: 26 ms, faster than 45.19% of Python online submissions for Swap Nodes in Pairs.
Memory Usage: 13.3 MB, less than 81.35% of Python online submissions for Swap Nodes in Pairs.
"""