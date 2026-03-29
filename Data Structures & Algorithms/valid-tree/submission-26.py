class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # tree: connected and no-cycle graph
        
        # user globel var visited_node 
        # undirected edge
        # disjoint set 
        # if find_root(a) == find_root(b) cycle return false
        # if in the end there is only one root return True
        # else return False
        root = [i for i in range(n)]

        def find_root(a):
            if root[a] != a:
                root[a] = find_root(root[a])
            return root[a]

        def join(a, b):
            r_a = find_root(a)
            r_b = find_root(b)

            root[r_b] = r_a

        for a, b in edges:
            if find_root(a) == find_root(b):
                return False

            join(a, b)

        r = find_root(0)

        return all(find_root(i) == r for i in range(n))