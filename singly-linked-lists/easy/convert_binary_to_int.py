"""
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

The most significant bit is at the head of the linked list.
"""


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


test_cases = [("101", 5), ("111", 7), ("0", 0), ("1", 1), ("1101", 13)]

solution = Solution()
for binary_str, expected in test_cases:
    head = create_linked_list(binary_str)
    result = solution.getDecimalValue(head)
    print(f"Binary: {binary_str} -> Decimal: {result}, Expected: {expected}")
    assert result == expected, f"Test failed for binary: {binary_str}"
