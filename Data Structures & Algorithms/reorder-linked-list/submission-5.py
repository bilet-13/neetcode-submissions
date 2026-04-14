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
        right = prev
        left = head
        dummy = ListNode()
        node = dummy

        while left and right:
            node.next = left
            left = left.next

            node = node.next

            node.next = right
            right = right.next
    
            node = node.next

        node.next = left if left else right

        #time complexity o(n)
