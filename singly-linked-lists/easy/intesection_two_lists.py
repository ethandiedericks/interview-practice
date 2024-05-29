import unittest


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA, headB):
        track = set()
        while headA:
            track.add(id(headA))
            headA = headA.next
        while headB:
            if id(headB) in track:
                return headB
            headB = headB.next

        return None


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


def find_node_by_value(head, value):
    current = head
    while current:
        if current.val == value:
            return current
        current = current.next
    return None


class TestSolution(unittest.TestCase):
    def test_no_intersection(self):
        solution = Solution()
        listA = list_to_linked_list([1, 2, 3])
        listB = list_to_linked_list([4, 5, 6])
        result = solution.getIntersectionNode(listA, listB)
        self.assertIsNone(result)

    def test_intersection_at_beginning(self):
        solution = Solution()
        intersection = list_to_linked_list([2, 3])
        listA = ListNode(1)
        listA.next = intersection
        listB = ListNode(4)
        listB.next = intersection
        result = solution.getIntersectionNode(listA, listB)
        self.assertEqual(result, intersection)

    def test_intersection_at_middle(self):
        solution = Solution()
        intersection = list_to_linked_list([5, 6])
        listA = list_to_linked_list([1, 2, 3])
        node3 = find_node_by_value(listA, 3)
        node3.next = intersection
        listB = list_to_linked_list([4])
        node4 = find_node_by_value(listB, 4)
        node4.next = intersection
        result = solution.getIntersectionNode(listA, listB)
        self.assertEqual(result, intersection)

    def test_intersection_at_end(self):
        solution = Solution()
        intersection = ListNode(6)
        listA = list_to_linked_list([1, 2, 3, 4, 5])
        node5 = find_node_by_value(listA, 5)
        node5.next = intersection
        listB = list_to_linked_list([9])
        node9 = find_node_by_value(listB, 9)
        node9.next = intersection
        result = solution.getIntersectionNode(listA, listB)
        self.assertEqual(result, intersection)


if __name__ == "__main__":
    unittest.main()
