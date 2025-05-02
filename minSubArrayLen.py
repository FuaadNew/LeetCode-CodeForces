from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLength = float('inf')
        l = 0
        curSum =0
        for r in range(len(nums)):
            curSum +=nums[r]
            while curSum >= target:
                minLength = min(minLength, r - l + 1)
                curSum-=nums[l]
                l+=1
        return minLength if minLength!= float('inf') else 0

if __name__ == "__main__":
    solution = Solution()
    print(solution.minSubArrayLen(7, [2,3,1,2,4,3]))
