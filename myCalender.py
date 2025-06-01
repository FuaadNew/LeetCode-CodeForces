class MyCalendar:

    def __init__(self):
        self.calender = []

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.calender:
            self.calender.append((startTime, endTime))
            return True
        
        # Binary search to find insertion point
        l, r = 0, len(self.calender)
        while l < r:
            mid = (l + r) // 2
            if self.calender[mid][0] <= startTime:
                l = mid + 1
            else:
                r = mid

        # Check for overlap with neighbors
        if self.intercepts(l, startTime, endTime):
            return False
        
        # Safe to book the event
        self.calender.insert(l, (startTime, endTime))
        return True

    def intercepts(self, index, start, end):
        return ((self.calender[index - 1][1] > start if index >= 1 else False) or 
                (self.calender[index][0] < end if index < len(self.calender) else False))

if __name__ == "__main__":
    myCalendar = MyCalendar()
    print(myCalendar.book(10, 20))
    print(myCalendar.book(15, 25))
    print(myCalendar.book(20, 30))