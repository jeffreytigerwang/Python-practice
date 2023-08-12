# https://leetcode.com/problems/delete-node-in-a-bst/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return

        if root.val < key:
            root.right = self.deleteNode(root.right, key)
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                # have left and right --> replace the node that is going to be deleted with the min node in right subtree
                curr = root.right

                while curr.left:
                    curr = curr.left

                root.val = curr.val

                # delete the min node in right subtree as it is now moved to the deleted node's position
                root.right = self.deleteNode(root.right, root.val)

        return root
