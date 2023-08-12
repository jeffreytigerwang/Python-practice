# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # res = []
        #
        # def inOrderTraversal(root):
        #     if root:
        #         inOrderTraversal(root.left)
        #         res.append(root.val)
        #         inOrderTraversal(root.right)
        #
        # inOrderTraversal(root)
        #
        # for i in range(1, len(res)):
        #     if res[i - 1] >= res[i]:
        #         return False
        #
        # return True

        def isValid(root, left, right):
            if not root:
                return True

            if not (right > root.val > left):
                return False

            return isValid(root.left, left, root.val) and isValid(root.right, root.left, right)

        return isValid(root, float("-inf"), float("inf"))


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
