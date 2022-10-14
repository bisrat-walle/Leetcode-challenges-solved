# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        # print(slow, prev)
        if not slow.next:
            if not prev:
                return None
            else:
                prev.next = None
        else:
            slow.val = slow.next.val
            slow.next = slow.next.next
        return head
        