import math

class DriveTrain():
    """ Represents a drive train, responsible for controlling motors """
    def __init__(self, left_motor, right_motor, log_flag):
        self.left_motor = left_motor
        self.right_motor = right_motor
        self.log_flag = log_flag

    def set_heading(self, speed, angle):
        """
        Drive in a certain direction at a certain speed

        Args:
            speed (int): The speed to drive at from 0 - 1 inclusive
            angle (int): Direction to go 0 being straight, -π/2 => left, π/2 => right
        """

        # Check inputs
        assert 0 <= speed <= 1, "Argument 'speed' is out of range"
        assert -math.pi <= angle <= math.pi, "Argument 'angle' is out of range"

        # Use trig to break down the triangle
        forward_component = math.cos(angle)
        side_component = math.sin(angle)

        # Put it back together in terms of motor speed
        # If the side component is right, spin left wheel faster
        left_speed = forward_component + side_component
        right_speed = forward_component - side_component

        # Check for overflows
        left_speed = min(1, left_speed)
        right_speed = min(1, right_speed)

        left_speed = max(-1, left_speed)
        right_speed = max(-1, right_speed)

        # Print results
        if self.log_flag:
            print("Motor speeds, Left: {:.2f} Right: {:.2f}".format(left_speed, right_speed))

        # Drive
        self.left_motor.set_speed(left_speed)
        self.right_motor.set_speed(right_speed)
        