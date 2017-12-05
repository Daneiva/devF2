import unittest

from _DevF.shoting import Position, Velocity


class VelocityTest(unittest.TestCase):
    def test_create_velocity_with_two_positions(self):

        start_position =  Position()
        end_position =  Position(4,3)

        velocity = Velocity(start_position, end_position)

        self.assertIsNotNone(velocity)

    def test_magnitude_is_zero_if_start_and_end_positions_are_the_same(self):
        position = Position(1, 1)
        velocity = Velocity(position, position)

        self.assertEquals(0,velocity.magnitude())

    def test_magnitudeof_velocity_is_given_by_pythagoras_theorem(self):
        print("asdf")

    def test_angel_of_velocity_is_45_if_x_and_y_of_end_position_are_the_same(self):
        start_position=Position()
        end_position = Position(2,2)

        velocity = Velocity(start_position,end_position)
        self.assertEquals(45,velocity.angle())
    def test_angle_of_velocity
    if __name__=="main":
        unittest.main()
