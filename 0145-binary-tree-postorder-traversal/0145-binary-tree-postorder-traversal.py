# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        self.postorder_list = []
        return self.traversal(root, self.postorder_list)

    def traversal(self, node, _list):
        if node is None:
            return _list
        # if node.left: (don't need to check if node.left or node.right exists with base case now)
        self.traversal(node.left, _list)
        # if node.right:
        self.traversal(node.right, _list)
        # if node.left is None and node.right is None:
        _list.append(node.val)
        return _list