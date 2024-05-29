import unittest


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        if not list1 and not list2:
            return None

        temp = ListNode()
        tail = temp

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list2:
            tail.next = list2
        else:
            tail.next = list1

        return temp.next


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
    def test_mergeTwoLists_both_empty(self):
        solution = Solution()
        list1 = list_to_linked_list([])
        list2 = list_to_linked_list([])
        merged_head = solution.mergeTwoLists(list1, list2)
        result = linked_list_to_list(merged_head)
        self.assertEqual(result, [])

    def test_mergeTwoLists_first_empty(self):
        solution = Solution()
        list1 = list_to_linked_list([])
        list2 = list_to_linked_list([1, 2, 3])
        merged_head = solution.mergeTwoLists(list1, list2)
        result = linked_list_to_list(merged_head)
        self.assertEqual(result, [1, 2, 3])

    def test_mergeTwoLists_second_empty(self):
        solution = Solution()
        list1 = list_to_linked_list([1, 2, 3])
        list2 = list_to_linked_list([])
        merged_head = solution.mergeTwoLists(list1, list2)
        result = linked_list_to_list(merged_head)
        self.assertEqual(result, [1, 2, 3])

    def test_mergeTwoLists_both_non_empty(self):
        solution = Solution()
        list1 = list_to_linked_list([1, 3, 5])
        list2 = list_to_linked_list([2, 4, 6])
        merged_head = solution.mergeTwoLists(list1, list2)
        result = linked_list_to_list(merged_head)
        self.assertEqual(result, [1, 2, 3, 4, 5, 6])

    def test_mergeTwoLists_with_duplicates(self):
        solution = Solution()
        list1 = list_to_linked_list([1, 3, 5])
        list2 = list_to_linked_list([1, 2, 5, 6])
        merged_head = solution.mergeTwoLists(list1, list2)
        result = linked_list_to_list(merged_head)
        self.assertEqual(result, [1, 1, 2, 3, 5, 5, 6])


if __name__ == "__main__":
    unittest.main()
