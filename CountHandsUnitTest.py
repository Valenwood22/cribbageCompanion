import unittest
from Main import CribCompanion

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.c = CribCompanion()

    def testRuns(self):
        self.assertEqual(5, self.c.countHand([(1, 'A', 'S'), (9, '9', 'S'), (10, '10', 'D'), (10, 'J', 'D'), (10, 'Q', 'H'), (10, 'K', 'D')]))
        self.assertEqual(10, self.c.countHand([(9, '9', 'D'), (9, '9', 'S'), (10, '10', 'D'), (10, 'J', 'D'), (10, 'Q', 'H'), (10, 'K', 'D')]))
        self.assertEqual(0, self.c.countHand([(1, 'A', 'S'), (9, '9', 'S'), (3, '3', 'D'), (5, '5', 'D'), (10, 'Q', 'H'), (10, 'K', 'D')]))
        self.assertEqual(6, self.c.countHand([(1, 'A', 'S'), (2, '2', 'S'), (3, '3', 'D'), (10, 'J', 'D'), (10, 'Q', 'H'), (10, 'K', 'D')]))
        self.assertEqual(6, self.c.countHand([(1, 'A', 'S'), (3, '3', 'S'), (4, '4', 'D'), (5, '5', 'D'), (5, '5', 'H'), (10, 'K', 'D')]))
        self.assertEqual(12, self.c.countHand([(1, 'A', 'S'), (10, '10', 'S'), (10, '10', 'D'), (10, 'J', 'D'), (10, 'Q', 'H'), (10, 'Q', 'D')]))

    def testFlush(self):
        self.assertEqual(0, self.c.countHand([(1, 'A', 'S'), (9, '9', 'S'), (10, '10', 'D'), (10, 'J', 'D'), (10, 'Q', 'H'), (10, 'K', 'D')]))
        self.assertEqual(6, self.c.countHand([(1, 'A', 'S'), (9, '9', 'S'), (10, '10', 'S'), (10, 'J', 'S'), (10, 'Q', 'S'), (10, 'K', 'S')]))
        self.assertEqual(5, self.c.countHand([(1, 'A', 'S'), (9, '9', 'S'), (10, '10', 'S'), (10, 'J', 'S'), (10, 'Q', 'S')], cut=(10, 'K', 'D')))
        self.assertEqual(0, self.c.countHand([(1, 'A', 'S'), (9, '9', 'D'), (10, '10', 'S'), (10, 'J', 'S'), (10, 'Q', 'S')], cut=(10, 'K', 'D')))
        self.assertEqual(6, self.c.countHand([(1, 'A', 'S'), (9, '9', 'S'), (10, '10', 'S'), (10, 'J', 'S'), (10, 'Q', 'S')], cut=(10, 'K', 'S')))
        self.assertEqual(0, self.c.countHand([(1, 'A', 'S'), (9, '9', 'S'), (10, '10', 'S'), (10, 'J', 'S'), (10, 'Q', 'S')], cut=(10, 'K', 'D'), isCrib=True))
        self.assertEqual(6, self.c.countHand([(1, 'A', 'S'), (9, '9', 'S'), (10, '10', 'S'), (10, 'J', 'S'), (10, 'Q', 'S')], cut=(10, 'K', 'S'), isCrib=True))

    def testKnobs(self):
        self.assertEqual(0, self.c.countHand([(1, 'A', 'S'), (9, '9', 'S'), (10, '10', 'S'), (10, 'J', 'S'), (10, 'Q', 'S')], cut=(10, 'K', 'D')))
        self.assertEqual(1, self.c.countHand([(1, 'A', 'S'), (9, '9', 'D'), (10, '10', 'S'), (10, 'J', 'S'), (10, 'Q', 'S')], cut=(10, 'K', 'S')))
        self.assertEqual(0, self.c.countHand([(1, 'A', 'S'), (9, '9', 'S'), (10, '10', 'S'), (10, 'J', 'S'), (10, 'Q', 'S')]))


if __name__ == '__main__':
    unittest.main()
