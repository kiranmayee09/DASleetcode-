# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None

        count = 0
        temp = head

        while temp:
            count += 1
            temp = temp.next

        middle = count // 2

        """ temp = head
        for i in range(middle -1):
            temp = temp.next
        temp.next = temp.next.next
        return head """

        dummy = ListNode(0)
        dummy.next = head
        temp = dummy

        for _ in range(middle):
            temp = temp.next
        temp.next = temp.next.next
        return dummy.next