# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Initialize two pointers, both starting at the head
        slow, fast = head, head

        # Move fast pointer twice as fast as the slow pointer
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # If they meet, there is a cycle
            if slow == fast:
                return True

        # If we reach the end of the list, there is no cycle
        return False
