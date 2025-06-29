# Definition for a binary tree node.
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        def function(node):
            if not node:
                return 0
            left_depth = function(node.left)
            right_depth = function(node.right)
            self.max_diameter = max(self.max_diameter, (left_depth + right_depth))
            return max(left_depth , right_depth) + 1
        function(root)
        return self.max_diameter

            
    