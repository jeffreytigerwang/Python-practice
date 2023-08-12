# https://leetcode.com/problems/reorder-list/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head

        mid = self.findMid(head)
        reversedList = mid.next
        mid.next = None

        prev = None
        curr = reversedList

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr

            curr = temp

        tempHead = ListNode()
        dummy = tempHead

        # while prev:
        #     print(prev.val)
        #     prev = prev.next

        while head and prev:
            dummy.next = head
            head = head.next
            dummy = dummy.next

            dummy.next = prev
            prev = prev.next

            dummy = dummy.next

        if head:
            dummy.next = head
        else:
            dummy.next = prev

        # while tempHead:
        #     print(tempHead.val)
        #     tempHead = tempHead.next

        return tempHead.next



    def findMid(self, head):
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


sol = Solution()
head = ListNode(0)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(5)

sol.reorderList(head)