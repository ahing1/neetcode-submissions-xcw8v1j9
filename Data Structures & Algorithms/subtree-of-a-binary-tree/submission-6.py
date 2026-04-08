# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSameTree(p, q):
            if not p and not q:
                return True
            if p and q and p.val == q.val:
                left = isSameTree(p.left, q.left)
                right = isSameTree(p.right, q.right)
                return left and right
            else:
                return False
        
        if not root:
            return False
        
        if root and subRoot and root.val == subRoot.val:
            if isSameTree(root, subRoot):
                return True
            else:
                left = self.isSubtree(root.left, subRoot)
                right = self.isSubtree(root.right, subRoot)
                return left or right
        else:
            left = self.isSubtree(root.left, subRoot)
            right = self.isSubtree(root.right, subRoot)
            return left or right