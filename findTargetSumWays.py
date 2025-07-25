class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(i, curSum):
            # Check if result is already computed
            if (i, curSum) in memo:
                return memo[(i, curSum)]

            # Base case: if we've considered all numbers
            if i == len(nums):
                return 1 if curSum == target else 0

            # Try adding and subtracting the current number
            add = dfs(i + 1, curSum + nums[i])
            subtract = dfs(i + 1, curSum - nums[i])

            # Memoize and return the total number of ways
            memo[(i, curSum)] = add + subtract
            return memo[(i, curSum)]

        return dfs(0, 0)
