# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node to handle edge cases easily
        dummy = ListNode()
        tail = dummy
        
        # Iterate while both lists have nodes
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            
            # Move the tail pointer forward
            tail = tail.next
            
        # Attach any remaining nodes from either list
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
            
        # The merged list starts at dummy.next
        return dummy.next