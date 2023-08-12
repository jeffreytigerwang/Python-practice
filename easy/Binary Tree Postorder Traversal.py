# https://leetcode.com/problems/binary-tree-postorder-traversal/
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def recursive(root):
            if root:
                recursive(root.left)
                recursive(root.right)
                res.append(root.val)

        recursive(root)
        return res
