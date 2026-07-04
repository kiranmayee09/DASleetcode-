# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """ if not head:
            return head

        arr = []
        temp = head
        while temp:
            arr.append(temp.val)
            temp = temp.next

        for i in range(0, len(arr) - 1, 2):
            arr[i], arr[i+1] = arr[i+1], arr[i]

        temp = head
        i = 0
        while temp:
            temp.val = arr[i]
            i += 1
            temp = temp.next

        return head """

        if not head or not head.next:
            return head

        frist = head
        secound = head.next

        frist.next = self.swapPairs(secound.next)
        secound.next = frist

        return secound