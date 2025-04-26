from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        curSum = 0
        for n in nums:
            curSum = max(curSum + n, n)
            maxSum = max(curSum, maxSum)
        return maxSum

if __name__ == "__main__":
    solution = Solution()
    print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
