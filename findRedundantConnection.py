class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {i:i for i in range(1,len(edges)+1)}
        rank = {i:0 for i in range(1,len(edges)+1)}

        def find(node):
            if parent[node] == node:
                return parent[node]
            return find(parent[node])

        def union(node1,node2):
            p1,p2 = find(node1),find(node2)
            if p1 == p2:
                return False
            if rank[p1]> rank[p2]:
                parent[p2] = p1
            else:
                parent[p1] = p2
            return True
        
        for node1,node2 in edges:
            if not union(node1,node2):
                return [node1,node2]
        