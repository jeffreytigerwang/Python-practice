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
        if not head:
            return head

        deepCopyDict = {}
        temp = head

        while temp:
            deepCopyDict[temp] = Node(temp.val)
            temp = temp.next

        # for key in deepCopyDict.keys():
        #     print(deepCopyDict[key].val)

        temp = head

        while temp:
            if temp.next:
                deepCopyDict[temp].next = deepCopyDict[temp.next]

            if temp.random:
                deepCopyDict[temp].random = deepCopyDict[temp.random]

            temp = temp.next

        return deepCopyDict[head]




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
