# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        arr = []
        temp = head
        while temp:
            if temp.val < x:
                arr.append(temp.val)
            temp = temp.next

        temp = head
        while temp:
            if temp.val >= x:
                arr.append(temp.val)
            temp = temp.next
        
        """ temp = head
        i = 0
        while temp:
            temp.val = arr[i]
            i += 1
            temp = temp.next
        return head """

        dummy = ListNode(0)
        curr = dummy
        for num in arr:
            curr.next = ListNode(num)
            curr = curr.next
        return dummy.next