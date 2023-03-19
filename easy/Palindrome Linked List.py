# https://leetcode.com/problems/palindrome-linked-list/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        #
        # tempHead = head
        # tempList = []
        #
        # while tempHead:
        #     tempList.append(tempHead.val)
        #     tempHead = tempHead.next
        #
        # rightIndex = len(tempList) // 2
        #
        # if len(tempList) % 2 == 0:
        #     leftIndex = rightIndex - 1
        # else:
        #     leftIndex = rightIndex
        #
        # while leftIndex >= 0 and rightIndex < len(tempList):
        #     if tempList[rightIndex] == tempList[leftIndex]:
        #         rightIndex += 1
        #         leftIndex -= 1
        #         continue
        #     else:
        #         return False
        #
        # return True

        fast, slow = head, head
        rev = None

        while fast and fast.next:
            fast = fast.next.next

            # temp = rev
            # rev = slow
            # slow = slow.next    #reverse line 47 and 48 will result in an error as assigning rev.next to temp means slow.next = temp and, later, slow = slow.next means slow = temp, which is None
            # rev.next = temp

            rev, rev.next, slow = slow, rev, slow.next

        if fast:
            slow = slow.next

        while rev and rev.val == slow.val:
            rev = rev.next
            slow = slow.next

        return not rev
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