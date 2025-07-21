from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = defaultdict(list)  # Build adjacency list
        res = []                 # Holds the topological order

        # Fill adjacency list with prerequisite edges
        for a, b in prerequisites:
            adj[a].append(b)

        # DFS function with cycle detection
        def dfs(crs, visit):
            if crs in visit:
                return False  # Cycle detected
            if adj[crs] == []:
                if crs not in res:
                    res.append(crs)  # Already processed
                return True

            visit.add(crs)

            for pre in adj[crs]:
                if not dfs(pre, visit):
                    return False

            visit.remove(crs)
            adj[crs] = []      # Memoize this node
            res.append(crs)    # Add course to result after all prereqs
            return True

        # Try to schedule all courses
        for i in range(numCourses):
            if not dfs(i, set()):
                return []  # Cycle found — scheduling not possible

        return res
