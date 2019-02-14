# test_utils.py
# Author: Sébastien Combéfis
# Version: February 8, 2018

import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_fact(self):
        self.assertEqual(utils.fact(5),120)
        self.assertEqual(utils.fact(9),362880)
        with self.assertRaise(ValueError):
            utils.fact(-5)
    
    def test_roots(self):
        self.assertEqual(utils.roots(1,5,4), -1, -4)
        with self.assertRaise(ValueError):
            utils.roots(1,4,6)
    
    def test_integrate(self):
        self.assertEqual(utils.integrate("x", 0, 2), 2)
        self.assertEqual(utils.integrate("x", 0, 4), 8)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())
