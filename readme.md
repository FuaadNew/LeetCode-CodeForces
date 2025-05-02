# LeetCode/CodeForces Solutions

This repository contains my solutions to various competitive programming problems from platforms like LeetCode and CodeForces.

## Problems

### Two Sum (LeetCode)

File: [twoSum.py](./twoSum.py)

**Problem Description:**
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to the target.

**Approach:**
- Hash map-based solution with O(n) time complexity
- For each number, check if its complement (target - current number) exists in the hash map
- If found, return the indices of both numbers
- Otherwise, add the current number and its index to the hash map

**How to run:**
```bash
python twoSum.py
```

### Find Median from Data Stream (LeetCode #295)

File: [medianFinder.py](./medianFinder.py)

**Problem Description:**
Design a data structure that supports adding integers and finding the median of the stream at any time.

**Approach:**
- Uses two heaps to maintain the stream of numbers
- Small heap (max heap) stores the smaller half of numbers
- Large heap (min heap) stores the larger half of numbers
- Carefully balances the heaps after each insertion
- O(log n) time for adding numbers and O(1) for finding median

**How to run:**
```bash
python medianFinder.py
```

### Sliding Window Median (LeetCode #480)

File: [slidingWindowMedian.py](./slidingWindowMedian.py)

**Problem Description:**
Find the median of all the elements in a sliding window of size k as it moves from the beginning to the end of an array.

**Approach:**
- Extension of the two-heap approach used in Find Median from Data Stream
- Uses a hashmap to track elements that need to be removed from heaps
- Lazy removal approach to maintain heap structure efficiently
- Handles window sliding with careful rebalancing of heaps
- Time complexity: O(n log k) where n is the length of array and k is window size

**How to run:**
```bash
python slidingWindowMedian.py
```

### Redundant Connection (LeetCode #684)

File: [redundantConnection.py](./redundantConnection.py)

**Problem Description:**
In an undirected graph formed from a tree with an additional edge, find and return the edge that can be removed to make the graph a tree again.

**Approach:**
- Uses Union-Find (Disjoint Set) algorithm
- Tracks connected components and detects cycles
- When adding an edge creates a cycle, that edge is redundant
- Time complexity: O(n) where n is the number of edges, with path compression
- Space complexity: O(n) for parent and rank tracking

**How to run:**
```bash
python redundantConnection.py
```

### Implement Trie (Prefix Tree) (LeetCode #208)

File: [implementTrie.py](./implementTrie.py)

**Problem Description:**
Implement a trie (prefix tree) with insert, search, and startsWith methods.

**Approach:**
- Uses a custom TrieNode class with children dictionary and word flag
- Insert: builds a path in the trie for each character, marking the end as a complete word
- Search: traverses the trie to find if a word exists completely
- StartsWith: checks if a prefix exists in the trie
- Time complexity: O(m) for all operations, where m is the key length
- Space complexity: O(n) where n is total number of characters across all keys

**How to run:**
```bash
python implementTrie.py
```

### Number of Connected Components in an Undirected Graph (LeetCode #323)

File: [countComponents.py](./countComponents.py)

**Problem Description:**
Count the number of connected components in an undirected graph with n nodes labeled from 0 to n-1 and a list of undirected edges.

**Approach:**
- Uses Depth-First Search (DFS) to traverse connected components
- Builds an adjacency list representation of the graph
- Iterates through all nodes and performs DFS from unvisited nodes
- Increments counter for each new connected component discovered
- Time complexity: O(V + E) where V is number of vertices and E is number of edges
- Space complexity: O(V + E) for adjacency list and visited set

**How to run:**
```bash
python countComponents.py
```

### Accounts Merge (LeetCode #721)

File: [accountsmerge.py](./accountsmerge.py)

**Problem Description:**
Given a list of accounts where each account contains a name and a list of emails, merge accounts that belong to the same person (i.e., have at least one common email).

**Approach:**
- Uses depth-first search (DFS) to find connected email addresses
- Builds an adjacency list to represent connections between emails
- Maps emails to account names
- Performs DFS starting from each unvisited email to find all connected emails
- Sorts emails within each merged account for consistent output
- Time complexity: O(n log n) where n is the total number of emails
- Space complexity: O(n) for adjacency list and visited set

**How to run:**
```bash
python accountsmerge.py
```

### Maximum Subarray (LeetCode #53)

