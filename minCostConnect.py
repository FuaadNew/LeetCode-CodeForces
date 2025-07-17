from collections import defaultdict
import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Build the graph using an adjacency list
        adj = defaultdict(list)
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i + 1, len(points)):
                x2, y2 = points[j]
                dist = abs(x1 - x2) + abs(y1 - y2)  # Manhattan distance
                adj[i].append((dist, j))
                adj[j].append((dist, i))

        # Prim’s Algorithm setup
        minHeap = [(0, 0)]  # (cost, node)
        visited = set()
        res = 0

        # Continue until all nodes are included in the MST
        while len(visited) < len(points):
            cost, point = heapq.heappop(minHeap)

            if point in visited:
                continue

            res += cost
            visited.add(point)

            # Push neighbors that are not yet in MST
            for neiCost, nei in adj[point]:
                if nei not in visited:
                    heapq.heappush(minHeap, (neiCost, nei))

        return res