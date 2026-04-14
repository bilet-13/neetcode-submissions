# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # is the head == None
        # reverse the right half of the list

        # how to split right half
        #1 identify the right half -> slow, fast pointer
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None
        node = slow.next
        slow.next = None # split left and right half

        # 2 reverse the right half start by the midlle pointer
        while node:
            nxt = node.next
            node.next = prev
            prev = node
            node = nxt

        # merge the left half list and reversed list one by one

        left = head
        right = prev

        while left and right:
            nxt_left = left.next
            next_right = right.next

            left.next = right
            right.next = nxt_left

            left = nxt_left
            right = next_right
