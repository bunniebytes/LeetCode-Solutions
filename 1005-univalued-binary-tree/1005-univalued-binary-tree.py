# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        self.root_val = root.val
        self.return_val = True
        return self.nodeValuesEqual(root) and self.return_val
        
    def nodeValuesEqual(self, node):
        if node is None:
            return True
        if node.val == self.root_val:
            self.nodeValuesEqual(node.left)
            self.nodeValuesEqual(node.right)
        else:
            self.return_val = False
        return True