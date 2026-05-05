# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        res = 0
        minVal = float('-inf')

        def dfs(root, minVal):
            nonlocal res
            if not root:
                return
            
            if root.val >= minVal:
                minVal = root.val
                res += 1
            
            dfs(root.left, minVal)
            dfs(root.right, minVal)
        
        dfs(root, minVal)
        return res
            
