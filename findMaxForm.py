class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        memo = {}

        def dfs(i, m, n):
            # Base case: no more strings
            if i >= len(strs):
                return 0

            # Check memo table
            if (i, m, n) in memo:
                return memo[(i, m, n)]

            # Count 0s and 1s in current string
            m_count = strs[i].count("0")
            n_count = strs[i].count("1")

            new_m = m - m_count
            new_n = n - n_count

            # Option 1: Skip current string if it exceeds budget
            if new_m < 0 or new_n < 0:
                memo[(i, m, n)] = dfs(i + 1, m, n)
                return memo[(i, m, n)]

            # Option 2: Choose max between including or excluding the string
            include = 1 + dfs(i + 1, new_m, new_n)
            exclude = dfs(i + 1, m, n)
            memo[(i, m, n)] = max(include, exclude)

            return memo[(i, m, n)]

        return dfs(0, m, n)
