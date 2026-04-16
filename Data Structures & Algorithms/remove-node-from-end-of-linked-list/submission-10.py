# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
         # is the list empty
        # is the n invalid that is n > len(list)
        # 1 2 3 4
        # slow      fast
        # 1    2   3        4

        dummy = ListNode(next=head)
        slow = dummy
        fast = dummy

        for i in range(n):
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next # cut the nth node

        return dummy.next