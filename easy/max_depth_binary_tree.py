# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxDepth(self, root):
        return self.child(root)

    def child(self, tree):
        if tree is None:
            return 0
        if tree.left is None and tree.right is None:
            return 1

        return 1 + max(self.child(tree.left), self.child(tree.right))


b1 = TreeNode(9)
b2 = TreeNode(20)
root = TreeNode(3,b1,b2)
b2.left = TreeNode(15)
b2.right = TreeNode(7)

answer = Solution()
print(answer.maxDepth(root))
