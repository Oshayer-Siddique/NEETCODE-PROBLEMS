print("Invert Binary Tree")


from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        res = []
        def function(node):
            if not node:
                return
            leftinvert = self.invertTree(node.left)
            rightinvert = self.invertTree(node.right)

            node.left = rightinvert
            node.right  = leftinvert

            return node
        return function(root)
    
        
        