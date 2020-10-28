""" Provides a DCMotor class """

import RPi.GPIO as GPIO

class DCMotor():
    """
    A class that represents a direct current motor powered by a L298N driver.
    """

    FREQUENCY = 100

    def __init__(self, pwm_pin, forward_pin, backward_pin):
        """
        Set up motor interface pins

        Args:
            pwm_pin (interger): The microcontroller pin connected to the ena pin on the L298N
            forward_pin (interger): The microcontroller pin for the IN1 or IN3 pin on the L298N
            backward_pin (interger): The microcontroller pin for the IN2 or IN4 pin on the L298N
        """
        self._pwm_pin = pwm_pin
        self._forward_pin = forward_pin
        self._backward_pin = backward_pin

        # Ensure that the proper pin layout is set
        self.set_board_pinout_mode()

        # Set each pin as an output pin
        GPIO.setup(self._pwm_pin, GPIO.OUT)
        GPIO.setup(self._forward_pin, GPIO.OUT)
        GPIO.setup(self._backward_pin, GPIO.OUT)

        # Create a pwm object to represent the speed pin
        self._pwm = GPIO.PWM(self._pwm_pin, self.FREQUENCY)

        # Set speed to 0 and 0 out pins
        self._speed = 0
        self.set_speed(0)

    def set_speed(self, speed):
        """
        Sets the speed of the motor

        Args:
            speed (integer): Target speed between -100 and 100 inclusive
        """
        self._speed = speed

        # Update pins
        self._pwm.start(abs(speed))
        GPIO.output(self._forward_pin, GPIO.HIGH if speed > 0 else GPIO.LOW)
        GPIO.output(self._backward_pin, GPIO.LOW if speed > 0 else GPIO.HIGH)

    def set_board_pinout_mode(self):
        """
        The jetson has 4 pin layouts, we want to use the one that matches the numbers on the board
        See https://github.com/NVIDIA/jetson-gpio
        """
        if GPIO.getmode() != GPIO.BOARD:
            GPIO.setmode(GPIO.BOARD)
