"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #hash map 
        # time o(n)
        #space o(n)
        if not head:
            return None

        new_nodes = {}
        node = head

        while node:
            new_nodes[node] = Node(x=node.val)
            node = node.next

        node = head

        while node:
            if node.next:
                new_nodes[node].next = new_nodes[node.next]
            if node.random:
                new_nodes[node].random = new_nodes[node.random]
            node = node.next
        
        return new_nodes[head]


        