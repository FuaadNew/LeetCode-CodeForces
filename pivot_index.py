class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            leftTotal,rightTotal = 0,0
            for j in range(i):
                leftTotal+=nums[j]
            for j in range(i+1,len(nums)):
                rightTotal+=nums[j]
            if leftTotal == rightTotal:
                return i
        return -1
if __name__ == '__main__':
    nums = [1,7,3,6,5,6]
    print(Solution().pivotIndex(nums))