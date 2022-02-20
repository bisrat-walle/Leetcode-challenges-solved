# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import copy

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        head2 = copy.deepcopy(head)
        
        rev = None
        current = head2
        while current:
            nex = current.next
            current.next = rev
            rev = current
            current = nex
        
        size = 0
        current = head
        while current:
            current = current.next
            size += 1
        
        
        slow1 = head
        slow2 = rev
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow1_next = slow1.next
            slow2_next = slow2.next
            slow1.next = slow2
            slow2.next = slow1_next
            slow1 = slow1_next
            slow2 = slow2_next
        
        current = head
        for i in range(size-1):
            current = current.next
        current.next = None
        
        
        return head
            
            
            
            
            
        