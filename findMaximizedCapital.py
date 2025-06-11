import heapq
from typing import List
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        minHeap = [(c,p) for c,p in zip(capital,profits)]
        maxHeap = []
        heapq.heapify(minHeap)

   

        for _ in range(k):
            while minHeap and minHeap[0][0] <= w:
                c,p = heapq.heappop(minHeap)
                heapq.heappush(maxHeap,-p)
            if not maxHeap:
                break
            w+= -heapq.heappop(maxHeap)
        return w
if __name__ == "__main__":
    solution = Solution()
    print(solution.findMaximizedCapital(2,0,[1,2,3],[0,1,1]))   