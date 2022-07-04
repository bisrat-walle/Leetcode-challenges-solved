# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head:
            return
        
        n = 0
        current = head
        while current.next:
            current = current.next
            n += 1
        n += 1
        current.next = head
        rotation_length = k % n
        
        current = head
        new_head = None
        counter = 0
        # print(f"*** {n-rotation_length} ***")
        while counter < n-rotation_length-1:
            current = current.next
            counter += 1
        
        new_head = current.next
        current.next = None
        return new_head
        