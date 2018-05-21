from unittest import TestCase
from square_processing import square_preceding



class TestSquareProcessing(TestCase):

    def test1(self):
        self.assertEqual(square_preceding([1, 2, 3]), [0, 1, 4])

    def test2(self):
        self.assertTrue(square_preceding([0, 1, 4]))


