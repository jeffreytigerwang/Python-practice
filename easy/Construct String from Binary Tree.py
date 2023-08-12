# https://leetcode.com/problems/construct-string-from-binary-tree/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        res = ''

        def inorderDFS(node):
            nonlocal res
            if not node:
                return

            res += str(node.val)

            if not node.left and not node.right:
                return

            # must process left unless both left and right are none
            res += '('
            inorderDFS(node.left)
            res += ')'

            if node.right:
                res += '('
                inorderDFS(node.right)
                res += ')'

        inorderDFS(root)
        return res