# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # assign 2 pointers where p2 is moved to the nth node
        p1 = head
        p2 = head
        # (e.g n = 2 move to next node twice):
        for x in range(n):
            p2 = p2.next
        if n is 1 and p2 is None: # (This is after assigning p2 to nth node)
            return p2
        # need to check if p2 is valid - if not that means that n = length of linked list and we need to remove the 1st element aka return head.next
        if p2 is None:
            return head.next
        # once p2 is in place loop through while p2.next is valid
        while p2.next:
            # if valid move p1 and p2 to next
            p1 = p1.next
            p2 = p2.next
        # if p2.next is no longer valid p1.next should be the nth node from the end
        # assign p1.next to p1.next.next (This will remove the nth node which is p1.next)
        p1.next = p1.next.next
        # return the head of linked list
        return head