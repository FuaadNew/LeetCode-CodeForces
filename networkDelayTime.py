import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # 1. Build adjacency list
     
        adj = {i: [] for i in range(1, n + 1)}
        for u, v, w in times:
            adj[u].append((w, v))        # (edge weight, destination)

  
        # 2. Dijkstra setup

        minHeap = [(0, k)]               # (current distance, node)
        visited = set()
        maxTime = 0                      # tracks the longest shortest-path

     
        # 3. Main loop
       
        while minHeap:
            dist, node = heapq.heappop(minHeap)

            # Skip if this node’s shortest path is already settled
            if node in visited:
                continue
            visited.add(node)

            # Update the overall maximum time seen so far
            maxTime = max(maxTime, dist)

            # Push neighbors with updated distances
            for weight, nei in adj[node]:
                if nei not in visited:
                    heapq.heappush(minHeap, (dist + weight, nei))


       
        # If we reached every node, maxTime is the network delay;
        # otherwise, some nodes were unreachable.
        return maxTime if len(visited) == n else -1
