class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Mapping from digit to corresponding characters
        keyboard = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        res = []

        # Edge case: empty input returns no combinations
        if not digits:
            return []

        # Helper function for DFS traversal
        def dfs(i, subset):
            # If we've built a full combination, add to result
            if i == len(digits):
                res.append("".join(subset))
                return

            # Iterate over all possible letters for the current digit
            for c in keyboard[digits[i]]:
                subset.append(c)          # Choose the letter
                dfs(i + 1, subset)        # Explore deeper
                subset.pop()              # Backtrack

        # Start DFS with an empty subset
        dfs(0, [])
        return res