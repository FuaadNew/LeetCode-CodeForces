# LeetCode/CodeForces Solutions

This repository contains my solutions to various competitive programming problems from platforms like LeetCode and CodeForces.

## Problems

### Course Schedule (LeetCode #207)

File: [canFinish.py](./canFinish.py)

**Problem Description:**
There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you must take course `bi` first if you want to take course `ai`. Return `true` if you can finish all courses, otherwise return `false`.

**Approach:**
- Uses Depth-First Search (DFS) with cycle detection to determine if all courses can be completed
- Builds an adjacency list where each course points to its prerequisites
- Implements DFS with a visited set to detect cycles in the prerequisite graph
- If a cycle is found, it's impossible to complete all courses
- Uses memoization by clearing prerequisite lists for courses that are confirmed safe
- Backtracks properly by removing courses from the current DFS path
- Time complexity: O(V + E) where V is number of courses and E is number of prerequisites
- Space complexity: O(V + E) for adjacency list and recursion stack

**How to run:**
```bash
python canFinish.py
```

### Course Schedule II (LeetCode #210)

File: [findorder.py](./findorder.py)

**Problem Description:**
There are a total of `numCourses` courses you have to take, labeled from `0` to `numCourses - 1`. You are given an array `prerequisites` where `prerequisites[i] = [ai, bi]` indicates that you must take course `bi` first if you want to take course `ai`. Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

**Approach:**
- Uses Depth-First Search (DFS) with cycle detection to determine course scheduling order
- Builds an adjacency list where each course points to its prerequisites
- Implements DFS with a visited set to detect cycles in the prerequisite graph
- If a cycle is found, returns an empty array as scheduling is impossible
- Uses memoization by clearing prerequisite lists for courses that are confirmed safe
- Returns topological ordering of courses by appending to result after processing prerequisites
- Backtracks properly by removing courses from the current DFS path
- Time complexity: O(V + E) where V is number of courses and E is number of prerequisites
- Space complexity: O(V + E) for adjacency list and recursion stack

**How to run:**
```bash
python findorder.py
```

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

### My Calendar I (LeetCode #729)

File: [myCalender.py](./myCalender.py)

**Problem Description:**
Implement a calendar that can book events without overlapping. The MyCalendar class should support the book(startTime, endTime) method that returns true if the event can be added to the calendar successfully without causing a double booking.

**Approach:**
- Uses binary search to find the optimal insertion point for new events
- Maintains events in sorted order by start time for efficient searching
- Checks for overlaps with neighboring events using a helper method
- Returns false if booking would cause an overlap, true otherwise
- Time complexity: O(log n) for booking due to binary search and insertion
- Space complexity: O(n) to store the calendar events

**How to run:**
```bash
python myCalender.py
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

File: [findRedundantConnection.py](./findRedundantConnection.py)

**Problem Description:**
In an undirected graph formed from a tree with an additional edge, find and return the edge that can be removed to make the graph a tree again.

**Approach:**
- Uses Union-Find (Disjoint Set Union) data structure with path compression
- Maintains parent and rank arrays for efficient union operations
- Iterates through edges and attempts to union the connected nodes
- When union operation fails (nodes already connected), that edge creates a cycle
- Returns the first edge that creates a redundant connection
- Time complexity: O(n × α(n)) where α is the inverse Ackermann function (nearly constant)
- Space complexity: O(n) for parent and rank tracking

**How to run:**
```bash
python findRedundantConnection.py
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

### Word Search II (LeetCode #212)

File: [word_search.py](./word_search.py)

**Problem Description:**
Given an m x n board of characters and a list of strings words, return all words on the board. Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring.

**Approach:**
- Uses Trie data structure for efficient word storage and prefix matching
- Implements backtracking DFS to explore all possible paths on the board
- Builds a Trie from the input words for O(1) prefix lookup
- For each cell on the board, performs DFS to find all possible words
- Uses a visited set to avoid revisiting cells during the current path
- Removes found words from results using a set to avoid duplicates
- Time complexity: O(m × n × 4^L) where m,n are board dimensions and L is max word length
- Space complexity: O(W × L) for Trie storage where W is number of words

**How to run:**
```bash
python word_search.py
```

### Prefix and Suffix Search (LeetCode #745)

File: [trie_search.py](./trie_search.py)

