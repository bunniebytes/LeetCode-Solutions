# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        val_list = []
        while head is not None:
            val_list.append(head.val)
            head = head.next
        
        reverse_list = val_list[::-1]

        if reverse_list == val_list:
            return True
        else:
            return False