import unittest
from pq_module.priority_queue import *


class PriorityQueueTestCase(unittest.TestCase):

    def setUp(self) -> None:
        heap = PriorityQueue()
        heap.append(Node(5))
        heap.append(Node(6))
        heap.append(Node(7))
        heap.append(Node(2))
        heap.append(Node(1))
        heap.append(Node(8))
        heap.append(Node(10))
        heap.append(Node(10))

        self.heap = heap

    def tearDown(self) -> None:
        self.heap.clear()

    def test_init_priority_queue(self):
        h = PriorityQueue()
        self.assertListEqual(h.copy_list(), [])

    def test_get_children(self):
        target = (1, 2)
        results = PriorityQueue.get_children(0)
        self.assertTupleEqual(results, target)

    def test_get_parent(self):
        result1 = PriorityQueue.get_parent(1)
        result2 = PriorityQueue.get_parent(2)
        self.assertEqual(result1, 0)
        self.assertEqual(result2, 0)

    def test_is_empty_on_empty_heap(self):
        h = PriorityQueue()
        self.assertTrue(h.is_empty())

    def test_is_empty_on_not_empty_list(self):
        h = PriorityQueue()
        h.append(Node(5))
        self.assertFalse(h.is_empty())

    def test_empty_heapify(self):
        h = PriorityQueue()
        h.heapify(0)

        self.assertListEqual(h.copy_list(), [])

    def test_heapify(self):
        target = [Node(2), Node(5), Node(3)]

        h = PriorityQueue()
        h.append(target[1])
        h.append(target[0])
        h.append(target[2])
        h.heapify(0)

        self.assertListEqual(h.copy_list(), target)

    def test_max(self):
        self.assertEqual(self.heap.max(), Node(10))

    def test_min(self):
        self.assertEqual(self.heap.min(), Node(1))

    def test_empty_max(self):
        h = PriorityQueue()
        self.assertIsNone(h.max())

    def test_min_empty(self):
        h = PriorityQueue()
        self.assertIsNone(h.min())

    def test_search(self):
        self.assertEqual(self.heap.search(Node(1)), 0)

    def test_search_none(self):
        self.assertIsNone(self.heap.search(Node(200)))

    def test_len(self):
        self.assertEqual(self.heap.len(), 8)

    def test_len_empty_list(self):
        h = PriorityQueue()
        self.assertEqual(h.len(), 0)


if __name__ == '__main__':
    unittest.main()
