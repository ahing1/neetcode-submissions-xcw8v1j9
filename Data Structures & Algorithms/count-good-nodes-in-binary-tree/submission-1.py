# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # keep track of max seen so far
        res = 0
        q = deque()
        q.append((root, float('-inf')))

        while q:
            node, maxVal = q.popleft()
            if node.val >= maxVal:
                res += 1
                maxVal = node.val
            
            if node.left:
                q.append((node.left, maxVal))
            
            if node.right:
                q.append((node.right, maxVal))
        
        return res