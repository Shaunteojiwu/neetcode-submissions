# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            nxt = curr.next     # Store the next node so we don't lose it
            curr.next = prev    # Reverse the pointer to face backward
            
            # Shift both pointers forward for the next iteration
            prev = curr
            curr = nxt
            
        # At the end, 'curr' is None and 'prev' is the new head
        return prev
        