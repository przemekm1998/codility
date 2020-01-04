import unittest
import split_sum


class TestSplitSum(unittest.TestCase):
    def test_split_sum(self):
        A = [3, 1, 2, 4, 3]
        result = split_sum.split_sum(A)
        self.assertEqual(result, 1)

    def test_split_sum_two_elements(self):
        A = [-1000, 1000]
        result = split_sum.split_sum(A)
        self.assertEqual(result, 2000)

    def test_split_sum_negative_elements(self):
        A = [-2, -3, -4, -1]
        result = split_sum.split_sum(A)
        self.assertEqual(result, 0)

    def test_split_sum_negative_and_positive(self):
        A = [-10, -20, -30, -40, 100]
        result = split_sum.split_sum(A)
        self.assertEqual(result, 20)


if __name__ == '__main__':
    unittest.main()
