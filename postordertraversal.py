# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Iterative solution    
from typing import Optional, List
from collections import deque
from TreeNode import TreeNode

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        stack = [(root, False)]  # (node, visited)
        res = []

        while stack:
            curr, visited = stack.pop()
            if visited:
                res.append(curr.val)
            else:
                stack.append((curr, True))  # Mark node as visited
                if curr.right:
                    stack.append((curr.right, False))
                if curr.left:
                    stack.append((curr.left, False))
        
        return res
