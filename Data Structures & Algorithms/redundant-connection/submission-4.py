class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # disjoint set and use union by rank and path compression
        # the time complexity is nearyly o(E)
        n = len(edges)
        roots = [i for i in range(n + 1)]
        rank = [0 for i in range(n + 1)]
        # need to aware node 0 not exist

        def find_root(a):
            if a != roots[a]:
                roots[a] = find_root(roots[a])

            return roots[a]

        def union(a, b):
            root_a = find_root(a)
            root_b = find_root(b)

            if root_a == root_b:
                return False
            
            if rank[root_a] == rank[root_b]:
                roots[root_a] = roots[root_b]
                rank[root_b] += 1
            
            elif rank[root_a] < rank[root_b]:
                roots[root_a] = roots[root_b]
            
            else:
                roots[root_b] = roots[root_a]
                
            return True

        for a, b in edges:
            if not union(a, b):
                return [a, b]

        return [-1, -1]
        