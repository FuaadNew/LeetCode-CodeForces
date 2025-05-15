class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Dictionary to store (prefixSum : frequency)
        prefixSums = {0: 1}
        # Count of valid subarrays
        res = 0   
        # Running prefix sum
        prefix = 0     
        
        for n in nums:
           # Update running sum
            prefix += n 
            diff = prefix - k            
             # Check if there's a previous prefix that sums to k

            if diff in prefixSums:
              # Add the count of how many times that prefix occurred
                res += prefixSums[diff] 
            
            # Update the frequency of the current prefix sum
            prefixSums[prefix] = 1 + prefixSums.get(prefix, 0)
        
        return res
if __name__ == '__main__':
    s = Solution()
    print(s.subarraySum([1,2,3], 3)) # 2
    print(s.subarraySum([1,1,1], 2)) # 2