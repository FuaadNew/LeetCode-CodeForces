class Solution:
    def trap(self, height: List[int]) -> int:
        # Step 1: Build the prefix max array
        prefix = []
        pre = 0
        for h in height:
            pre = max(pre, h)        # Track the max height from the left
            prefix.append(pre)       # Store the current max for each index

        # Step 2: Build the postfix max array (right to left)
        postfix = [0] * len(height)
        post = 0
        for i in range(len(height) - 1, -1, -1):
            post = max(post, height[i])  # Track the max height from the right
            postfix[i] = post            # Store the current max for each index

        # Step 3: Calculate total trapped water
        res = 0
        for i in range(len(height)):
            level = min(prefix[i], postfix[i])  # Water level is the min of max heights from both sides
            res += level - height[i]            # Water trapped at index = level - height

        return res  # Return total amount of trapped water

if __name__ == "__main__":
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(Solution().trap(height))