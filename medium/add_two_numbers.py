from typing import Optional
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = ''
        s2 = ''

        temp = l1

        while temp:
            s1 += str(temp.val)
            temp = temp.next

        temp = l2

        while temp:
            s2 += str(temp.val)
            temp = temp.next

        s1 = reversed(s1)
        s2 = reversed(s2)

        sum = int(''.join(s1)) + int(''.join(s2))

        dummy = ListNode()
        temp = dummy

        for i in reversed(str(sum)):
            temp.next = ListNode(int(i))
            temp = temp.next

        return dummy.next



def main():
    l1_1 = ListNode(2)
    l1_2 = ListNode(4)
    l1_3 = ListNode(3)

    l1_1.next = l1_2
    l1_2.next = l1_3

    l2_1 = ListNode(5)
    l2_2 = ListNode(6)
    l2_3 = ListNode(4)

    l2_1.next = l2_2
    l2_2.next = l2_3

    addTwoNumbers = Solution()
    addTwoNumbers.addTwoNumbers(l1_1, l2_1)

    # head = l1_1
    # while head:
    #     print(head.val)
    #     head = head.next

if __name__ == "__main__":
    main()
