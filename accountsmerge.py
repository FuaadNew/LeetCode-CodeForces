from typing import List
from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        adj = defaultdict(list)
        email_to_name = {}
        visit = set()
        res = []

        for account in accounts:
            name = account[0]

            for email in account[1:]:
                adj[account[1]].append(email)
                adj[email].append(account[1])

                email_to_name[email] = name




        for email in adj:
            if email not in visit:
                stack = [email]
                local_res = []

                while stack:
                    node = stack.pop()

                    if node not in visit:
                        visit.add(node)
                        local_res.append(node)

                        for nei in adj[node]:
                            if nei not in visit:
                                stack.append(nei)
                res.append([email_to_name[email]] + sorted(local_res))
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.accountsMerge([["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]))