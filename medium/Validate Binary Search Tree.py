# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        output = []
        self.inOrderTraversal(root, output)

        for i in range(len(output) - 1):
            if output[i] >= output[i + 1]:
                return False

        return True

    def inOrderTraversal(self, root, output):
        if root is None:
            return

        self.inOrderTraversal(root.left, output)
        output.append(root.val)
        self.inOrderTraversal(root.right, output)

def main():
    node1 = TreeNode(1)
    node3 = TreeNode(3)
    node6 = TreeNode(6)
    node4 = TreeNode(4, node3, node6)
    #
    root = TreeNode(5, node1, node4)

    # node1 = TreeNode(1)
    # root = TreeNode(1, None, node1)


    sol = Solution()
    print(sol.isValidBST(root))
    # print(type(root))

if __name__ == "__main__":
    main()
