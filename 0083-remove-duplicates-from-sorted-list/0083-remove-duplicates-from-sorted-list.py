# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head

        prev = head
        unique_list = prev
        curr = head.next
        while curr is not None:
            if prev.val == curr.val:
                curr = curr.next
            else:
                prev.next = curr
                prev = prev.next
                curr = curr.next
            if curr is None:
                prev.next = curr

        return unique_list