# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        intersectNode = None
        listA = headA
        listB = headB
        cycleA = False
        cycleB = False

        while True:
            if listA is None and not cycleA:
                listA = headB
                cycleA = True
            if listB is None and not cycleB:
                listB = headA
                cycleB = True
            if listA == listB and cycleA and cycleB:
                return listA
            elif cycleA and cycleB and (listA is None or listB is None):
                return None
            listA = listA.next
            listB = listB.next