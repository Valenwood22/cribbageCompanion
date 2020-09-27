import unittest
from Main import CribCompanion

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.c = CribCompanion()

    def testCountHand(self):
        self.assertEqual(13, self.c.countHand([(5, '5', 'C'), (9, '9', 'S'), (10, '10', 'D'), (10, 'J', 'D'), (10, 'Q', 'H'), (10, 'K', 'D')]))
        self.assertEqual(26, self.c.countHand([(9, '9', 'D'), (9, '9', 'S'), (10, '10', 'D'), (10, 'J', 'D'), (9, '9', 'C'), (10, 'J', 'C')]))
        self.assertEqual(8, self.c.countHand([(2, '2', 'S'), (9, '9', 'S'), (3, '3', 'D'), (5, '5', 'D'), (10, 'Q', 'H'), (10, 'K', 'D')]))
        self.assertEqual(12, self.c.countHand([(1, 'A', 'S'), (2, '2', 'S'), (3, '3', 'D'), (10, 'J', 'D'), (10, 'Q', 'H'), (10, 'K', 'D')]))
        self.assertEqual(6, self.c.countHand([(1, 'A', 'S'), (9, '9', 'S'), (10, '10', 'S'), (10, 'J', 'D'), (10, 'Q', 'S')], cut=(10, 'K', 'D')))
        self.assertEqual(12+12, self.c.countHand([(1, 'A', 'S'), (1, 'A', 'D'), (1, 'A', 'C'), (1, 'A', 'H'), (3, '3', 'S')], cut=(10, 'K', 'D')))



if __name__ == '__main__':
    unittest.main()
