# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = []

        def rec(node: TreeNode, tempMax: int):
            if node.left is None and node.right is None:
                if node.val >= tempMax:
                    count.append(node.val)
                    return

            if node.val >= tempMax:
                count.append(node.val)

            if node.left is not None:
                rec(node.left, max(node.val, tempMax))

            if node.right is not None:
                rec(node.right, max(node.val, tempMax))

        rec(root, root.val)
        res = len(count)
        return res


def main():
    node1 = TreeNode(5)
    node2 = TreeNode(1)
    node3 = TreeNode(3)
    node4 = TreeNode(4, node2, node1)
    node5 = TreeNode(1, node3)
    root = TreeNode(3, node5, node4)

    solution = Solution()
    print(solution.goodNodes(root))


if __name__ == '__main__':
    main()