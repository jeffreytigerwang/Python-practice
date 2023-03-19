# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return

        if len(nums) == 1:
            return TreeNode(nums[0])

        mid = len(nums) // 2

        root = TreeNode(nums[mid])

        root.left = self.sortedArrayToBST(nums[0: mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])

        return root
