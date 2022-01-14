# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tot = 0
        current = head
        ar = []
        while current is not None:
            ar.append(current)
            current = current.next
            tot += 1
            
        return ar[tot//2]