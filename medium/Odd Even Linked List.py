# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        count = 0
        tempHead = head
        tempLast = head
        tempNode = head

        # print(head.val)
        if head is None:
            return head

        while tempLast.next:
            count = count + 1
            tempLast = tempLast.next

        if count <= 1:
            return head

        for i in range(count + 1):
            if i % 2 != 0:
                tempLast.next = tempNode
                tempLast = tempLast.next

            tempNode = tempNode.next

            if i % 2 == 0 and i < count:
                tempHead.next = tempHead.next.next
                tempHead = tempHead.next

        tempLast.next = None
        return head