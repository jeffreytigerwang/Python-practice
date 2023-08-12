# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        curr = [root]
        res = []

        while curr:
            res.append([node.val for node in curr])

            temp = []

            for node in curr:
                temp.append(node.left)
                temp.append(node.right)

            curr = [node for node in temp if node]

        return res






def main():
    node9 = TreeNode(9)
    node15 = TreeNode(15)
    node7 = TreeNode(7)
    node20 = TreeNode(20, node15, node7)

    root = TreeNode(3, node9, node20)

    sol = Solution()
    print(sol.levelOrder(root))
    # print(type(root))


if __name__ == "__main__":
    main()
