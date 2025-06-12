from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        # Recursive helper function
        def dfs(i, subset):
            # Base case: end of list
            if i == len(nums):
                res.append(subset[:])  # Append a copy of current subset
                return

            # Include nums[i]
            subset.append(nums[i])
            dfs(i + 1, subset)

            # Exclude nums[i]
            subset.pop()
            dfs(i + 1, subset)

        dfs(0, [])
        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.subsets([1, 2, 3]))