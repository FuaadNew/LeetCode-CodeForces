class NumArray:
    def __init__(self, nums: List[int]):
        self.prefix = []
        total = 0
        for n in nums:
            total += n              # Add current number to running total
            self.prefix.append(total)  # Store the prefix sum up to this index

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefix[right]  # If starting from index 0, return prefix directly
        return self.prefix[right] - self.prefix[left - 1]  # Subtract prefix up to (left - 1)

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5]
    obj = NumArray(nums)
    print(obj.sumRange(0, 2))  # Output: 6
    print(obj.sumRange(2, 4))  # Output: 12
