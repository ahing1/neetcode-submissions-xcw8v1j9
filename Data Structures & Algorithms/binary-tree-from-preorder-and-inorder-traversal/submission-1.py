# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        # both arrays always represent the same set of nodes. If preorder is empty, inorder must also be empty 
        # they can never get out of sync since you're always slicing them based on the same root index
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])

        mid = 0
        for i, n in enumerate(inorder):
            if n == root.val:
                mid = i
                break

        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root