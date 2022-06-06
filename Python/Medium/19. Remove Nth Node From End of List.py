"""
19. Remove Nth Node From End of List - https://leetcode.com/problems/remove-nth-node-from-end-of-list/


Given the head of a linked list, remove the nth node from the end of the list and return its head.


Example 1:

Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fast = head # one node that will always be 1 position ahead of the other node
        slow = head # the node that will start after fast node is ahead
        for i in range(n): # fast gets the node in the nth position
            fast = fast.next
        if fast == None: # list is equal to or smaller than n, remove first node
            return head.next
        while fast.next: # continue down until reaching the end (this makes the slow node end up in the correct position because lengthOfList - n = length of fast)
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next # remove the nth node here and make the second node point to the following node (the node after the nth node), this also changes in head
        return head

############## LOCAL TESTING ONLY ############################   
    def __init__(self, head, n):
        self.removeNthFromEnd(head, n)

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
        
l1arr = [1,2,3,4,5]
l1 = create_linked_lst(l1arr)

s = Solution(l1, 2)

"""
Runtime: 34 ms, faster than 27.03% of Python online submissions for Remove Nth Node From End of List.
Memory Usage: 13.4 MB, less than 68.46% of Python online submissions for Remove Nth Node From End of List.
"""