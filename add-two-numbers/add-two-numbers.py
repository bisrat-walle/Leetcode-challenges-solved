# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ""
        num2 = ""
        current = l1
        while current is not None:
            num1 += str(current.val)
            current = current.next
        
        current = l2
        while current is not None:
            num2 += str(current.val)
            current = current.next
        
        num = str(int("".join(reversed(num1))) + int("".join(reversed(num2))))
        
        l = ListNode()
        l.val = int(num[-1])
        current = l
        for i in reversed(num[:-1]):
        # for i in reversed(num):
            # current.val = int(i)
            # new_node = ListNode()
            # current.next = new_node
            # if current.next is not None:
            #     current = new_node
            new_node = ListNode(int(i))
            current.next = new_node
            current = current.next
        return l
            
        