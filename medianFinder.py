import heapq

class MedianFinder:

    def __init__(self):
        self.small = []  # Max heap (store negatives for largest value on top)
        self.large = []  # Min heap (store as-is for smallest value on top)

    def addNum(self, num: int) -> None:
        # Add to max heap (simulate by pushing negative)
        heapq.heappush(self.small, -num)

        # Ensure ordering: small's max should be <= large's min
        if self.small and self.large and (-self.small[0] > self.large[0]):
            heapq.heappush(self.large, -heapq.heappop(self.small))

        # Balance the heaps
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))
        elif len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        # Even number of elements
        return (-self.small[0] + self.large[0]) / 2
