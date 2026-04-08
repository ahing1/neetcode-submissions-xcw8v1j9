# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if head is None or head.next is None:
            return
        
        slow, fast = head, head.next #use slow and fast to get the middle of the linked list where slow is the middle

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next #start of second list
        slow.next = None #seperate the two lists

        # reverse second half
        cur = second
        prev = None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        l1 = head
        l2 = prev

        while l1 and l2:
            n1 = l1.next
            n2 = l2.next
            
            l1.next = l2
            l2.next = n1
            
            l1 = n1
            l2 = n2

