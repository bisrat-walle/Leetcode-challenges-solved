# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        li = []
        for l in lists:
            current = l
            while current is not None:
                li.append(current.val)
                current = current.next
        li.sort()
        an = None
        if li != []:
            an = ListNode(li[0])
        current = an
        for i in li[1:]:
            new_node = ListNode(i)
            current.next = new_node
            current = current.next
        return an
            
        