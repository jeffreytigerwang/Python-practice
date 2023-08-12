# https://leetcode.com/problems/count-good-nodes-in-binary-tree/submissions/924977077/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def dfs(root, currMax):
            nonlocal count

            if not root:
                return

            if root.val >= currMax:
                # res.append(root.val)
                count += 1

            temp = max(currMax, root.val)

            dfs(root.left, temp)
            dfs(root.right, temp)

        dfs(root, root.val)

        return count


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