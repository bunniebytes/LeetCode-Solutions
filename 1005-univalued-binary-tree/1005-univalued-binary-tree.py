# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        self.root_val = root.val
        return self.nodeValuesEqual(root)
        
    def nodeValuesEqual(self, node):
        if node is None:
            return True
        # print(node.val == self.root_val)
        # if node.val == self.root_val:
        #     self.nodeValuesEqual(node.left)
        #     self.nodeValuesEqual(node.right)
        # else:
        #     return False
        return node.val == self.root_val and self.nodeValuesEqual(node.left) and self.nodeValuesEqual(node.right)