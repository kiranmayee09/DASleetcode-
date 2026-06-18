# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        """ if head is None or head.next is None:
            return head

        new_head = self.reverselist(head.next)

        head.next.next = head
        head.next = None

        return new_head """

        """ stack = []
        temp = head
        while temp:
            stack.append(temp.val)
            temp = temp.next
        
        temp = head
        while temp:
            temp.val = stack.pop()
            temp = temp.next
        return head """
        curr = head
        prev = None
        next = None

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev