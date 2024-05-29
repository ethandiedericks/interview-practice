import unittest
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next  # Skip the duplicate node
            else:
                current = current.next  # Move to the next node
        return head


def list_to_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


def linked_list_to_list(node):
    lst = []
    while node:
        lst.append(node.val)
        node = node.next
    return lst


class TestSolution(unittest.TestCase):
    def test_empty_list(self):
        solution = Solution()
        head = list_to_linked_list([])
        result = solution.deleteDuplicates(head)
        self.assertEqual(linked_list_to_list(result), [])

    def test_single_element_list(self):
        solution = Solution()
        head = list_to_linked_list([1])
        result = solution.deleteDuplicates(head)
        self.assertEqual(linked_list_to_list(result), [1])

    def test_no_duplicates(self):
        solution = Solution()
        head = list_to_linked_list([1, 2, 3])
        result = solution.deleteDuplicates(head)
        self.assertEqual(linked_list_to_list(result), [1, 2, 3])

    def test_duplicates_at_beginning(self):
        solution = Solution()
        head = list_to_linked_list([1, 1, 2, 3])
        result = solution.deleteDuplicates(head)
        self.assertEqual(linked_list_to_list(result), [1, 2, 3])

    def test_duplicates_in_middle(self):
        solution = Solution()
        head = list_to_linked_list([1, 2, 2, 3])
        result = solution.deleteDuplicates(head)
        self.assertEqual(linked_list_to_list(result), [1, 2, 3])

    def test_duplicates_at_end(self):
        solution = Solution()
        head = list_to_linked_list([1, 2, 3, 3])
        result = solution.deleteDuplicates(head)
        self.assertEqual(linked_list_to_list(result), [1, 2, 3])

    def test_all_duplicates(self):
        solution = Solution()
        head = list_to_linked_list([1, 1, 1, 1])
        result = solution.deleteDuplicates(head)
        self.assertEqual(linked_list_to_list(result), [1])


if __name__ == "__main__":
    unittest.main()
