from unittest import TestCase

from atd_1.lesson_3_two_way_list import TwoWayList


class TestLesson2(TestCase):

    def setUp(self):

        self.ll = TwoWayList()
        self.ll_filled = TwoWayList()

        self.ll_filled.add_to_empty(1)
        for i in range(2, 6):
            self.ll_filled.add_tail(i)
        self.ll_filled.right()
        self.ll_filled.right()

    def test_add_to_empty(self):

        self.ll.add_to_empty(10)

        self.assertEqual(10, self.ll.get())
        self.assertEqual(TwoWayList.ADD_TO_EMPTY_OK, self.ll.get_add_to_empty_status())

        self.ll.add_to_empty(50)
        self.assertEqual(TwoWayList.ADD_TO_EMPTY_ERR, self.ll.get_add_to_empty_status())

    def test_get(self):

        self.ll.get()
        self.assertEqual(TwoWayList.GET_ERR, self.ll.get_get_status())

        self.ll.add_to_empty(10)

        self.assertEqual(10, self.ll.get())
        self.assertEqual(TwoWayList.GET_OK, self.ll.get_get_status())

    def test_is_head(self):

        self.ll.is_head()
        self.assertEqual(TwoWayList.IS_HEAD_ERR, self.ll.get_is_head_status())

        self.ll.add_to_empty(10)

        self.assertTrue(self.ll.is_head())
        self.assertEqual(TwoWayList.IS_HEAD_OK, self.ll.get_is_head_status())

    def test_is_tail(self):

        self.ll.is_tail()
        self.assertEqual(TwoWayList.IS_TAIL_ERR, self.ll.get_is_tail_status())

        self.ll.add_to_empty(10)

        self.assertTrue(self.ll.is_tail())
        self.assertEqual(TwoWayList.IS_HEAD_OK, self.ll.get_is_tail_status())

    def test_remove(self):

        self.ll.remove()
        self.assertEqual(TwoWayList.REMOVE_ERR, self.ll.get_remove_status())

        self.ll.add_to_empty(10)
        self.ll.remove()
        self.assertEqual(TwoWayList.REMOVE_OK, self.ll.get_remove_status())
        self.assertFalse(self.ll.is_value())

    def test_is_value(self):

        self.assertFalse(self.ll.is_value())

        self.ll.add_to_empty(10)
        self.assertTrue(self.ll.is_value())

    def test_head(self):

        self.ll.head()
        self.assertEqual(TwoWayList.HEAD_ERR, self.ll.get_head_status())

        self.ll.add_to_empty(1)
        for i in range (2, 10):
            self.ll.add_tail(i)
            self.ll.right()

        self.assertEqual(9, self.ll.get())

        self.ll.head()
        self.assertEqual(1, self.ll.get())
        self.assertEqual(TwoWayList.HEAD_OK, self.ll.get_head_status())

    def test_tail(self):

        self.ll.tail()
        self.assertEqual(TwoWayList.TAIL_ERR, self.ll.get_tail_status())

        self.ll.add_to_empty(1)
        for i in range (2, 10):
            self.ll.add_tail(i)

        self.assertEqual(1, self.ll.get())

        self.ll.tail()
        self.assertEqual(9, self.ll.get())
        self.assertEqual(TwoWayList.TAIL_OK, self.ll.get_tail_status())

    def test_right(self):

        self.ll.right()
        self.assertEqual(TwoWayList.RIGHT_ERR, self.ll.get_right_status())

        self.ll.add_to_empty(1)

        with self.subTest():
            for i in range(2, 10):
                self.ll.add_tail(i)
                self.ll.right()
                self.assertEqual(i, self.ll.get())
                self.assertEqual(TwoWayList.RIGHT_OK, self.ll.get_right_status())

        self.ll.right()
        self.assertEqual(TwoWayList.RIGHT_ERR, self.ll.get_right_status())

    def test_left(self):

        self.ll.left()
        self.assertEqual(TwoWayList.LEFT_ERR, self.ll.get_left_status())

        self.ll.add_to_empty(1)

        for i in range(2, 10):
            self.ll.add_tail(i)

        self.ll.tail()
        with self.subTest():
            for i in range (9, 1):
                self.ll.left()
                self.assertEqual(i, self.ll.get())
                self.assertEqual(TwoWayList.LEFT_OK, self.ll.get_left_status())

        self.ll.right()
        self.assertEqual(TwoWayList.RIGHT_ERR, self.ll.get_right_status())

    def test_put_right(self):

        self.ll.put_right(100)
        self.assertEqual(TwoWayList.PUT_RIGHT_ERR, self.ll.get_put_right_status())

        self.ll_filled.put_right(100)
        self.assertEqual(TwoWayList.PUT_RIGHT_OK, self.ll_filled.get_put_right_status())
        self.ll_filled.right()
        self.assertEqual(100, self.ll_filled.get())

        self.ll_filled.tail()

        self.ll_filled.put_right(200)
        self.assertEqual(TwoWayList.PUT_RIGHT_OK, self.ll_filled.get_put_right_status())
        self.assertFalse(self.ll_filled.is_tail())

        self.ll_filled.right()
        self.assertEqual(TwoWayList.RIGHT_OK, self.ll_filled.get_right_status())
        self.assertEqual(200, self.ll_filled.get())
        self.assertTrue(self.ll_filled.is_tail())

    def test_put_left(self):

        self.ll_filled.head()
        self.ll_filled.put_left(500)
        self.assertEqual(TwoWayList.PUT_LEFT_OK, self.ll_filled.get_put_left_status())

        self.assertNotEqual(500, self.ll_filled.get())
        self.assertFalse(self.ll_filled.is_head())

        self.ll_filled.head()
        self.assertEqual(500, self.ll_filled.get())
        self.assertTrue(self.ll_filled.is_head())

    def test_add_tail(self):

        self.ll.add_to_empty(1)

        with self.subTest():
            for i in range(2, 10):
                self.ll.add_tail(i)
                self.assertEqual(TwoWayList.ADD_TAIL_OK, self.ll.get_add_tail_status())
                self.assertFalse(self.ll.is_tail())
                self.ll.right()
                self.assertTrue(self.ll.is_tail())

    def test_replace(self):

        self.ll.replace(100)
        self.assertEqual(TwoWayList.REPLACE_ERR, self.ll.get_replace_status())

        self.ll.add_to_empty(10)

        self.assertEqual(10, self.ll.get())

        self.ll.replace(2)
        self.assertEqual(TwoWayList.REPLACE_OK, self.ll.get_replace_status())
        self.assertEqual(2, self.ll.get())

    def test_find(self):

        self.ll_filled.find(300)
        self.assertEqual(TwoWayList.FIND_ERR, self.ll_filled.get_find_status())

        self.ll_filled.find(5)
        self.assertEqual(TwoWayList.FIND_OK, self.ll_filled.get_find_status())
        self.assertEqual(5, self.ll_filled.get())

        self.ll_filled.find(5)
        self.assertEqual(TwoWayList.FIND_ERR, self.ll_filled.get_find_status())

    def test_remove_all(self):

        self.ll.add_to_empty(1)

        for _ in range(10):
            self.ll.add_tail(1)

        self.assertEqual(11, self.ll.size())
        self.ll.remove_all(1)
        self.assertFalse(self.ll.is_value())
        self.assertEqual(0, self.ll.size())

        self.ll.add_to_empty(1)
        for _ in range(10):
            self.ll.add_tail(1)
        self.ll.add_tail(2)
        self.ll.tail()

        self.assertEqual(12, self.ll.size())
        self.assertEqual(2, self.ll.get())

        self.ll.remove_all(2)
        self.assertEqual(11, self.ll.size())
        self.assertEqual(1, self.ll.get())
