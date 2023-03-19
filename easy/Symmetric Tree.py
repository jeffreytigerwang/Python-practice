# https://leetcode.com/problems/symmetric-tree/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def helper(left, right):
            if not left and not right:
                return True

            if not left or not right:
                return False

            if left.val == right.val:
                outPair = helper(left.left, right.right)
                inPair = helper(left.right, right.left)

                return outPair and inPair
            else:
                return False

        if not root:
            return True
        else:
            return helper(root.left, root.right)
def main():
    sol = Solution()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)


    print(sol.isSymmetric(root))

if __name__ == "__main__":
    main()
