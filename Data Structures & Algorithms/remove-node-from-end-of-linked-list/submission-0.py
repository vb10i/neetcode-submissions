# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr != None:
            curr = curr.next
            length += 1
        newn = length-n
        temp = head
        if newn == 0:
            head = head.next
            return head 
        while newn!=1:
            temp = temp.next
            newn -= 1
        temp.next = temp.next.next
        return head 