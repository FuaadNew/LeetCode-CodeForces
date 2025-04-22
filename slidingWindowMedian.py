from typing import List
from collections import  defaultdict
import heapq

class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        small,large = [],[]
        delete = defaultdict(int)

        for i in range(k):
            heapq.heappush(small,-nums[i])
        
        for i in range(k//2):
            heapq.heappush(large,-heapq.heappop(small))
        
        res = [-small[0] if k & 1 else (large[0] - small[0])/2 ]

        for i in range(k,len(nums)):
            delete[nums[i-k]]+=1
            balance = -1 if nums[i-k] <= -small[0] else 1

            if nums[i] <= -small[0]:
                heapq.heappush(small,-nums[i])
                balance+=1
            else:
                heapq.heappush(large,nums[i])
                balance-=1
            
            if balance < 0:
                heapq.heappush(small,-heapq.heappop(large))
            if balance > 0:
                heapq.heappush(large,-heapq.heappop(small))

            while small and delete[-small[0]] > 0:
                delete[-heapq.heappop(small)]-=1
            
            while large and delete[large[0]] > 0:
                delete[heapq.heappop(large)]-=1
            
            res.append(-small[0] if k & 1 else (large[0] - small[0])/2)
        return res

if __name__ == "__main__":
    medianFinder = Solution()
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3

    print(medianFinder.medianSlidingWindow(nums,k))
