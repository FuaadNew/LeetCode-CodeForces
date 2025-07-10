class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        hashSet = {}
        for n in nums:
            hashSet[n] = hashSet.get(n,0) + 1
        res =[]
        def dfs(i,subsets):
            if i > len(nums):
                return
            if len(subsets) == len(nums):
                res.append(subsets[:])
                return
            for n in hashSet:
                if hashSet[n] > 0:
                    subsets.append(n)
                    hashSet[n]-=1
                    dfs(i+1,subsets)
                    subsets.pop()
                    hashSet[n]+=1
        dfs(0,[])
        return res
         