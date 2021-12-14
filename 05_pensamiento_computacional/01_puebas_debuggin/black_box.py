import unittest


def add(num_1, num_2):

    return num_1 + num_2


class BlackBoxTest(unittest.TestCase):

    def add_two_positives(self):
        num_1 = 10
        num_2 = 5

        result = add(num_1, num_2)
        self.assertEqual(result, 15)

    def subtract_two_negatives(self):
        num_1 = -10
        num_2 = -7

        result = add(num_1, num_2)
        self.assertEqual(result, -17)


if __name__ == '__main__':
    unittest.main()
