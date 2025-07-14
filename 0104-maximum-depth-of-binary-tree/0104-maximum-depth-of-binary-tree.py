# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depth = 0
        return self.countDepth(root, depth)

    def countDepth(self, root, count):
        if root is None:
            return count
        count += 1
        return max(self.countDepth(root.left, count), self.countDepth(root.right, count))