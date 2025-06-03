# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.curr = root

    def next(self) -> int:
        # Traverse to the leftmost node
        while self.curr:
            self.stack.append(self.curr)
            self.curr = self.curr.left
        # Process the node and move to right subtree
        self.curr = self.stack.pop()
        res = self.curr.val
        self.curr = self.curr.right
        return res

    def hasNext(self) -> bool:
        # There is a next node if stack or current pointer is not empty
        return bool(self.stack or self.curr)
