"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None
        
        cur = head
        while cur:
            copy = Node(cur.val)
            copy.next = cur.next
            cur.next = copy
            cur = cur.next.next
        
        orig = head
        while orig:
            copy = orig.next
            if orig.random:
                copy.random = orig.random.next
            orig = orig.next.next
        
        old = head
        new = head.next
        res = new

        while old:
            old.next = old.next.next
            new.next = new.next.next if new.next else None
            old = old.next
            new = new.next
        
        return res



