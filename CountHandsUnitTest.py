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
        self.assertEqual(12, self.c.countHand([(3, '3', 'S'), (5, '5', 'S'), (5, '5', 'D'), (10, 'Q', 'S')], cut=(4, '4', 'H')))

        self.assertEqual(2,  self.c.countHand([(3,  '3', 'D'), (9,  '9', 'H'), (10, 'Q',  'H'), (4, '4', 'D')], cut=(4,  '4', 'C')))
        self.assertEqual(16, self.c.countHand([(9,  '9', 'C'), (9,  '9', 'S'), (8,  '8',  'C'), (7, '7', 'H')], cut=(6,  '6', 'D')))
        self.assertEqual(6,  self.c.countHand([(10, 'K', 'C'), (4,  '4', 'D'), (5,  '5',  'C'), (8, '8', 'C')], cut=(5,  '5', 'S')))
        self.assertEqual(0,  self.c.countHand([(10, 'J', 'H'), (10, '10','D'), (7,  '7',  'D'), (6, '6', 'C')], cut=(3,  '3', 'S')))
        self.assertEqual(9,  self.c.countHand([(1,  'A', 'D'), (6,  '6', 'S'), (3,  '3',  'S'), (2, '2', 'S')], cut=(6,  '6', 'H')))
        self.assertEqual(6,  self.c.countHand([(8,  '8', 'H'), (10, 'K', 'H'), (5,  '5',  'D'), (3, '3', 'H')], cut=(5,  '5', 'H')))
        self.assertEqual(2,  self.c.countHand([(3,  '3', 'D'), (10, 'Q', 'H'), (8,  '8',  'H'), (7, '7', 'D')], cut=(10, 'J', 'C')))
        self.assertEqual(2,  self.c.countHand([(8,  '8', 'H'), (6,  '6', 'H'), (10, '10', 'D'), (6, '6', 'D')], cut=(4,  '4', 'H')))



if __name__ == '__main__':
    unittest.main()