**Problem Description:**
Design a special dictionary that can search words by a prefix and a suffix. Implement the WordFilter class with a constructor that takes an array of words and a method f(prefix, suffix) that returns the index of the word with the given prefix and suffix. If there is more than one valid index, return the largest index.

**Approach:**
- Uses Trie data structure to store all possible prefix#suffix combinations
- During initialization, generates all combinations of prefixes and suffixes for each word
- Stores the word index at each leaf node in the Trie
- For queries, combines the prefix and suffix with '#' separator and searches the Trie
- Returns the stored index if the pattern exists, -1 otherwise
- Time complexity: O(N × K²) for initialization where N is number of words and K is average word length
- Query time complexity: O(P + S) where P is prefix length and S is suffix length
- Space complexity: O(N × K²) for storing all prefix#suffix combinations

**How to run:**
```bash
python trie_search.py
```

### Accounts Merge (LeetCode #721)

File: [accountsMerge.py](./accountsMerge.py)

**Problem Description:**
Given a list of accounts where each account contains a name and a list of email addresses, merge accounts that belong to the same person. Two accounts belong to the same person if they share at least one common email address.

**Approach:**
- Uses graph-based approach with DFS traversal to find connected email groups
- Builds an adjacency list where emails within the same account are connected
- Uses DFS to find connected components (groups of emails belonging to the same person)
- Maintains a mapping from emails to names for result construction
- Returns merged accounts with names and sorted email lists
- Time complexity: O(N × M × log(M)) where N is number of accounts and M is average emails per account
- Space complexity: O(N × M) for the graph and visited tracking

**How to run:**
```bash
python accountsMerge.py
```

### Binary Search Tree Iterator (LeetCode #173)

File: [BSTIterator.py](./BSTIterator.py)

**Problem Description:**
Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST). The iterator should support next() and hasNext() methods.

**Approach:**
- Uses iterative in-order traversal with a stack for memory-efficient iteration
- Maintains a stack to store nodes and a current pointer for traversal
- next() method returns the next smallest element in the BST
- hasNext() method checks if there are more elements to iterate
- Implements lazy evaluation - only processes nodes as needed
- Time complexity: O(1) average for next() and hasNext(), O(h) worst case where h is tree height
- Space complexity: O(h) for the stack where h is the height of the tree

**How to run:**
```bash
python BSTIterator.py
```

### Binary Tree Preorder Traversal (LeetCode #144)

File: [preorderTraversal.py](./preorderTraversal.py)

**Problem Description:**
Given the root of a binary tree, return the preorder traversal of its nodes' values. Preorder traversal visits nodes in the order: root, left subtree, right subtree.

**Approach:**
- Uses recursive depth-first search (DFS) to traverse the tree
- Visits current node first, then recursively traverses left and right subtrees
- Maintains a result list to store node values in preorder sequence
- Base case handles null nodes by returning immediately
- Time complexity: O(n) where n is the number of nodes in the tree
- Space complexity: O(h) for recursion stack where h is the height of the tree

**How to run:**
```bash
python preorderTraversal.py
```

### Binary Tree Postorder Traversal (LeetCode #145)

File: [postorderTraversal.py](./postorderTraversal.py)

**Problem Description:**
Given the root of a binary tree, return the postorder traversal of its nodes' values. Postorder traversal visits nodes in the order: left subtree, right subtree, root.

**Approach:**
- Uses iterative approach with a stack and visited flags for memory-efficient traversal
- Maintains a stack of (node, visited) tuples to track traversal state
- Processes nodes only after both left and right subtrees have been visited
- Avoids recursion to prevent stack overflow for deep trees
- Time complexity: O(n) where n is the number of nodes in the tree
- Space complexity: O(h) for the stack where h is the height of the tree

**How to run:**
```bash
python postorderTraversal.py
```

### IPO (LeetCode #502)

File: [findMaximizedCapital.py](./findMaximizedCapital.py)

**Problem Description:**
You are given several projects with their capital requirements and expected profits. You can start with an initial capital w and can choose at most k projects to maximize your final capital.

**Approach:**
- Uses two-heap strategy for optimal project selection
- Min heap stores projects sorted by capital requirements
- Max heap stores available projects sorted by profit (highest first)
- Greedily selects the most profitable project that can be afforded
- For each of k iterations, moves affordable projects to max heap and selects the best one
- Time complexity: O(n log n + k log n) where n is number of projects
- Space complexity: O(n) for the heaps

