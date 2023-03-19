# https://leetcode.com/problems/intersection-of-two-linked-lists/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        m = 0
        n = 0

        tempA = headA
        tempB = headB

        while tempA is not None:
            m += 1
            tempA = tempA.next

        while tempB is not None:
            n += 1
            tempB = tempB.next

        tempA = headA
        tempB = headB

        if m > n:
            while m > n:
                m -= 1
                tempA = tempA.next
        elif n > m:
            while n > m:
                n -= 1
                tempB = tempB.next

        while tempA is not None:
            if tempA == tempB:
                return tempA

            tempA = tempA.next
            tempB = tempB.next

        # print(tempA.val)
        # print(tempB.val)


        return None


