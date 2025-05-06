from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers)-1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            if numbers[l] + numbers[r] > target:
                r-=1
            if numbers[l] + numbers[r] < target:
                l+=1

if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([2,7,11,15], 9))
    print(solution.twoSum([2,3,4], 6))
    print(solution.twoSum([-1,0], -1))
