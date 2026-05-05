# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        curr = head
        if head is None:
            return head
        _next = curr.next
        len_list = 1
        tail = None

        while _next is not None:
            _next = _next.next
            len_list += 1
        if k > len_list:
            k = k % len_list
        num_nodes = len_list - k
        if num_nodes == 0:
            return head
        _next = curr.next
        
        while _next is not None:
            num_nodes -= 1 # this might need to be moved?
            if num_nodes == 0 and tail is None:
                tail = head
                head = _next
                curr.next = None
            curr = _next
            _next = curr.next
            if _next is None:
                curr.next = tail

        return head