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
        # if len(preorder) == 0:
        #     return
        #
        # if len(preorder) == 1:
        #     return TreeNode(preorder[0])
        #
        # root = TreeNode(preorder[0])
        #
        # leftInOrder = inorder[: inorder.index(preorder[0])]
        # rightInOrder = inorder[inorder.index(preorder[0]) + 1:]
        #
        # leftPreOrder = preorder[1: len(leftInOrder) + 1]
        # rightPreOrder = preorder[1 + len(leftInOrder): ]
        #
        # root.left = self.buildTree(leftPreOrder, leftInOrder)
        # root.right = self.buildTree(rightPreOrder, rightInOrder)
        #
        #
        # return root

        inorderDict = {}

        for i, num in enumerate(inorder):
            inorderDict[num] = i

        preorderIndex = 0

        def helper(startIndex, endIndex):
            nonlocal preorderIndex

            if startIndex > endIndex:
                return

            rootValue = preorder[preorderIndex]
            root = TreeNode(rootValue)

            preorderIndex += 1

            root.left = helper(startIndex, inorderDict[rootValue] - 1)  # inorderDict[rootValue] - 1: because it is a helper function, not slicing list!
            root.right = helper(inorderDict[rootValue] + 1, endIndex)   # - 1 and + 1 : help to exclude inorderDict[rootValue]

            return root

        return helper(0, len(inorder) - 1)