from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

# Helper function to create a linked list with a cycle
def create_linked_list_with_cycle(values, pos):
    """
    values: List of node values
    pos: Index at which the last node should point to create a cycle (-1 for no cycle)
    """
    if not values:
        return None
    nodes = [ListNode(val) for val in values]
    for i in range(len(values) - 1):
        nodes[i].next = nodes[i + 1]
    if pos != -1:
        nodes[-1].next = nodes[pos]
    return nodes[0]

# Test the function
if __name__ == "__main__":
    # Example: [3, 2, 0, -4] with cycle at position 1 (0-based index)
    head = create_linked_list_with_cycle([3, 2, 0, -4], 1)

    sol = Solution()
    print("Cycle detected?" , sol.hasCycle(head))  # Output: True
