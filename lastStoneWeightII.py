class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stones_sum = sum(stones)
        target = (stones_sum)//2

        memo = {}
        def dfs(i,total):
            if i>= len(stones) or total > target:
                return abs(total - (stones_sum - total))
            if (i,total) in memo:
                return memo[(i,total)]
            
            include = dfs(i+1, total + stones[i])
            exclude = dfs(i+1, total)

            memo[(i,total)] = min(include,exclude)

            return memo[(i,total)]
        return dfs(0,0)



