from typing import Optional
from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        resListNode = ListNode()
        tail = resListNode

        temp1 = []
        temp2 = []

        head1 = l1
        head2 = l2

        while head1 is not None:
            temp1.append(head1.val)
            head1 = head1.next

        while head2 is not None:
            temp2.append(head2.val)
            head2 = head2.next

        temp1.reverse()
        temp2.reverse()

        s1 = [str(item) for item in temp1]
        s1 = "".join(s1)
        res1 = int(s1)

        s2 = [str(item) for item in temp2]
        s2 = "".join(s2)
        res2 = int(s2)

        res = res1 + res2

        res = list(str(res))
        res.reverse()

        print(res)

        for i in range(len(res)):
        # for i in res:
            if i >= len(res) - 1:
                tail.val = res[i]
                tail.next = None
            else:
                tail.val = res[i]
                tail.next = ListNode()
                tail = tail.next

        return resListNode

        # head = resListNode
        # while head:
        #     print(head.val)
        #     head = head.next

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
