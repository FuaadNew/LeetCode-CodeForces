from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build adjacency list: course -> list of prerequisites
        adj = defaultdict(list)
        for a, b in prerequisites:
            adj[a].append(b)

        # DFS helper to detect cycles
        def dfs(course, visit):
            # If course has no prerequisites, it's safe
            if adj[course] == []:
                return True
            # If course is already in the current DFS path, there's a cycle
            if course in visit:
                return False

            # Mark course as being visited in current DFS path
            visit.add(course)

            # Recurse into prerequisites
            for pre in adj[course]:
                if not dfs(pre, visit):
                    return False

            # Backtrack: remove course from path and memoize
            visit.remove(course)
            adj[course] = []  # Memoize that this course is safe
            return True

        # Run DFS on every course
        for i in range(numCourses):
            if not dfs(i, set()):
                return False

        return True

