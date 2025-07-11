# Definition for a binary tree node.
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def function(node):
            if not node:
                return
            
            function(node.left)
            function(node.right)
            res.append(node.val)
            

        function(root)
        return res
        