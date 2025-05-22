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

### Two Sum II (LeetCode #167)

File: [twoSum_two.py](./twoSum_two.py)

**Problem Description:**
Given a 1-indexed array of integers `numbers` that is already sorted in non-decreasing order, find two numbers such that they add up to a specific `target` number. Return the indices of the two numbers, where index1 must be less than index2.

**Approach:**
- Two-pointer solution with O(n) time complexity
- Uses left and right pointers starting from both ends of the array
- Moves pointers inward based on the sum comparison with target
- Returns 1-indexed positions of the two numbers
- Space complexity: O(1) as it uses constant extra space

**How to run:**
```bash
python twoSum_two.py
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

Files: 
- [implementTrie.py](./implementTrie.py) - Original implementation
- [trieNode.py](./trieNode.py) - Modular implementation

**Problem Description:**
Implement a trie (prefix tree) with insert, search, and startsWith methods.

**Approach:**
- Uses a custom TrieNode class with children dictionary and word flag
- Insert: builds a path in the trie for each character, marking the end as a complete word
- Search: traverses the trie to find if a word exists completely
- StartsWith: checks if a prefix exists in the trie
- Time complexity: O(m) for all operations, where m is the key length
- Space complexity: O(n) where n is total number of characters across all keys

**Implementation Details (trieNode.py):**
- Modular implementation with separate TrieNode and Trie classes
- TrieNode class manages character nodes and word flags
- Trie class provides the public interface for operations
- Clean, reusable implementation for other prefix-based problems

**How to run:**
```bash
python implementTrie.py
python trieNode.py
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

### Longest Repeating Character Replacement (LeetCode #424)

File: [characterReplacement.py](./characterReplacement.py)

**Problem Description:**
Given a string `s` and an integer `k`, find the length of the longest substring containing the same letter that can be obtained by replacing at most `k` characters.

**Approach:**
- Uses sliding window technique with a character count dictionary
- Maintains a window where the number of replacements needed (window length - max frequency) is at most `k`
- Adjusts window size dynamically while tracking character frequencies
- Time complexity: O(n) where n is the length of the string
- Space complexity: O(1) as we only store counts for a fixed number of characters

**How to run:**
```bash
python characterReplacement.py
```

### Valid Palindrome (LeetCode #125)

File: [isPalindrome.py](./isPalindrome.py)

**Problem Description:**
Given a string `s`, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

**Approach:**
- Uses two-pointer technique starting from both ends of the string
- Skips non-alphanumeric characters using a helper function
- Compares characters case-insensitively
- Time complexity: O(n) where n is the length of the string
- Space complexity: O(1) using only constant extra space

**How to run:**
```bash
python isPalindrome.py
```

### Container With Most Water (LeetCode #11)

File: [maxArea.py](./maxArea.py)

**Problem Description:**
Given n non-negative integers representing the height of vertical lines, find two lines that together with the x-axis forms a container that holds the most water.

**Approach:**
- Uses two-pointer technique starting from both ends of the array
- Moves the pointer with the smaller height inward
- Keeps track of the maximum area found
- Time complexity: O(n) where n is the length of the array
- Space complexity: O(1) using only constant extra space

**How to run:**
```bash
python maxArea.py
```

### Remove Duplicates from Sorted Array II (LeetCode #80)

File: [removeDuplicates.py](./removeDuplicates.py)

**Problem Description:**
Given a sorted array `nums`, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

**Approach:**
- Uses two-pointer technique with O(n) time complexity
- Maintains array in-place with O(1) extra space
- Allows at most 2 occurrences of each element
- Returns the length of the modified array

**How to run:**
```bash
python removeDuplicates.py
```

### Trapping Rain Water (LeetCode #42)

File: [trap.py](./trap.py)

**Problem Description:**
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

**Approach:**
- Uses dynamic programming with prefix and postfix arrays
- Tracks maximum heights from both left and right sides
- Water trapped at each index is determined by the minimum of max heights from both sides
- Time complexity: O(n) where n is the length of the array
- Space complexity: O(n) for storing prefix and postfix arrays

**How to run:**
```bash
python trap.py
```

### Find Pivot Index (LeetCode #724)

File: [pivot_index.py](./pivot_index.py)

**Problem Description:**
Given an array of integers `nums`, calculate the pivot index of this array. The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

**Approach:**
- Uses linear scan to check each index as potential pivot
- For each index, calculates sum of elements to its left and right
- Returns the first index where left sum equals right sum
- Time complexity: O(n²) where n is the length of the array
- Space complexity: O(1) using only constant extra space

**How to run:**
```bash
python pivot_index.py
```

### Range Sum Query - Immutable (LeetCode #303)

File: [numArray.py](./numArray.py)

**Problem Description:**
Given an integer array `nums`, handle multiple queries of the following type: Calculate the sum of the elements of `nums` between indices `left` and `right` inclusive.

