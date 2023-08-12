# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if not head:
            return 0

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        dummy = None

        while slow:
            temp = slow.next
            slow.next = dummy
            dummy = slow
            slow = temp

        res = 0

        while dummy and head:
            res = max(res, dummy.val + head.val)
            dummy = dummy.next
            head = head.next

        return res




sol = Solution()
head = ListNode(5)
head.next = ListNode(4)
head.next.next = ListNode(2)
head.next.next.next = ListNode(1)
# head.next.next.next.next = ListNode(0)
# head.next.next.next.next.next = ListNode(100)

sol.pairSum(head)