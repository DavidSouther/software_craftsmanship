import unittest
import unittest.mock
import rugs


class SquareRugTest(unittest.TestCase):
    def test_square_rug_no_fringe(self):
        rug = rugs.SquareRug(5, False)

        area = rug.area()
        perimeter = rug.perimeter()
        cost = rug.cost()

        self.assertEqual(area, 25)
        self.assertEqual(perimeter, 20)
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
    
    @unittest.mock.patch("builtins.input")
    def test_square_rug_get_value(self, mock_input):
        rug = rugs.SquareRug(5, False)
        mock_input.side_effect = [ "y", "5" ]
        rug.get_values()
        self.assertEqual(rug.side_length, 5)
        self.assertEqual(rug.has_fringe, True)

    @unittest.mock.patch("builtins.print")
    def test_square_rug_print_rug(self, mock_print):
        rug = rugs.SquareRug(5, False)
        rug.print()
        mock_print.assert_called_with(
            "This square rug costs $125.00 without fringe.")

if __name__ == "__main__":
    unittest.main()
