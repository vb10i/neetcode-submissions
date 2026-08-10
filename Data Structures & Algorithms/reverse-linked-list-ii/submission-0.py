# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        dist = right-left+1
        curr = head
        l,r = left, right
        while l!=1:
            curr = curr.next
            l -= 1

        last = head
        while r!=1:
            last = last.next
            r -= 1
        
        futhead = head
        futlast = curr
        after = last.next
        prev = after

        while dist!=0:
            currnext = curr.next
            curr.next = prev
            prev = curr
            curr = currnext
            dist -= 1
        futlast.next = curr
        
        if left == 1:
            head = prev
        else:
            for i in range(left-2):
                futhead = futhead.next
            futhead.next = prev
        return head 

        