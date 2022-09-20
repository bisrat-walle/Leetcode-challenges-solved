# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = ListNode()
        even = ListNode()
        index = 0
        current = head
        current_even = even
        current_odd = odd
        while current:
            temp = current.next
            current.next = None
            if index%2 == 0:
                current_even.next = current
                current_even = current
            else:
                current_odd.next = current
                current_odd = current
            index += 1
            current = temp
        current_even.next = odd.next
        return even.next