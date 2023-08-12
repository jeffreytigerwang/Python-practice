# https://leetcode.com/problems/palindrome-linked-list/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
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

        l, r = head, dummy

        while head and dummy:
            if head.val != dummy.val:
                return False

            head = head.next
            dummy = dummy.next

        return True



def main():
    sol = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(1)
    head.next.next.next.next = ListNode(1)


    print(sol.isPalindrome(head))

if __name__ == "__main__":
    main()