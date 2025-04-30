from typing import List
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        l = 0
        for r in range(len(nums)):
            if r - l + 1 > k + 1:
                window.remove(nums[l])
                l+=1
            if nums[r] in window:
                return True
            window.add(nums[r])
        return False
if __name__ == "__main__":
    solution = Solution()
    print(solution.containsNearbyDuplicate([1,2,3,1], 3))
    print(solution.containsNearbyDuplicate([1,0,1,1], 1))
    print(solution.containsNearbyDuplicate([1,2,3,1,2,3], 2))
