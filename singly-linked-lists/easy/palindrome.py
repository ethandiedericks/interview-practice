import unittest
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head

        # find middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse 2nd half
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        # check palindrome
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True


def list_to_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for value in lst[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


class TestSolution(unittest.TestCase):
    def test_empty_list(self):
        solution = Solution()
        head = list_to_linked_list([])
        self.assertTrue(solution.isPalindrome(head))

    def test_single_element_list(self):
        solution = Solution()
        head = list_to_linked_list([1])
        self.assertTrue(solution.isPalindrome(head))

    def test_two_element_palindrome(self):
        solution = Solution()
        head = list_to_linked_list([1, 1])
        self.assertTrue(solution.isPalindrome(head))

    def test_two_element_non_palindrome(self):
        solution = Solution()
        head = list_to_linked_list([1, 2])
        self.assertFalse(solution.isPalindrome(head))

    def test_palindrome_list(self):
        solution = Solution()
        head = list_to_linked_list([1, 2, 3, 2, 1])
        self.assertTrue(solution.isPalindrome(head))

    def test_non_palindrome_list(self):
        solution = Solution()
        head = list_to_linked_list([1, 2, 3, 4, 5])
        self.assertFalse(solution.isPalindrome(head))

    def test_palindrome_list_with_even_elements(self):
        solution = Solution()
        head = list_to_linked_list([1, 2, 2, 1])
        self.assertTrue(solution.isPalindrome(head))


if __name__ == "__main__":
    unittest.main()
