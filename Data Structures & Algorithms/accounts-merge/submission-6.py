class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # merge accouns by a same email
        # disjoint set?
        # node = {name, email}
        # node a connect to node b if they belong same one 
        # ndoe: account
        # how to join 
        email_to_name = {}
        parent = {}

        def find(a):
            if parent[a] != a:
                parent[a] = find(parent[a])
            return parent[a]

        def union(a, b):
            r_a = find(a)
            r_b = find(b)

            parent[r_a] = parent[r_b]

        for a in accounts:
            name = a[0]

            for e in a[1:]:
                parent[e] = e
                email_to_name[e] = name

        for a in accounts:
            name = a[0]
            email = a[1]

            for e in a[2:]:
                union(email, e)

        result_map = defaultdict(list)
        for email in parent:
            result_map[find(email)].append(email)
        
        result = []
        for root, emails in result_map.items():
            account = [email_to_name[root]]
            account.extend(sorted(emails))

            result.append(account)

        return result


        
        


