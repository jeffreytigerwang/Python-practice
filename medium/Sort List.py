# https://leetcode.com/problems/sort-list/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        left = head
        right = self.findMid(head)
        temp = right.next
        right.next = None
        right = temp

        left = self.sortList(left)
        right = self.sortList(right)

        return self.merge(left, right)

    def findMid(self, head):
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def merge(self, list1, list2):
        start = ListNode()
        tempNode = start

        while list1 and list2:
            if list1.val > list2.val:
                tempNode.next = list2
                list2 = list2.next
            else:
                tempNode.next = list1
                list1 = list1.next

            tempNode = tempNode.next

        if list1:
            tempNode.next = list1

        if list2:
            tempNode.next = list2

        return start.next

def main():
    node3 = ListNode(3)
    node2 = ListNode(1, node3)
    node1 = ListNode(2,node2)
    root = ListNode(4, node1)

    sol = Solution()
    sol.sortList(root)


if __name__ == "__main__":
    main()