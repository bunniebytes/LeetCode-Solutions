# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        curr = head
        prev = head
        temp = None

        while curr is not None:
            if temp is None:
                if curr.val == val:
                    curr = curr.next
                    prev = prev.next
                else:
                    curr = curr.next
                    temp = prev
            elif curr.val == val:
                while curr and curr.val == val:
                    curr = curr.next
                prev.next = curr
                prev = prev.next
                if curr:
                    curr = curr.next
            else:
                prev = prev.next
                curr = curr.next
        return temp