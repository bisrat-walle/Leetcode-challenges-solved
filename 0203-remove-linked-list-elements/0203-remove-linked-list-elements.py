# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        new_head = ListNode()
        current = head
        current2 = new_head
        while current:
            temp = current.next
            current.next = None
            if current.val != val:
                current2.next = current
                current2 = current2.next
            current = temp
            
        return new_head.next