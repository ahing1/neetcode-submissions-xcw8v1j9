# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []
        # preorder traversal
        def dfs(node):
            if not node:
                res.append("N")
                return
            
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right) 

            return
        
        dfs(root)
        return ",".join(res)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        values = data.split(",")
        q = deque(values)

        def dfs():
            val = q.popleft()
            if val == "N":
                return None
            else:
                node = TreeNode(int(val))
                node.left = dfs()
                node.right = dfs()
                return node

        return dfs()

            