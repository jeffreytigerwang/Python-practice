# https://leetcode.com/problems/path-sum/description/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, currSum):
            if not node:
                return False

            currSum += node.val

            if not node.left and not node.right and currSum == targetSum:
                return True

            left = dfs(node.left, currSum)
            right = dfs(node.right, currSum)

            return left or right

        return dfs(root, 0)