from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        # Base case
        if root is None:
            return 0

        queue = deque([(root, 1)]) # (node, depth) we will add to depth if not a leaf node
        
        # while queue has elements in it
        while queue:
            node, depth = queue.popleft() # gives node we are looking at

            # returns when it hits the first leaf
            if node.left is None and node.right is None:
                return depth

            # traverses through tree if no leaf
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))