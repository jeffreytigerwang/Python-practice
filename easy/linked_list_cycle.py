# Floyd’s Cycle-Finding Algorithm // fast slow approach // 2 pointers // "tortoise and the hare algorithm"
#
# Approach: This is the fastest method and has been described below:
#
# Traverse linked list using two pointers.
#
# Move one pointer(slow_p) by one and another pointer(fast_p) by two.
#
# If these pointers meet at the same node then there is a loop. If pointers do not meet then linked list doesn’t have a loop.


from typing import Optional


# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False

        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

        return False


node1 = ListNode(1)
node2 = ListNode(2)
node1.next = node2

print(node1.next.val)