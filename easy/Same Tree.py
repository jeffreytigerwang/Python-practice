# https://leetcode.com/problems/same-tree/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # def helper(p, q):
        #
        #     if not p and not q:
        #         return True
        #
        #     # if not p and q or not q and p:
        #     #     return False
        #
        #     if q and p:
        #         if q.val != p.val:
        #             return False
        #         else:
        #             return helper(p.left, q.left) and helper(p.right, q.right)
        #     else:
        #         return False
        #
        # return helper(p, q)

        if not p and not q:
            return True

        if p and q:
            if p.val == q.val:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            else:
                return False
        else:
            return False
