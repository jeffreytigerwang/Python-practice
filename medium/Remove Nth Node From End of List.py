# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

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

        count = 0
        tempNode = head

        while tempNode.next is not None:
            count = count + 1
            tempNode = tempNode.next

        if n == count + 1:
            return head.next

        tempNode = head

        while (count - n) > 0:
            tempNode = tempNode.next
            count = count - 1

        tempNode.next = tempNode.next.next
        return head