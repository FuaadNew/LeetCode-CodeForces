from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Sort to group duplicates
        res = []

        def dfs(i, subset):
            if i == len(nums):
                res.append(subset[:])
                return

            # Include nums[i]
            subset.append(nums[i])
            dfs(i + 1, subset)
            subset.pop()

            # Skip duplicates
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            # Exclude nums[i]
            dfs(i + 1, subset)

        dfs(0, [])
        return res


if __name__ == "__main__":
    sol = Solution()
    print(sol.subsetsWithDup([1, 2, 2]))
    # [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]] 