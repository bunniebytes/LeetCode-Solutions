# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        output = []
        if root is None:
            return root
        self.tree_reverse(root)
        return root

    def tree_reverse(self, root):
        root.left, root.right = root.right, root.left
        if root.left:
            self.tree_reverse(root.left)
        if root.right:
            self.tree_reverse(root.right)
        return