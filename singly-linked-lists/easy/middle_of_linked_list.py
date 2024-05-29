import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


class TestSolution(unittest.TestCase):
    def list_to_linked_list(self, lst):
        if not lst:
            return None
        head = ListNode(lst[0])
        current = head
        for value in lst[1:]:
            current.next = ListNode(value)
            current = current.next
        return head

    def linked_list_to_list(self, node):
        lst = []
        while node:
            lst.append(node.val)
            node = node.next
        return lst

    def test_middleNode_single_element(self):
        sol = Solution()
        head = self.list_to_linked_list([1])
        result = sol.middleNode(head)
        self.assertEqual(self.linked_list_to_list(result), [1])

    def test_middleNode_two_elements(self):
        sol = Solution()
        head = self.list_to_linked_list([1, 2])
        result = sol.middleNode(head)
        self.assertEqual(self.linked_list_to_list(result), [2])

    def test_middleNode_odd_elements(self):
        sol = Solution()
        head = self.list_to_linked_list([1, 2, 3, 4, 5])
        result = sol.middleNode(head)
        self.assertEqual(self.linked_list_to_list(result), [3, 4, 5])

    def test_middleNode_even_elements(self):
        sol = Solution()
        head = self.list_to_linked_list([1, 2, 3, 4, 5, 6])
        result = sol.middleNode(head)
        self.assertEqual(self.linked_list_to_list(result), [4, 5, 6])

    def test_middleNode_empty_list(self):
        sol = Solution()
        head = self.list_to_linked_list([])
        result = sol.middleNode(head)
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()
