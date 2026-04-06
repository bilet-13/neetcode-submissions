# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # tiem complexity o(n + m)
        dummy = ListNode()

        node = dummy
        n1 = list1
        n2 = list2

        while n1 and n2:
            if n1.val < n2.val:
                node.next = n1
                n1 = n1.next

            else:
                node.next = n2
                n2 = n2.next
            
            node = node.next
        
        if n1:
            node.next = n1
        elif n2:
            node.next = n2
        
        return dummy.next


        