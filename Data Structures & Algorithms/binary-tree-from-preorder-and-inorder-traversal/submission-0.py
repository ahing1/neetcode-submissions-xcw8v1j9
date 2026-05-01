# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])

        inMid = 0
        for i, n in enumerate(inorder):
            if n == root.val:
                inMid = i
                break

        root.left = self.buildTree(preorder[1:inMid+1], inorder[:inMid])
        root.right = self.buildTree(preorder[inMid+1:], inorder[inMid+1:])

        return root