from contextlib import redirect_stdout
from io import StringIO
from unittest import TestCase

from recursion.task_5 import print_even_numbers


class TestPrint(TestCase):

    def test_print(self):

        output = StringIO()

        with redirect_stdout(output):
            print_even_numbers([32, 205, 100500, 1337, 21, -40])
        self.assertEqual("32\n100500\n-40\n", output.getvalue())

        output.close()
