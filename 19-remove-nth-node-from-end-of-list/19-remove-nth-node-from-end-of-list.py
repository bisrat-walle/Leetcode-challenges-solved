# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ln = 0
        current = head
        while current:
            ln += 1
            current = current.next
        current = head
        for _ in range(ln-n-1):
            current = current.next
        if ln == 1:
            return None
        if ln == n:
            return head.next
        if current.next:
            temp = current.next.next
            current.next.next = None
            current.next = temp
        
        return head
        