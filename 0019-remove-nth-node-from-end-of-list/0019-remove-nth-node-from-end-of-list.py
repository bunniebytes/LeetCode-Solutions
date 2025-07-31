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
        # loop through range of n so p2 is now at 2nd node (e.g n = 2)
        for x in range(n):
            p2 = p2.next
        # check if p2 is not valid:
        if p2 is None:
            return head.next
        # while p2.next is valid:
        while p2.next:
            # move p1 and p2 to next node
            p1, p2 = p1.next, p2.next
        # if p2 is no longer valid:
        # we know current p1 node is 3 (in first example) and we want the next node
        #to skip 4 (since that is the 2nd node from the end) and be node 5
        p1.next = p1.next.next
        return head