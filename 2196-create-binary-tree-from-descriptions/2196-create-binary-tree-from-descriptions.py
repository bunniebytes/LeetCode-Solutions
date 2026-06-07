# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        node_dict = {}
        head_set = set()
        child_set = set()
        # creating nodes and store it in dictionary with value of the node as key
        # keep track of curr head so we know what to return (but how does this update?)
        # loop through descriptions
        for description in descriptions:
        #     separate out the node description into val, child, isleft
            node_val, child_val, isleft = description
            child_set.add(child_val)
            if node_dict.get(node_val):
                node = node_dict[node_val]
            else:
                node = TreeNode()
                node.val = node_val
                # curr_head = node
                head_set.add(node_val)
            if node_dict.get(child_val):
                child = node_dict[child_val]
            else:
                child = TreeNode()
                child.val = child_val
                node_dict[child_val] = child
            if isleft == 1:
                node.left = child
            else:
                node.right = child
            node_dict[node_val] = node
        head_val, = head_set.difference(child_set)

        return node_dict[head_val]