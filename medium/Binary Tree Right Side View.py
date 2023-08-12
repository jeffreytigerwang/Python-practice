# https://leetcode.com/problems/binary-tree-right-side-view/
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        def levelOrderTraversal(root):
            res = []
            curr = [root]

            while curr:
                res.append([node.val for node in curr])

                temp = []

                for node in curr:
                    temp.extend([node.left, node.right])

                curr = [node for node in temp if node]

            return res

        res = [level[-1] for level in levelOrderTraversal(root)]

        return res