**How to run:**
```bash
python findMaximizedCapital.py
```

### Subsets (LeetCode #78)

File: [subsets.py](./subsets.py)

**Problem Description:**
Given an integer array `nums` of unique elements, return all possible subsets (the power set). The solution set must not contain duplicate subsets and can be returned in any order.

**Approach:**
- Uses recursive backtracking with depth-first search (DFS)
- For each element, makes two recursive calls: include the element and exclude the element
- Maintains a current subset that gets modified during recursion
- Creates a copy of the subset when reaching the base case (end of array)
- Explores all 2^n possible combinations systematically
- Time complexity: O(2^n × n) where n is the length of the input array
- Space complexity: O(n) for recursion stack depth

**How to run:**
```bash
python subsets.py
```

### Subsets II (LeetCode #90)

File: [subsets_two.py](./subsets_two.py)

**Problem Description:**
Given an integer array `nums` that may contain duplicates, return all possible subsets (the power set). The solution set must not contain duplicate subsets.

**Approach:**
- Uses DFS backtracking with duplicate handling
- Sorts input array to group duplicates together
- For each number, makes two choices: include or exclude
- Skips duplicate numbers to avoid generating duplicate subsets
- Time complexity: O(2^n) where n is the length of the array
- Space complexity: O(n) for recursion stack

**How to run:**
```bash
python subsets_two.py
```

### Combination Sum (LeetCode #39)

File: [combinationSum.py](./combinationSum.py)

**Problem Description:**
Given an array of distinct integers `candidates` and a target integer `target`, return a list of all unique combinations of `candidates` where the chosen numbers sum to `target`. You may choose the same number from `candidates` an unlimited number of times.

**Approach:**
- Uses recursive backtracking with depth-first search (DFS)
- For each candidate, makes two decisions: include it (allowing reuse) or skip to next candidate
- Maintains a current subset and running sum to track progress toward target
- Backtracks by removing elements when exploring alternative paths
- Base cases: return when sum equals target, or when sum exceeds target or all candidates processed
- Time complexity: O(2^t) where t is the target value (worst case when candidates=[1])
- Space complexity: O(target) for recursion depth in worst case

**How to run:**
```bash
python combinationSum.py
```

### Letter Combinations of a Phone Number (LeetCode #17)

File: [phone_combinations.py](./phone_combinations.py)

**Problem Description:**
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. A mapping of digit to letters (just like on the telephone buttons) is given.

**Approach:**
- Uses Depth-First Search (DFS) with backtracking to generate all combinations
- Maps digits 2-9 to their corresponding phone keypad letters
- Recursively builds combinations character by character
- Backtracks by removing the last added character to explore other possibilities
- Handles edge case of empty input by returning an empty list
- Time complexity: O(4^n) where n is the number of digits (worst case when all digits map to 4 letters)
- Space complexity: O(4^n) for storing all possible combinations

**How to run:**
```bash
python phone_combinations.py
```

### Permutations (LeetCode #46)

File: [permute.py](./permute.py)

**Problem Description:**
Given an array `nums` of distinct integers, return all the possible permutations. You can return the answer in any order.

**Approach:**
- Uses recursive backtracking with depth-first search (DFS) to generate all permutations
- Maintains a current permutation being built and a result list of all permutations
- For each position, tries all unused numbers from the input array
- Backtracks by removing the last added number to explore other possibilities
- Base case: when current permutation length equals input array length, add copy to results
- Time complexity: O(n! × n) where n is the length of the input array (n! permutations, each taking O(n) to copy)
- Space complexity: O(n) for recursion stack depth

**How to run:**
```bash
python permute.py
```

### Permutations II (LeetCode #47)

File: [permuteUnique.py](./permuteUnique.py)

**Problem Description:**
Given a collection of numbers `nums` that might contain duplicates, return all possible unique permutations in any order.

**Approach:**
- Uses recursive backtracking with frequency counting to handle duplicates
- Maintains a hashmap to track the frequency of each number
- For each position, tries all available numbers (with remaining count > 0)
- Decrements frequency when using a number, increments when backtracking
- Avoids generating duplicate permutations by using frequency instead of position-based tracking
- Base case: when current permutation length equals input array length, add copy to results
- Time complexity: O(n! × n) where n is the length of the input array
- Space complexity: O(n) for recursion stack depth and frequency map

