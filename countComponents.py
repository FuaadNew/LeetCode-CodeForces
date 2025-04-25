from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visit = set()
        adj = {i:[] for i in range(n)}
        res =0

        for node1,node2 in edges:
            adj[node1].append(node2)
            adj[node2].append(node1)

        

        def dfs(node):
            if node in visit:
                return
            visit.add(node)
            for nei in adj[node]:
                    dfs(nei)
            return True


        for node in adj:
            if dfs(node):
                res+=1
        return res
    
if __name__ == "__main__":
    sol = Solution()
    print(sol.countComponents(5, [[0,1],[1,2],[3,4]]))