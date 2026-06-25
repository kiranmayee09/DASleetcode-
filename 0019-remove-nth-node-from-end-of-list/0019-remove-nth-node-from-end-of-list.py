# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """ temp = head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        if count == n:
            return head.next
        pos = count - n
        temp = head
        for i in range(pos-1):
            temp = temp.next
        temp.next = temp.next.next
        return head """

        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy
        for i in range(n):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next