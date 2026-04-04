class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # disjoint set and use union by rank and path compression
        # the time complexity is nearyly o(E)
        n = len(edges)
        parent = [i for i in range(n + 1)]
        rank = [0 for i in range(n + 1)]
        # need to aware node 0 not exist

        def find(a):
            if a != parent[a]:
                parent[a] = find(parent[a])
            return parent[a]

        def union(a, b):
            root_a = find(a)
            root_b = find(b)

            if root_a == root_b:
                return False
            
            if rank[root_a] == rank[root_b]:
                parent[root_a] = parent[root_b]
                rank[root_b] += 1
            
            elif rank[root_a] < rank[root_b]:
                parent[root_a] = parent[root_b]
            
            else:
                parent[root_b] = parent[root_a]

            return True

        for a, b in edges:
            if not union(a, b):
                return [a, b]

        return [-1, -1]
        