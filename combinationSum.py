class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, subset, curSum):
            # Base cases
            if curSum == target:
                res.append(subset[:])
                return
            if i >= len(candidates) or curSum > target:
                return

            # Include current number (can reuse it)
            subset.append(candidates[i])
            dfs(i, subset, curSum + candidates[i])

            # Exclude current number
            subset.pop()
            dfs(i + 1, subset, curSum)

        dfs(0, [], 0)
        return res