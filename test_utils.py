# test_utils.py
# Author: Sébastien Combéfis
# Version: February 8, 2018

import unittest
import utils

class TestUtils(unittest.TestCase):
    def test_fact(self):
        # À compléter...
        self.assertEqual(utils.fact(3), 6)
        self.assertEqual(utils.fact(5), 120)
    
    def test_roots(self):
        # À compléter...
        self.assertEqual(utils.roots(1, 1, -2), (1.0, -2.0))
        self.assertEqual(utils.roots(1, 2, 1), (-1.0))
    
    def test_integrate(self):
        # À compléter...
        self.assertEqual(utils.integrate("x + 2", 1, 2), 3.5)
        self.assertEqual(utils.integrate("x ** 2 + x - 2", 0, 3), 7.5)

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestUtils)
    runner = unittest.TextTestRunner()
    exit(not runner.run(suite).wasSuccessful())
