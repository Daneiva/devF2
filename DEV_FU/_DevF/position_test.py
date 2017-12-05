import unittest
#import prime
from shoting import Position

class PrimeTest(unittest.TestCase):
        def test_position_can_be_created_with_no_params(self):
                position = Position()
                self.assertTrue(position!= None)

        def test_position_with_no_params_corresponds_to_origin(self):
                position = Position(1,1)

                self.assertEqual(0,position.x())
                self.assertEqual(0,position.y())

        def test_position_can_be_created_with_x_and_y_params(self):
                position = Position(2,2)
                self.assertEqual(2, position.x())
                self.assertEqual(3, position.y())

        def test_distance_to_same_position_is_zero(self):
                position = Position(2,3)
                self.assertEqual(0, position.distance_to(position))

        def test_distance_is_greater_than_zero_if_positions_are_diff(self):
                first_pos = Position()
                second_po = Position(1,1)
                self.assertTrue(first_pos.distance_to(second_po)>0)


if __name__ == "__main__":
        unittest.main()