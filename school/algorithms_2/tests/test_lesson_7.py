from unittest import TestCase

from algorithms_2.lesson_7 import Heap


class TestLesson7(TestCase):

    def setUp(self):

        self.heap = Heap()
        self.heap.MakeHeap([11, 9, 4, 7, 8, 3, 1, 2, 5, 6], 3)

    def test_make_heap(self):

        self.assertEqual(15, len(self.heap.HeapArray))
        self.assertIsNotNone(self.heap.HeapArray[9])
        self.assertIsNone(self.heap.HeapArray[10])

    def test_get_max(self):

        self.assertEqual(11, self.heap.GetMax())
        self.assertListEqual([9, 8, 4, 6, 7, 3, 1, 2, 5, None, None, None, None, None, None], self.heap.HeapArray)

        self.assertEqual(9, self.heap.GetMax())
        self.assertListEqual([8, 7, 4, 5, 6, 3, 1, 2, None, None, None, None, None, None, None], self.heap.HeapArray)

        self.assertEqual(8, self.heap.GetMax())
        self.assertListEqual([7, 6, 4, 2, 5, 3, 1, None, None, None, None, None, None, None, None], self.heap.HeapArray)

        self.assertEqual(7, self.heap.GetMax())
        self.assertListEqual([6, 5, 4, 1, 2, 3, None, None, None, None, None, None, None, None, None], self.heap.HeapArray)

        self.assertEqual(6, self.heap.GetMax())
        self.assertListEqual([5, 3, 4, 1, 2, None, None, None, None, None, None, None, None, None, None], self.heap.HeapArray)

        self.assertEqual(5, self.heap.GetMax())
        self.assertListEqual([4, 2, 3, 1, None, None, None, None, None, None, None, None, None, None, None], self.heap.HeapArray)

        self.assertEqual(4, self.heap.GetMax())
        self.assertListEqual([3, 1, 2, None, None, None, None, None, None, None, None, None, None, None, None], self.heap.HeapArray)

        self.assertEqual(3, self.heap.GetMax())
        self.assertListEqual([2, 1, None, None, None, None, None, None, None, None, None, None, None, None, None], self.heap.HeapArray)

        self.assertEqual(2, self.heap.GetMax())
        self.assertListEqual([1, None, None, None, None, None, None, None, None, None, None, None, None, None, None], self.heap.HeapArray)

        self.assertEqual(1, self.heap.GetMax())
        self.assertListEqual([None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], self.heap.HeapArray)

        self.assertEqual(-1, self.heap.GetMax())

    def test_add(self):

        self.assertTrue(self.heap.Add(10))
        self.assertListEqual([11, 10, 4, 7, 9, 3, 1, 2, 5, 6, 8, None, None, None, None], self.heap.HeapArray)

        self.assertTrue(self.heap.Add(12))
        self.assertListEqual([12, 10, 11, 7, 9, 4, 1, 2, 5, 6, 8, 3, None, None, None], self.heap.HeapArray)

        self.assertTrue(self.heap.Add(14))
        self.assertListEqual([14, 10, 12, 7, 9, 11, 1, 2, 5, 6, 8, 3, 4, None, None], self.heap.HeapArray)

        self.assertTrue(self.heap.Add(20))
        self.assertListEqual([20, 10, 14, 7, 9, 11, 12, 2, 5, 6, 8, 3, 4, 1, None], self.heap.HeapArray)

        self.assertTrue(self.heap.Add(100))
        self.assertListEqual([100, 10, 20, 7, 9, 11, 14, 2, 5, 6, 8, 3, 4, 1, 12], self.heap.HeapArray)

        self.assertFalse(self.heap.Add(100500))





