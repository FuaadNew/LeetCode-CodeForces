from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashDict = {}
        for i,n in enumerate(nums):
            diff = target - n 
            if diff in hashDict:
                return [hashDict[diff],i]
            hashDict[n] = i
        print(hashDict)


if __name__ =="__main__":
    solution = Solution()
    nums = [2,7,11,15]
    target = 9
    print(solution.twoSum(nums,target))
