# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        res = []
        q = deque()
        q.append(root)

        while q:
            qLen = len(q) #tells us how many nodes are at this level
            level = [] #sublist for level

            for i in range(qLen): #loop for nodes in the level
                node = q.popleft() #pop to get node
                if node: #make sure it exists
                    level.append(node.val) #add to sublist
                    q.append(node.left) #append children
                    q.append(node.right)

            if level: #make sure level is not empty since q could have null nodes
                res.append(level)
        
        return res