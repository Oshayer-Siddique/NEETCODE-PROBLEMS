from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def function(node):
            if not node:
                return 0
            leftnode = function(node.left)
            rightnode = function(node.right)

            return max(leftnode,rightnode) + 1
        return function(root)
        