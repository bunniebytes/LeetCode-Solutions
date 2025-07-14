# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        sum_value = 0

        while head:
            sum_value *= 2
            sum_value += head.val
            head = head.next
        return sum_value
