# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        # Edge case: empty list or single node with no cycle
        if not head or not head.next:
            return None

        # Phase 1: Detect if a cycle exists using Floyd's Tortoise & Hare algorithm
        while fast and fast.next:
            slow = slow.next          # move slow by 1
            fast = fast.next.next     # move fast by 2

            if fast == slow:          # cycle detected
                # Phase 2: Find the entry point of the cycle
                slow = head           # reset slow to head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow           # start of the cycle

        return None                   # no cycle found
