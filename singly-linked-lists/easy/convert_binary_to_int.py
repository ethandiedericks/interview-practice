import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        curr = temp = head
        num = -1
        sum_int = 0

        while curr:
            num += 1
            curr = curr.next

        while temp:
            sum_int += temp.val * (2**num)
            num -= 1
            temp = temp.next

        return sum_int


def create_linked_list(binary_str):
    head = ListNode(int(binary_str[0]))
    current = head
    for char in binary_str[1:]:
        current.next = ListNode(int(char))
        current = current.next
    return head


class TestSolution(unittest.TestCase):
    def test_getDecimalValue(self):
        solution = Solution()
        test_cases = [
            ("101", 5),
            ("111", 7),
            ("0", 0),
            ("1", 1),
            ("1101", 13),
            ("10010", 18),
            ("0000", 0),
            ("001", 1),
            ("01010", 10),
            ("11111", 31),
        ]

        for binary_str, expected in test_cases:
            with self.subTest(binary_str=binary_str, expected=expected):
                head = create_linked_list(binary_str)
                result = solution.getDecimalValue(head)
                self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
