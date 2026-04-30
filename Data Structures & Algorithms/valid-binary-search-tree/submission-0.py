# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root, lowerBound, upperBound):
            if not root:
                return True
            
            if not (lowerBound < root.val < upperBound): # if not in bounds
                return False
            
            # when going left we want the upper bound to shrink bc nodes value must be less than parent
            # when going right we want the lower bound to shrink bc nodes value must be greater than parent
            # as we move down the tree we tighten the bounds
            return dfs(root.left, lowerBound, root.val) and dfs(root.right, root.val, upperBound)

        # root has no contraints
        return dfs(root, float('-inf'), float('inf'))