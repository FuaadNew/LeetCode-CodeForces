class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        curSet = []  # Current permutation being built
        res = []     # Final list of all permutations

        def dfs():
            # Base case: if curSet is a complete permutation
            if len(curSet) == len(nums):
                res.append(curSet.copy())  # Add a copy to results
                return

            # Try each number not yet used
            for n in nums:
                if n not in curSet:
                    curSet.append(n)   # Choose
                    dfs()              # Explore
                    curSet.pop()       # Backtrack

        dfs()
        return res
