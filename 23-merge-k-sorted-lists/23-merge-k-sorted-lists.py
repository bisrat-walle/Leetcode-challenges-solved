# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        for i in lists:
            current = i
            while current is not None:
                arr.append(current.val)
                current = current.next
        arr.sort()
        
        head = None
        if len(arr) > 0:
            head = ListNode(arr[0])
        
        current = head
        
        for i in arr[1:]:
            node = ListNode(i)
            current.next = node
            current = current.next
        return head