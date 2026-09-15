# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        cur = head
        end = head
        if not head.next:
            return
        while cur:
            end = cur
            while end.next:
                prev = end
                end = end.next
            prev.next = None
            temp = cur.next    
            cur.next = end
            end.next = temp
            cur = cur.next
            if not cur:
                break
            cur = cur.next