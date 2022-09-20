# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        if not head:
            return [None] * k
        ln = 0
        current = head
        while current:
            current = current.next
            ln += 1
        if ln > k:
            width = ln // k
            remaining = ln%k
        else:
            width = 1
            remaining = 0
        current = head
        ans = []
        for _ in range(k):
            ans.append(current)
            for i in range(width+int(bool(remaining))):
                if not current:
                    break
                if i == (width+int(bool(remaining)))-1:
                    temp = current.next
                    current.next = None
                else:
                    current = current.next
            current = temp
            if remaining:
                remaining -= 1
        return ans