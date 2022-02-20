# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        l = []
        current = head
        while current:
            l.append(current.val)
            current = current.next
        l.sort()
        sorted_head = ListNode(l[0])
        current = sorted_head
        for i in l[1:]:
            new_node = ListNode(i)
            current.next = new_node
            current = current.next
        
        return sorted_head