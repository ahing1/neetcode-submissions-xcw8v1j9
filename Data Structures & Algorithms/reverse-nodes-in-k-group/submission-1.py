# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # check for k nodes
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next
        if count < k:
            return head

        # reverse
        cur = head
        prev = None
        for i in range(k):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        # connect reversed groups
        head.next = self.reverseKGroup(nxt, k)
        return prev