# Definition for a binary tree node.

from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if self.isSametree(root , subRoot):
            return True
        return self.isSubtree(root.left , subRoot) or self.isSubtree(root.right , subRoot)
    def isSametree(self, X: Optional[TreeNode], Y: Optional[TreeNode]) -> bool:
        if not X and not Y:
            return True
        if not X or not Y:
            return False
        if X.val != Y.val:
            return False
        return self.isSametree(X.left , Y.left) and self.isSametree(X.right , Y.right)


        