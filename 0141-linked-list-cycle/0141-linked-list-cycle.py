# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visiter = set()
        temp = head
        while temp:
            if temp in visiter:
                return True
            
            visiter.add(temp)
            temp = temp.next
        return False