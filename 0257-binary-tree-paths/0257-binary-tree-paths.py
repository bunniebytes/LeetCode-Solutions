# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
       self.output = []
       temp_path = ""

       self.find_path(root, temp_path)
       return self.output
    
    def find_path(self, root, path):
        if root.left is None and root.right is None:
            path += str(root.val)
            self.output.append(path)
        else:
            path += f"{root.val}->"
            if root.left:
                self.find_path(root.left, path)
            if root.right:
                self.find_path(root.right, path)
