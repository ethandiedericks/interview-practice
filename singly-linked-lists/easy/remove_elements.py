import unittest
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        prev, curr = dummy, head

        while curr:
            nxt = curr.next
            if curr.val == val:
                prev.next = nxt
            else:
                prev = curr
            curr = nxt

        return dummy.next


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
    def test_remove_elements(self):
        solution = Solution()
        head = list_to_linked_list([1, 2, 6, 3, 4, 5, 6])
        val = 6
        result = solution.removeElements(head, val)
        self.assertEqual(linked_list_to_list(result), [1, 2, 3, 4, 5])

    def test_remove_elements_with_single_element(self):
        solution = Solution()
        head = list_to_linked_list([1])
        val = 1
        result = solution.removeElements(head, val)
        self.assertIsNone(result)

    def test_remove_elements_with_no_match(self):
        solution = Solution()
        head = list_to_linked_list([1, 2, 3, 4, 5])
        val = 6
        result = solution.removeElements(head, val)
        self.assertEqual(linked_list_to_list(result), [1, 2, 3, 4, 5])

    def test_remove_elements_with_all_matches(self):
        solution = Solution()
        head = list_to_linked_list([1, 1, 1, 1, 1])
        val = 1
        result = solution.removeElements(head, val)
        self.assertIsNone(result)

    def test_remove_elements_with_empty_list(self):
        solution = Solution()
        head = None
        val = 1
        result = solution.removeElements(head, val)
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