File: [maximumSubArray.py](./maximumSubArray.py)

**Problem Description:**
Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

**Approach:**
- Uses Kadane's algorithm to find maximum subarray sum
- Maintains two variables: current sum and maximum sum
- For each element, decides whether to extend the current subarray or start a new one
- Time complexity: O(n) where n is the length of the array
- Space complexity: O(1) using only constant extra space

**How to run:**
```bash
python maximumSubArray.py
```

### Maximum Subarray Sum Circular (LeetCode #918)

File: [maxSubarraySumCircular.py](./maxSubarraySumCircular.py)

**Problem Description:**
Given a circular integer array `nums`, find the maximum possible sum of a non-empty subarray, considering the array as circular (meaning the last element connects to the first element).

**Approach:**
- Extended version of Kadane's algorithm that works with circular arrays
- Computes both maximum subarray sum (standard case) and minimum subarray sum
- For circular case, the maximum sum equals total sum minus minimum subarray sum
- Handles the edge case when all elements are negative
- Time complexity: O(n) where n is the length of the array
- Space complexity: O(1) using only constant extra space

**How to run:**
```bash
python maxSubarraySumCircular.py
```

### Swim in Rising Water (LeetCode #778)

File: [swimInRisingWater.py](./swimInRisingWater.py)

**Problem Description:**
Given an N x N grid where each cell has a height, find the minimum time needed to swim from the top-left corner to the bottom-right corner. You can swim from one cell to another if the water level is at least the height of the destination cell.

**Approach:**
- Uses Dijkstra's algorithm with a min-heap to find the minimum time path
- Tracks visited cells to avoid revisiting
- For each cell, considers all four possible directions (up, down, left, right)
- The time to reach a cell is the maximum of the current time and the cell's height
- Time complexity: O(N² log N) where N is the grid size
- Space complexity: O(N²) for the visited set and heap

**How to run:**
```bash
python swimInRisingWater.py
```

### Longest Turbulent Subarray (LeetCode #978)

File: [longestTurbulentArray.py](./longestTurbulentArray.py)

**Problem Description:**
Given an integer array `arr`, find the length of a maximum size turbulent subarray. A subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

**Approach:**
- Uses a sliding window approach to track the turbulent subarray length
- Maintains the current comparison sign and length of the turbulent subarray
- Resets the length when adjacent elements are equal or when the sign pattern breaks
- Time complexity: O(n) where n is the length of the array
- Space complexity: O(1) using only constant extra space

**How to run:**
```bash
python longestTurbulentArray.py
```

### Contains Duplicate II (LeetCode #219)

File: [containsDuplicate.py](./containsDuplicate.py)

**Problem Description:**
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

**Approach:**
- Uses sliding window technique with a set to track elements
- Maintains a window of size k+1 using two pointers
- Checks for duplicates within the window
- Time complexity: O(n) where n is the length of the array
- Space complexity: O(k) for the sliding window set

**How to run:**
```bash
python containsDuplicate.py
```

### Number of Subarrays with Average Above Threshold (LeetCode #1343)

File: [numOfSubarrays.py](./numOfSubarrays.py)

**Problem Description:**
Given an array of integers `arr`, an integer `k`, and a threshold, return the number of subarrays of size `k` whose average is greater than or equal to the threshold.

**Approach:**
- Uses sliding window technique for efficient computation
- Maintains a running sum of the current window
- For each window of size k, checks if the average meets the threshold
- Time complexity: O(n) where n is the length of the array
- Space complexity: O(1) using constant extra space

**How to run:**
```bash
python numOfSubarrays.py
```

### Minimum Size Subarray Sum (LeetCode #209)

File: [minSubArrayLen.py](./minSubArrayLen.py)

**Problem Description:**
Given an array of positive integers `nums` and a positive integer `target`, return the minimal length of a subarray whose sum is greater than or equal to `target`. If there is no such subarray, return 0.

**Approach:**
- Uses sliding window technique to find the minimum length subarray
- Maintains a window with left and right pointers
- Expands the window by moving the right pointer and shrinks it by moving the left pointer
- Keeps track of the current sum and minimum length found
- Time complexity: O(n) where n is the length of the array
- Space complexity: O(1) using only constant extra space

**How to run:**
```bash
python minSubArrayLen.py
```

# Usage

Each solution can be run individually. The code includes test cases to demonstrate functionality.
