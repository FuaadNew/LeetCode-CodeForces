from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r = 0,len(height)-1
        res = 0
        while l<r:
            area = min(height[l],height[r]) *(r -l)
            res = max(area,res)
            if height[r] < height[l]:
                r-=1
            else:
                l+=1
        return res

if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]
    print(Solution().maxArea(height))
