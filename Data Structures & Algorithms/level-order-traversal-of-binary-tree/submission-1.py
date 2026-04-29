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
        if not root:
            return []
        q.append(root)

        while q:
            qLen = len(q) #tells us how many nodes are at this level
            level = [] #sublist for level

            for i in range(qLen): #loop for nodes in the level
                node = q.popleft() #pop to get node
                if node: #make sure it exists
                    level.append(node.val) #add to sublist
                    #append children
                    if node.left:
                        q.append(node.left) 
                    if node.right:
                        q.append(node.right)

            res.append(level)
        
        return res