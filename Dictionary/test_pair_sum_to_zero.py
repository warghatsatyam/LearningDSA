import unittest

from pair_sum_to_zero import get_pair_sum_to_zero_count

class TestPairSumToZero(unittest.TestCase):
    def test_pair_sum_to_zero(self):
        arr = [1,0,-1,2,-2,3]
        expected_count = 2
        actual_count = get_pair_sum_to_zero_count(arr)
        self.assertEqual(expected_count,actual_count)

    def test_no_pair_sum_to_zero(self):
        arr = [1,2,3,4,5]
        expected_count = 0
        actual_count = get_pair_sum_to_zero_count(arr)
        self.assertEqual(expected_count,actual_count)


if __name__ == '__main__':
    unittest.main()