import heapq

class MedianFinder:

    def __init__(self):
        self.small = [] #max Heap largest value in 0
        self.large = [] #min Heap smallest value in 0
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small,-num)

        if (self.small and self.large) and ((self.small[0]  * - 1) > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large,val)

        if len(self.small) > len(self.large):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large,val)

        elif len(self.large) > len(self.small):
            val = -1 * heapq.heappop(self.large)
            heapq.heappush(self.small,val)

        

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]

        return ((-1 * self.small[0]) + self.large[0])/2
        


if __name__ == "__main__":
    obj = MedianFinder()
    obj.addNum(1)
    obj.addNum(2)
    print(obj.findMedian())
    obj.addNum(3)
    print(obj.findMedian())



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()