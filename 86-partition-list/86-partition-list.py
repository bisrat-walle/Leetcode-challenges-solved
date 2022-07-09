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
            if current.val < x:
                current1.next = ListNode(current.val)
                current1 = current1.next
            else:
                current2.next = ListNode(current.val)
                current2 = current2.next
            current = current.next
        
        current1.next = after.next
        return before.next