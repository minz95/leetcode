# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        curr = head
        prev = head
        nhead = head
        while curr != None:
            if curr.next == None:
                curr = curr.next
                continue
            n = curr.next
            if prev != curr:
                prev.next = n
            else:
                nhead = n
            curr.next = n.next
            n.next = curr
            prev = curr
            curr = curr.next
        return nhead
        