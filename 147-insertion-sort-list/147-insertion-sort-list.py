# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
        
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prePointer = ListNode(-5001);
        while head:
            p = prePointer;
            while p:
                if  head.val >= p.val and (p.next == None or head.val <= p.next.val) :
                    nex = head.next;
                    head.next = p.next;
                    p.next = head;
                    head = nex;
                    break;
                
                p = p.next;
            
        
        return prePointer.next;