# https://leetcode.com/problems/insert-into-a-binary-search-tree/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Recursive
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right,val)

        return root


# Iterative
class Solution1:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        prev, curr = None, root

        while curr:
            prev = curr
            curr = curr.left if curr.val > val else curr.right

        if prev.val < val:
            prev.right = TreeNode(val)
        else:
            prev.left = TreeNode(val)

        return root