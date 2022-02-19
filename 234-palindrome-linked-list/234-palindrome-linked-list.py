# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        half_rev, fast, slow = None, head, head
        while fast and fast.next:
            fast = fast.next.next
            slow_next = slow.next
            slow.next = half_rev
            half_rev = slow
            slow = slow_next
        if fast:
            slow = slow.next
        is_palindrome = True
        while half_rev:
            if half_rev.val != slow.val:
                is_palindrome = False
                break
            half_rev = half_rev.next
            slow = slow.next
        return is_palindrome
        