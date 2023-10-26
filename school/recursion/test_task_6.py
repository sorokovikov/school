from contextlib import redirect_stdout
from io import StringIO
from unittest import TestCase

from recursion.task_6 import print_even_index_elements


class TestPrint(TestCase):

    def test_print(self):

        output = StringIO()

        with redirect_stdout(output):
            print_even_index_elements([32, "hello", "world", 1337, 21, "foo", "bar", 322])
        self.assertEqual("32\nworld\n21\nbar\n", output.getvalue())

        output = StringIO()

        with redirect_stdout(output):
            print_even_index_elements([100, "foo", "bar"])
        self.assertEqual("100\nbar\n", output.getvalue())

        output.close()
