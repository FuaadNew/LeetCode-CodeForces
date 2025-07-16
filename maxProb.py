import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # Build the adjacency list with probability-weighted edges
        adj = { i: [] for i in range(n) }
        for i in range(len(edges)):
            node1, node2 = edges[i]
            prob = succProb[i]
            adj[node1].append((prob, node2))
            adj[node2].append((prob, node1))

        # Max heap: store (-probability, node), negative to simulate max-heap
        maxHeap = [(-1, start_node)]
        visit = set()

        while maxHeap:
            prob, node = heapq.heappop(maxHeap)
            if node in visit:
                continue
            visit.add(node)
            prob = -prob  # Convert back to positive

            # Found the end node; return current max probability
            if node == end_node:
                return prob

            # Explore neighbors with updated probabilities
            for edgeProb, nei in adj[node]:
                newProb = prob * edgeProb
                heapq.heappush(maxHeap, (-newProb, nei))  # Push negated prob to maintain max-heap

        # If end node wasn't reached
        return 0
