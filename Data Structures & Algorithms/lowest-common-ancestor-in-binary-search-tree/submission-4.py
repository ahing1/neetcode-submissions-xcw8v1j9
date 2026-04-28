# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        if not root or not p or not q:
            return None

        if max(p.val, q.val) < root.val: #both are less than root so have to be in left subtree
            return self.lowestCommonAncestor(root.left, p, q)
        elif min(p.val, q.val) > root.val: #both are greater than root so have to be in right subtree
            return self.lowestCommonAncestor(root.right, p, q)
        else: #both are in opposite subtree so have to be root
            return root