**How to run:**
```bash
python permuteUnique.py
```

### Network Delay Time (LeetCode #743)

File: [networkDelayTime.py](./networkDelayTime.py)

**Problem Description:**
You are given a network of `n` nodes, labeled from `1` to `n`. You are also given `times`, a list of travel times as directed edges `times[i] = (ui, vi, wi)`, where `ui` is the source node, `vi` is the target node, and `wi` is the time it takes for a signal to travel from source to target. We will send a signal from a given node `k`. Return the time it takes for all the `n` nodes to receive the signal. If it is impossible for all the `n` nodes to receive the signal, return `-1`.

**Approach:**
- Uses Dijkstra's algorithm to find shortest paths from the source node to all other nodes
- Builds an adjacency list representation of the graph with edge weights
- Uses a min-heap to efficiently select the next node with minimum distance
- Tracks visited nodes to avoid processing the same node multiple times
- The maximum shortest path distance becomes the network delay time
- Returns `-1` if not all nodes are reachable from the source
- Time complexity: O((V + E) log V) where V is number of vertices and E is number of edges
- Space complexity: O(V + E) for adjacency list, heap, and visited set

**How to run:**
```bash
python networkDelayTime.py
```

### Path with Maximum Probability (LeetCode #1514)

File: [maxProb.py](./maxProb.py)

**Problem Description:**
You are given an undirected weighted graph of `n` nodes (0-indexed), represented by an edge list where `edges[i] = [a, b]` is an undirected edge connecting the nodes `a` and `b` with a probability of success of traversing that edge `succProb[i]`. Given two nodes `start` and `end`, find the path with the maximum probability of success to go from `start` to `end` and return its success probability.

**Approach:**
- Uses Dijkstra's algorithm with a max heap to find the path with maximum probability
- Implements max heap using negated probabilities in Python's min heap
- Builds an adjacency list with probability-weighted edges for bidirectional graph
- Tracks visited nodes to avoid cycles and redundant processing
- Multiplies probabilities along the path (since probabilities are between 0 and 1)
- Returns 0 if no path exists from start to end node
- Time complexity: O((V + E) log V) where V is number of vertices and E is number of edges
- Space complexity: O(V + E) for adjacency list, heap, and visited set

**How to run:**
```bash
python maxProb.py
```

### Minimum Cost to Connect Points (LeetCode #1584)

File: [minCostConnect.py](./minCostConnect.py)

**Problem Description:**
You are given an array `points` representing integer coordinates of some points on a 2D-plane, where `points[i] = [xi, yi]`. The cost of connecting two points `[xi, yi]` and `[xj, yj]` is the Manhattan distance between them: `|xi - xj| + |yi - yj|`. Return the minimum cost to make all points connected.

**Approach:**
- Uses Prim's algorithm to find the Minimum Spanning Tree (MST)
- Builds an adjacency list with Manhattan distances as edge weights
- Uses a min-heap to efficiently select the next edge with minimum cost
- Tracks visited nodes to avoid cycles in the MST
- Continues until all points are included in the spanning tree
- Manhattan distance formula: |x1 - x2| + |y1 - y2|
- Time complexity: O(n² log n) where n is the number of points
- Space complexity: O(n²) for adjacency list and heap storage

**How to run:**
```bash
python minCostConnect.py
```

### Target Sum (LeetCode #494)

File: [findTargetSumWays.py](./findTargetSumWays.py)

**Problem Description:**
You are given an integer array `nums` and an integer `target`. You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers. Return the number of different expressions that you can build, which evaluates to target.

**Approach:**
- Uses dynamic programming with memoization to avoid redundant calculations
- Implements depth-first search (DFS) to explore all possible combinations of '+' and '-' signs
- For each number, recursively tries both adding and subtracting it from the current sum
- Memoizes results using (index, current_sum) as the key to cache computed values
- Base case: when all numbers are processed, check if current sum equals target
- Time complexity: O(n × S) where n is the length of nums and S is the range of possible sums
- Space complexity: O(n × S) for memoization storage

**How to run:**
```bash
python findTargetSumWays.py
```

# Usage

Each solution can be run individually. The code includes test cases to demonstrate functionality.
