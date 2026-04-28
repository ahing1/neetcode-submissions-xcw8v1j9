# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def sameTree(root, subRoot):

            if not root and not subRoot:
                return True
            
            if root and subRoot and root.val == subRoot.val:
                left = sameTree(root.left, subRoot.left)
                right = sameTree(root.right, subRoot.right)
                return left and right
            else:
                return False

        
        if not subRoot:
            return True
        if not root:
            return False
        
        if sameTree(root, subRoot):
            return True
        else:
            left = self.isSubtree(root.left, subRoot)
            right = self.isSubtree(root.right, subRoot)
            return left or right