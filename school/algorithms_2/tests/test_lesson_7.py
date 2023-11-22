from unittest import TestCase

from algorithms_2.lesson_7 import Heap


class TestLesson7(TestCase):

    def setUp(self):

        self.heap = Heap()
        self.heap.MakeHeap([6, 5, 2, 1, 3, 8, 7, 4, 9, 11], 3)

    def test_make_heap(self):

        self.assertEqual(15, len(self.heap.HeapArray))
        self.assertIsNotNone(self.heap.HeapArray[9])
        self.assertIsNone(self.heap.HeapArray[10])
        self.assertEqual(11, self.heap.HeapArray[0])

    def test_get_max(self):

        self.assertEqual(11, self.heap.GetMax())
        self.assertListEqual([9, 8, 7, 5, 3, 2, 6, 1, 4, None, None, None, None, None, None], self.heap.HeapArray)

        self.assertEqual(9, self.heap.GetMax())
        self.assertListEqual([8, 5, 7, 4, 3, 2, 6, 1, None, None, None, None, None, None, None], self.heap.HeapArray)

        self.assertEqual(8, self.heap.GetMax())
        self.assertListEqual([7, 5, 6, 4, 3, 2, 1, None, None, None, None, None, None, None, None], self.heap.HeapArray)

        self.assertEqual(7, self.heap.GetMax())
        self.assertListEqual([6, 5, 2, 4, 3, 1, None, None, None, None, None, None, None, None, None], self.heap.HeapArray)

        self.assertEqual(6, self.heap.GetMax())
        self.assertListEqual([5, 4, 2, 1, 3, None, None, None, None, None, None, None, None, None, None], self.heap.HeapArray)

        self.assertEqual(5, self.heap.GetMax())
        self.assertListEqual([4, 3, 2, 1, None, None, None, None, None, None, None, None, None, None, None], self.heap.HeapArray)

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
        self.assertListEqual([11, 10, 7, 5, 9, 2, 6, 1, 4, 3, 8, None, None, None, None], self.heap.HeapArray)

        self.assertTrue(self.heap.Add(12))
        self.assertListEqual([12, 10, 11, 5, 9, 7, 6, 1, 4, 3, 8, 2, None, None, None], self.heap.HeapArray)

        self.assertTrue(self.heap.Add(14))
        self.assertListEqual([14, 10, 12, 5, 9, 11, 6, 1, 4, 3, 8, 2, 7, None, None], self.heap.HeapArray)

        self.assertTrue(self.heap.Add(20))
        self.assertListEqual([20, 10, 14, 5, 9, 11, 12, 1, 4, 3, 8, 2, 7, 6, None], self.heap.HeapArray)

        self.assertTrue(self.heap.Add(13))
        self.assertListEqual([20, 10, 14, 5, 9, 11, 13, 1, 4, 3, 8, 2, 7, 6, 12], self.heap.HeapArray)

        self.assertFalse(self.heap.Add(100500))

        self.assertEqual(20, self.heap.GetMax())
        self.assertListEqual([14, 10, 13, 5, 9, 11, 12, 1, 4, 3, 8, 2, 7, 6, None], self.heap.HeapArray)
