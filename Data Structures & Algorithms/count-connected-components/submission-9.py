class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # disjoint set
        # time complexiyt if we use union by rank and path compression it is nearly o(E)
        # return the number of roots -> the nubmer of commected components

        ranks = [0 for _ in range(n)]
        roots = [i for i in range(n)]

        def find_root(a):
            if a != roots[a]:
                roots[a] = find_root(roots[a])
            
            return roots[a]

        def union(a, b):
            root_a = find_root(a)
            root_b = find_root(b)

            if ranks[root_a] == ranks[root_b]:
                roots[root_a] = root_b
                ranks[root_b] += 1

            elif ranks[root_a] > ranks[root_b]:
                roots[root_b] = root_a

            else:
                roots[root_a] = root_b

        for a, b in edges:
            union(a, b)

        unique_roots = set(find_root(i) for i in range(n))

        return len(unique_roots)
        