class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        rightProduct = [1] * len(nums)
        leftProduct = []
        ans = []
        prod = 1
        for n in nums:
            leftProduct.append(prod)
            prod*=n
            
        prod = 1
        ans = []
        for i in range(len(nums)-1,-1,-1):
            rightProduct[i] = prod
            prod*=nums[i]
        for i in range(len(nums)):
            ans.append(rightProduct[i] * leftProduct[i]) 
        return ans

if __name__ == '__main__':  
    s = Solution()
    print(s.productExceptSelf([1,2,3,4]))  