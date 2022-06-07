"""
21. Merge Two Sorted Lists - https://leetcode.com/problems/merge-two-sorted-lists/


You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.


Example 1:

Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = ListNode() # creates a new list
        currNode = head # sets current node to head
        while list1 and list2: # while there are nodes in both in lists
            if list1.val < list2.val: # list1 node goes first
                currNode.next = list1
                list1 = list1.next
            else:
                currNode.next = list2 # list2 node goes first
                list2 = list2.next
            currNode = currNode.next
        if list1: # remaining nodes in list1
            currNode.next = list1
        else: # remaining nodes in list2
            currNode.next = list2
        return head.next # return the first node which is located after head

############## LOCAL TESTING ONLY ############################   
    def __init__(self, l1, l2):
        self.mergeTwoLists(l1, l2)

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
        
l1arr = [1,2,4]
l1 = create_linked_lst(l1arr)
l2arr = [1,2,4]
l2 = create_linked_lst(l2arr)

s = Solution(l1, l2)

"""
Runtime: 36 ms, faster than 40.19% of Python online submissions for Merge Two Sorted Lists.
Memory Usage: 13.6 MB, less than 33.71% of Python online submissions for Merge Two Sorted Lists.
"""
