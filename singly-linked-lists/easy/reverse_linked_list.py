import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev


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
    def test_reverseList(self):
        solution = Solution()
        test_cases = [
            ([], []),
            ([1], [1]),
            ([1, 2], [2, 1]),
            ([1, 2, 3], [3, 2, 1]),
            ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
            ([1, 2, 2, 1], [1, 2, 2, 1]),
        ]

        for lst, expected in test_cases:
            with self.subTest(lst=lst, expected=expected):
                head = list_to_linked_list(lst)
                reversed_head = solution.reverseList(head)
                result = linked_list_to_list(reversed_head)
                self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