**Approach:**
- Uses prefix sum array for O(1) range queries
- Precomputes cumulative sums during initialization
- Efficiently calculates range sums by subtracting prefix sums
- Time complexity: O(n) for initialization, O(1) for range queries
- Space complexity: O(n) for storing prefix sums

**How to run:**
```bash
python numArray.py
```

### Range Sum Query 2D - Immutable (LeetCode #304)

File: [sumRegion.py](./sumRegion.py)

**Problem Description:**
Given a 2D matrix `matrix`, handle multiple queries of the following type: Calculate the sum of the elements of `matrix` inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

**Approach:**
- Uses 2D prefix sum matrix for O(1) range queries
- Precomputes cumulative sums during initialization
- Uses inclusion-exclusion principle for submatrix sum calculation
- Time complexity: O(mn) for initialization, O(1) for range queries
- Space complexity: O(mn) for storing prefix sums

**How to run:**
```bash
python sumRegion.py
```

### Product of Array Except Self (LeetCode #238)

File: [productExceptSelf.py](./productExceptSelf.py)

**Problem Description:**
Given an array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`. The algorithm must run in O(n) time and without using the division operation.

**Approach:**
- Uses two arrays to store products from left and right sides
- Left product array stores running product of all elements to the left
- Right product array stores running product of all elements to the right
- Final answer at each index is product of corresponding left and right products
- Time complexity: O(n) where n is the length of the array
- Space complexity: O(n) for storing left and right product arrays

**How to run:**
```bash
python productExceptSelf.py
```

### Subarray Sum Equals K (LeetCode #560)

File: [subarraySum.py](./subarraySum.py)

**Problem Description:**
Given an array of integers `nums` and an integer `k`, return the total number of continuous subarrays whose sum equals to `k`.

**Approach:**
- Uses a hash map to store prefix sum frequencies
- For each element, calculates the running prefix sum
- Checks if (prefix sum - k) exists in the hash map
- If found, adds the frequency of that difference to the result count
- Updates the frequency of the current prefix sum in the hash map
- Time complexity: O(n) where n is the length of the array
- Space complexity: O(n) for storing the prefix sum frequencies

**How to run:**
```bash
python subarraySum.py
```

### Middle of the Linked List (LeetCode #876)

File: [middleNode.py](./middleNode.py)

**Problem Description:**
Given the head of a singly linked list, return the middle node of the linked list. If there are two middle nodes, return the second middle node.

**Approach:**
- Uses the two-pointer technique (slow and fast pointers)
- Fast pointer moves twice as fast as the slow pointer
- When fast pointer reaches the end, slow pointer is at the middle
- Time complexity: O(n) where n is the length of the linked list
- Space complexity: O(1) using only constant extra space

**How to run:**
```bash
python middleNode.py
```

### Maximum Twin Sum of a Linked List (LeetCode #2130)

File: [pairSum.py](./pairSum.py)

**Problem Description:**
In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node. Find the maximum twin sum in the linked list, where twin sum is defined as the sum of a node and its twin.

**Approach:**
- Uses two-pointer technique to find the middle of the linked list
- Reverses the second half of the linked list
- Compares corresponding nodes from the first half and reversed second half
- Calculates the maximum twin sum by iterating through both halves
- Time complexity: O(n) where n is the length of the linked list
- Space complexity: O(1) using only constant extra space

**How to run:**
```bash
python pairSum.py
```

### Linked List Cycle (LeetCode #141)

File: [hasCycle.py](./hasCycle.py)

**Problem Description:**
Given the head of a linked list, determine if the linked list has a cycle in it. A cycle occurs when a node in the linked list can be reached again by continuously following the next pointer.

**Approach:**
- Uses Floyd's Tortoise and Hare algorithm (two-pointer technique)
- Slow pointer moves one step at a time, fast pointer moves two steps
- If there is a cycle, the fast pointer will eventually meet the slow pointer
- If there is no cycle, the fast pointer will reach the end of the list
- Time complexity: O(n) where n is the length of the linked list
- Space complexity: O(1) using only constant extra space

**How to run:**
```bash
python hasCycle.py
```

### Linked List Cycle II (LeetCode #142)

File: [detectCycle.py](./detectCycle.py)

**Problem Description:**
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

**Approach:**
- Uses Floyd's Tortoise and Hare algorithm (two-pointer technique)
- First phase: Detect if a cycle exists using slow and fast pointers
- Second phase: Find the entry point of the cycle by resetting slow pointer to head
- When slow and fast pointers meet again, that node is the start of the cycle
- Time complexity: O(n) where n is the length of the linked list
- Space complexity: O(1) using only constant extra space

**How to run:**
```bash
python detectCycle.py
```

# Usage

Each solution can be run individually. The code includes test cases to demonstrate functionality.
