# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import random

class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.size = 0
        current = head
        while current:
            self.size += 1
            current = current.next

    def getRandom(self) -> int:
        random_pos = random.randint(1, self.size)
        current = self.head
        for _ in range(random_pos-1):
            current = current.next
        current.next
        return current.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()