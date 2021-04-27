# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def printNode(self):
        temp = self.head
        while temp:
            print(temp.val)
            temp = temp.next


class Solution(object):
    def removeElements(self, head, val):
        while head and head.val == val:
            head = head.next

        temp = head

        while temp is not None:
            if temp.next is not None and temp.next.val == val:
                temp.next = temp.next.next
            else:
                temp = temp.next

        return head



node7 = ListNode(6)
node6 = ListNode(5, node7)
node5 = ListNode(4, node6)
node4 = ListNode(3, node5)
node3 = ListNode(6, node4)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)
answer = Solution()
LL1 = LinkedList(answer.removeElements(node1, 6))

LL1.printNode()