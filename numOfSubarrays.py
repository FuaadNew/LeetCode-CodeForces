class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0
        res = 0
        curSum = 0
        for r in range(len(arr)):
            curSum+=arr[r]
            if (r - l + 1) == k:
                if (curSum / (r-l+1)) >= threshold:
                    res+=1
                curSum-=arr[l]
                l+=1
            
        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.numOfSubarrays([2,2,2,2,5,5,5,8], 3, 4))
    print(sol.numOfSubarrays([11,13,17,23,29,31,7,5,2,3], 3, 5))
    print(sol.numOfSubarrays([7,7,7,7,7,7,7], 7, 7))
    print(sol.numOfSubarrays([4,4,4,4], 4, 1))