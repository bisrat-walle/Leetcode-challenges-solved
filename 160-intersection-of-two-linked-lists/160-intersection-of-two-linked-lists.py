# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        lenA, lenB = 0, 0
        current = headA
        while current:
            lenA += 1
            current = current.next
        
        current = headB
        while current:
            lenB += 1
            current = current.next
            
        if lenA > lenB:
            current1, current2 = headA, headB
        else:
            current1, current2 = headB, headA
        
        for i in range(abs(lenA-lenB)):
            current1 = current1.next
        
        while current1 and current2:
            if current1 == current2:
                return current1
            current1 = current1.next
            current2 = current2.next
        return None
        
        