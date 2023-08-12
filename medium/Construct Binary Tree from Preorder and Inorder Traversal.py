# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/solutions/34579/python-short-recursive-solution/
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return

        # print(preorder)
        # print(inorder)

        root = TreeNode(preorder[0])

        indexRoot = inorder.index(root.val)

        root.left = self.buildTree(preorder[1: indexRoot + 1], inorder[: indexRoot])
        root.right = self.buildTree(preorder[indexRoot + 1:], inorder[indexRoot + 1:])

        return root