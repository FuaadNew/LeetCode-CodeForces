from typing import List
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return 1
        if len(arr) == 2 and arr[0]!=arr[1]:
            return 2
        length,res = 1,0
        sign = None

        for i in range(1,len(arr)):
            if arr[i-1] == arr[i]:
                length = 1
                sign = None
            elif arr[i-1] > arr[i] and (sign == ">" or sign == None):
                length+=1
                sign = "<"
            elif arr[i-1] < arr[i] and (sign == "<" or sign == None):
                length+=1
                sign = ">"
            else:
                length = 2

            

            res = max(res,length)
        return res

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxTurbulenceSize([9,4,2,10,7,8,8,1,9]))
    print(sol.maxTurbulenceSize([4,8,12,16]))
    print(sol.maxTurbulenceSize([100]))
    
