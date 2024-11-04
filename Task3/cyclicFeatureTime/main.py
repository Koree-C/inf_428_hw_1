import unittest

def time_difference(time1, time2):
    absolute_difference = abs(time2 - time1)

    if absolute_difference > 12:
        absolute_difference = 24 - absolute_difference

    return absolute_difference


class TestTimeDifference(unittest.TestCase):

    def test_same(self):
        self.assertEqual(time_difference(1, 1), 0)
        self.assertEqual(time_difference(12, 12), 0)

    def test_different(self):
        self.assertEqual(time_difference(1, 2), 1)
        self.assertEqual(time_difference(22, 23), 1)
        self.assertEqual(time_difference(2, 23), 3)
        self.assertEqual(time_difference(12, 3), 9)
        self.assertEqual(time_difference(4, 12), 8)
        self.assertEqual(time_difference(16, 12), 4)
        self.assertEqual(time_difference(2, 24), 2)
        self.assertEqual(time_difference(2, 12), 10)



if __name__ == "__main__":
    time1 = 2
    time2 = 12
    print(f"Time difference between {time1}:00 and {time2}:00 is {time_difference(time1, time2)} hours")

    unittest.main()