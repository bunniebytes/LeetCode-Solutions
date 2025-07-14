# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # if root.left and root.right is None:
        #     return True
        # if root.left is None or root.right is None:
        #     return False
        return self.checkNodes(root.left, root.right)

    def checkNodes(self, p, q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        return p.val == q.val and self.checkNodes(p.left, q.right) and self.checkNodes(p.right, q.left)
