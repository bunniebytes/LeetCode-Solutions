# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.height = 0
        if root is None:
            return True
        if root.left and root.right:
            depth = self.find_height(self.height, root.left) - self.find_height(self.height, root.right)
        elif root.left and root.right is None:
            depth = self.find_height(self.height, root.left)
        else:
            depth = self.find_height(self.height, root.right)
        return abs(depth) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)
        
        
    def find_height(self, c :int, root):
        if root is None:
            return c
        return max(self.find_height(c + 1, root.left), self.find_height(c + 1, root.right))