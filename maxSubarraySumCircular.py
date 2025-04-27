from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        subMax,subMin,total = nums[0],nums[0],0
        curMax,curMin = 0,0

        for n in nums:
            total+=n
            curMax = max(curMax + n, n)
            curMin = min(curMin + n, n)
            subMax = max(subMax, curMax)
            subMin = min(subMin, curMin)
        
        if subMax < 0:
            return subMax
        return max(total - subMin, subMax)

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxSubarraySumCircular([1,-2,3,-2]))