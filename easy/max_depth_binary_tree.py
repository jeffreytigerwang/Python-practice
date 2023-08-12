# Definition for a binary tree node.
from typing import Optional


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # return max(self.maxDepth(root.left) + 1, self.maxDepth(root.right) + 1)
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1



b1 = TreeNode(9)
b2 = TreeNode(20)
root = TreeNode(3,b1,b2)
b2.left = TreeNode(15)
b2.right = TreeNode(7)

answer = Solution()
print(answer.maxDepth(root))
