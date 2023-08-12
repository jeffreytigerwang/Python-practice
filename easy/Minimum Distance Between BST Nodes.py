# https://leetcode.com/problems/minimum-distance-between-bst-nodes/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        prev, res = None, float('inf')

        def dfs(root):
            if root:
                nonlocal prev, res

                dfs(root.left)

                if prev:
                    res = min(res, root.val - prev.val)

                prev = root
                dfs(root.right)

        dfs(root)

        return res
