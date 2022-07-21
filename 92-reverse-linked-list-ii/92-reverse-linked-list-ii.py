# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        counter = 1
        current = head
        prev = None
        new_head = head if left != 1 else None
        while counter < left:
            prev = current
            current = current.next
            counter += 1
        # print(current, prev, sep=" ***** ")
        initial_list_end = prev
        prev = None
        end = current
        while counter <= right:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
            counter += 1
        
        if not new_head: new_head = prev
            
        if not initial_list_end: 
            initial_list_end = prev
        else:
            initial_list_end.next = prev
        if end: end.next = current
        
        return new_head