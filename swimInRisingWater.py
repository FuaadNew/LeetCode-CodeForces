import heapq
from typing import List

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = set()
        minHeap = [(grid[0][0],0,0)]

        directions = [[0,1],[1,0],[0,-1],[-1,0]]

        while minHeap:
            t,r,c = heapq.heappop(minHeap)


            if r == N -1 and c == N - 1:
                return t
            for dr,dc in directions:
                nr,nc = dr + r, dc + c
                

                if 0 <= nr < N and 0<= nc < N and (nr,nc) not in visit:
                    visit.add((nr,nc))
                    time = max(t,grid[nr][nc])
                    

                    heapq.heappush(minHeap, (time, nr, nc))
            
if __name__ == "__main__":
    grid = [[0,1],[1,0]]
    print(Solution().swimInWater(grid))