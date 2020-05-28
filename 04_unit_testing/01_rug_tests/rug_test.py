import unittest
import rugs


class SquareRugTest(unittest.TestCase):
    def test_square_rug_no_fringe(self):
        rug = rugs.SquareRug(5, False)

        area = rug.area()
        perimeter = rug.perimeter()
        cost = rug.cost()

        self.assertEqual(area, 25)
        self.assertEqual(perimeter, 25)
        self.assertEqual(cost, 125)

    def test_square_rug_fringe(self):
        rug = rugs.SquareRug(5, False)

        area = rug.area()
        perimeter = rug.perimeter()
        cost = rug.cost()

        self.assertEqual(area, 25)
        self.assertEqual(perimeter, 20)
        self.assertEqual(cost, 125)
    
    def test_square_rug_no_size(self):
        rug = rugs.SquareRug(0, False)

        area = rug.area()
        perimeter = rug.perimeter()
        cost = rug.cost()

        self.assertEqual(area, 0)
        self.assertEqual(perimeter, 0)
        self.assertEqual(cost, 0)

if __name__ == "__main__":
    unittest.main()
