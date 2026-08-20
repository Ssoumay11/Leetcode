# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def solve(self, list1, list2):

        # Base case
        if list1 is None:
            return list2

        if list2 is None:
            return list1

        # Choose list1 node
        if list1.val <= list2.val:
            list1.next = self.solve(list1.next, list2)
            return list1

        # Choose list2 node
        else:
            list2.next = self.solve(list1, list2.next)
            return list2

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        return self.solve(list1, list2)
        