# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
from typing import Optional


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # dummy = ListNode(0, head)
        # l = dummy
        # r = head
        #
        # while r and n > 0:
        #     n -= 1
        #     r = r.next
        #
        # while r and l:
        #     r = r.next
        #     l = r.next
        #
        # l.next = l.next.next
        #
        # return dummy.next

        count = 0
        temp = head

        while temp:
            count += 1
            temp = temp.next

        # print(count)

        if count == n:
            return head.next

        temp = head
        diff = count - n

        while diff - 1 > 0:
            temp = temp.next
            diff -= 1

        temp.next = temp.next.next

        return head


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

sol = Solution()

sol.removeNthFromEnd(head, 2)