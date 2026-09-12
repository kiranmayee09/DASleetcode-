# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import math 

class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current = head

        while current.next:

            a = current.val
            b = current.next.val

            g = math.gcd(a, b)

            new_node = ListNode(g)

            new_node.next = current.next
            current.next = new_node

            current = new_node.next
        
        return head