# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def merge_two_lists(l1, l2):

            dummy = ListNode()
            tail = dummy

            while l1 and l2:
                if l1.val < l2.val:
                    tail.next = l1
                    l1 = l1.next
                else:
                    tail.next = l2
                    l2 = l2.next
                tail = tail.next
            
            if l1:
                tail.next = l1
            else:
                tail.next = l2
            
            return dummy.next
        
        def divide_and_conquer(lists):

            if len(lists) == 0:
                return None
            elif len(lists) == 1:
                return lists[0]

            mid = len(lists) // 2

            left = divide_and_conquer(lists[:mid])
            right = divide_and_conquer(lists[mid:])

            merged = merge_two_lists(left, right)
            return merged
        

        res = divide_and_conquer(lists)
        return res

