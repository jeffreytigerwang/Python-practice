# https://leetcode.com/problems/reverse-linked-list/description/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if not head or not head.next:
        #     return head
        #
        # prev = None
        # curr = head
        #
        # while curr:
        #     temp = curr.next
        #     curr.next = prev
        #     prev = curr
        #
        #     curr = temp
        #
        # return prev

        if not head:
            return None

        newHead = head
        # print(newHead.val)

        if head.next:
            newHead = self.reverseList(head.next)
            # print(newHead.val)
            head.next.next = head

        head.next = None

        return newHead


sol = Solution()
head = ListNode(0)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head.next.next.next.next = ListNode(4)
head.next.next.next.next.next = ListNode(5)

sol.reverseList(head)