import unittest
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


def create_cycle_linked_list(lst, pos):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    cycle_node = None
    for i, value in enumerate(lst[1:]):
        current.next = ListNode(value)
        current = current.next
        if i == pos - 1:
            cycle_node = current
    if cycle_node:
        current.next = cycle_node
    return head


class TestSolution(unittest.TestCase):
    def test_no_cycle(self):
        solution = Solution()
        head = create_cycle_linked_list([1, 2, 3, 4, 5], pos=-1)
        self.assertFalse(solution.hasCycle(head))

    def test_cycle_in_middle(self):
        solution = Solution()
        head = create_cycle_linked_list([1, 2, 3, 4, 5], pos=2)
        self.assertTrue(solution.hasCycle(head))

    def test_cycle_at_end(self):
        solution = Solution()
        head = create_cycle_linked_list([1, 2, 3, 4, 5], pos=4)
        self.assertTrue(solution.hasCycle(head))

    def test_single_node_no_cycle(self):
        solution = Solution()
        head = create_cycle_linked_list([1], pos=-1)
        self.assertFalse(solution.hasCycle(head))

    def test_empty_list(self):
        solution = Solution()
        head = create_cycle_linked_list([], pos=-1)
        self.assertFalse(solution.hasCycle(head))


if __name__ == "__main__":
    unittest.main()
