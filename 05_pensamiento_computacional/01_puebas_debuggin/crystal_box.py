import unittest


def adult(age):
    if age >= 18:
        return True
    else:
        return False


class CrystalBoxTest(unittest.TestCase):

    def adult_test(self):
        age = 20

        result = adult(age)

        self.assertTrue(result, True)
    
    def under_age_test(self):
        age = 15

        result = adult(age)

        self.assertTrue(result, False)


if __name__ == '__main__':
    unittest.main()
