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
        
        # inorder :mid = left mid+1: = right
        # preorder index in inorder is number of nodes in left
        # 1:mid+1 = left mid+1: = right

        mid = 0
        for i, n in enumerate(inorder):
            if n == root.val:
                mid = i
                break

        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root
