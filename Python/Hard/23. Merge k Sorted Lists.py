"""
23. Merge k Sorted Lists - https://leetcode.com/problems/merge-k-sorted-lists/


You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 
Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []
 

Constraints:

k == lists.length
0 <= k <= 104
0 <= lists[i].length <= 500
-104 <= lists[i][j] <= 104
lists[i] is sorted in ascending order.
The sum of lists[i].length will not exceed 104.
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2
        left, right = self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:]) # divide and conquer, it is splitting the lists in half until you get a left half and right half that has one list each
        return self.merge(left, right) # merge the two lsits
    
    def merge(self, left, right):
        head = ListNode() # creates a new list
        currNode = head # sets current node to head
        while left and right: # while there are nodes in both lists
            if left.val < right.val: # list1 node goes first
                currNode.next = left
                left = left.next
            else:
                currNode.next = right # list2 node goes first
                right = right.next
            currNode = currNode.next
        if left:
            currNode.next = left # remaining nodes in list1
        else:
            currNode.next = right # remaining nodes in list2
        return head.next # return the first node which is located after head

############## LOCAL TESTING ONLY ############################   
    def __init__(self, lists):
        self.mergeKLists(lists)

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
        
l1arr = [1,4,5]
l1 = create_linked_lst(l1arr)
l2arr = [1,3,4]
l2 = create_linked_lst(l2arr)
l3arr = [2,6]
l3 = create_linked_lst(l3arr)
lists = [l1, l2, l3]
s = Solution(lists)

"""
Runtime: 99 ms, faster than 80.28% of Python online submissions for Merge k Sorted Lists.
Memory Usage: 19.5 MB, less than 86.95% of Python online submissions for Merge k Sorted Lists.
"""