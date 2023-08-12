from typing import Optional
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def recursive(root):
            if root:
                recursive(root.left)
                res.append(root.val)
                recursive(root.right)

        recursive(root)
        return res





node1 = [1]
node2 = [2]

node3 = [1] + [2]

print(node3)