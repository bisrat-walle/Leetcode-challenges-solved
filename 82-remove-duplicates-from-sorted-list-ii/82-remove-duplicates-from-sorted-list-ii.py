# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        duplicates = set()
        current = head
        while current:
            if current.next and current.val == current.next.val:
                duplicates.add(current.val)
            current = current.next
        
        current = head
        unique = ListNode()
        current1 = unique
        while current:
            if current.val not in duplicates:
                current1.next = ListNode(current.val)
                current1 = current1.next
            current = current.next
        
        return unique.next