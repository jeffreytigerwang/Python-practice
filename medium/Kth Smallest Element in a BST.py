# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root, k):
        # recursive

        # count = 1
        # res = 0
        #
        # def inOrderTraversal(root):
        #     nonlocal count
        #     nonlocal res
        #
        #     if root:
        #         inOrderTraversal(root.left)
        #         if count == k:
        #             print(root.val)
        #             count += 1
        #             res = root.val
        #         else:
        #             count += 1
        #         inOrderTraversal(root.right)
        #
        # inOrderTraversal(root)
        #
        # return res


        # iterative

        curr = root
        temp = []
        count = 0

        while curr or temp:
            while curr: # visit all left subtrees/nodes
                temp.append(curr)
                curr = curr.left

            curr = temp.pop()   # visit the list from small to large
            count += 1

            if count == k:
                return curr.val

            curr = curr.right   # start to visit right subtrees/nodes






sol = Solution()

root = TreeNode(3)
root.left = TreeNode(1)
root.left.right = TreeNode(2)
root.right = TreeNode(4)

print(sol.kthSmallest(root, 1))