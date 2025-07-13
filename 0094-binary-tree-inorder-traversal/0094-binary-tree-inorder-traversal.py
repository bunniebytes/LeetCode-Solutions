# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.inorder_val = []

        if root is None:
            return []

        self.tree_traversal(root)

        return self.inorder_val

    def tree_traversal(self, root):
        if root.left:
            self.tree_traversal(root.left)
        self.inorder_val.append(root.val)
        if root.right:
            self.tree_traversal(root.right)
        else:
            return

