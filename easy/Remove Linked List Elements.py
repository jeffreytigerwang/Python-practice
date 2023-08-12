# https://leetcode.com/problems/remove-linked-list-elements/
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = head
        prev = dummy

        while curr:
            # temp = curr.next

            if curr.val == val:
                prev.next = curr.next
            else:
                # update prev when we do not need to remove the node (curr.val != val)
                prev = curr

            curr = curr.next

        return dummy.next