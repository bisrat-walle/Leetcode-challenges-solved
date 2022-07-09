# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before = ListNode() 
        after = ListNode()
        current1, current2 = before, after
        current = head
        while current:
            temp = current.next
            current.next = None
            if current.val < x:
                current1.next = current
                current1 = current1.next
            else:
                current2.next = current
                current2 = current2.next
            current = temp
        
        current1.next = after.next
        return before.next