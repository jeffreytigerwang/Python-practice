# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        level = [root]
        ans = []
        zigzag = False

        while level:
            if zigzag:
                ans.append([node.val for node in reversed(level)])

            else:
                ans.append([node.val for node in level])

            temp = []
            for node in level:  # Update level directly (without temp) will result in infinite loop
                # temp.extend([node.left, node.right])
                temp.extend([node.left])
                temp.extend([node.right])

            level = [leaf for leaf in temp if leaf]
            zigzag = not zigzag

        return ans
def main():
    node9 = TreeNode(9)
    node15 = TreeNode(15)
    node7 = TreeNode(7)
    node20 = TreeNode(20, node15, node7)

    root = TreeNode(3, node9, node20)

    sol = Solution()
    print(sol.zigzagLevelOrder(root))
    # print(type(root))

if __name__ == "__main__":
    main()
