# https://leetcode.com/problems/copy-list-with-random-pointer/

"""
# Definition for a Node.
"""
import copy
from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #   My approach, O(n^2)
        # if not head:
        #     return
        #
        # if not head.next:
        #     copyHead = Node(head.val)
        #
        #     if head.random:
        #         copyHead.random = copyHead
        #     return copyHead
        #
        # tempHead = head
        # tempHead = tempHead.next
        #
        # copyHead = Node(head.val)
        # tempCopyHead = copyHead
        #
        # while tempHead:
        #     tempNode = Node(tempHead.val)
        #     tempCopyHead.next = tempNode
        #     tempCopyHead = tempCopyHead.next
        #
        #     tempHead = tempHead.next
        #
        # tempHead = head
        # tempCopyHead = copyHead
        #
        # while tempHead:
        #     # print("Inside while tempHead")
        #     if tempHead.random:
        #         # print("Inside if tempHead.random exist")
        #         searchHead = head
        #         index = 0
        #         while searchHead:
        #
        #
        #             if searchHead != tempHead.random:
        #                 # print("Inside searchHead != tempHead.random")
        #                 index += 1
        #                 searchHead = searchHead.next
        #
        #             else:
        #                 # print(index)
        #                 searchCopyHead = copyHead
        #                 for i in range(index):
        #                     searchCopyHead = searchCopyHead.next
        #
        #                 # print("Inside else")
        #                 tempCopyHead.random = searchCopyHead
        #                 break
        #
        #     tempHead = tempHead.next
        #     tempCopyHead = tempCopyHead.next

        #   https://leetcode.com/problems/copy-list-with-random-pointer/solutions/373694/python3-dictionary/

        if not head:
            return None

        nodeDict = {}
        curr = head

        while curr:
            nodeDict[curr] = Node(curr.val)
            curr = curr.next

        curr = head

        while curr:
            if curr.next:
                nodeDict[curr].next = nodeDict[curr.next]

            if curr.random:
                nodeDict[curr].random = nodeDict[curr.random]

            curr = curr.next

        return nodeDict[head]

        # while copyHead:
        #     print(copyHead.val)
        #
        #     if not copyHead.random:
        #         print("Null")
        #     else:
        #         print(copyHead.random.val)
        #
        #     print()
        #     copyHead = copyHead.next

        return copyHead


sol = Solution()

head = Node(7)
node13 = Node(13)
node11 = Node(11)
node10 = Node(10)
node1 = Node(1)

head.next = node13

node13.next = node11
node13.random = head

node11.next = node10
node11.random = node1

node10.next = node1
node10.random = node11

node1.random = head

# while head:
#     print(head.val)
#
#     if not head.random:
#         print("Null")
#     else:
#         print(head.random.val)
#
#     print()
#
#     head = head.next

sol.copyRandomList(head)
