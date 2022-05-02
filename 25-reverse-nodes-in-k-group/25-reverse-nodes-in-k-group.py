# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(start, end):
            r = None        
            curr = start        
            while curr!=end:
                prev=curr
                curr = curr.next
                prev.next = r             
                r = prev
            start.next = end
            return r
    
    
        new_head_pointer=ListNode(None, head) 
        prev=new_head_pointer
        curr = head        
        while curr:
            start = curr
            i = k
            while curr and i != 0: 
                curr=curr.next
                i -= 1
			
            if i == 0: # reverse only if it has size k                         
                prev.next = reverse(start, curr)
                prev = start                          
            
        return new_head_pointer.next