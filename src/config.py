from Vision.web_cam import WebCamera
from Vision.pi_cam import PiCamera
from Drive.mock_motor import MockMotor
from Drive.drive_train import DriveTrain

config = {
    "camera": {
        "type": "pi",  # [web, pi]
        "port": 1  # Typically [0, 1], only relevant if type == web
    },
    "drive": {
        "type": "pwm",  # [pwm, mock]
        "log": False,
        "left": {
            "pwm_pin": 33,
            "forward_pin": 12,
            "reverse_pin": 11
        },
        "right": {
            "pwm_pin": 32,
            "forward_pin": 16,
            "reverse_pin": 15
        },
    }
}


def get_camera():
    """ Provides the camera as defined in the config object """

    if config["camera"]["type"] == "web":
        return WebCamera(config["camera"]["port"])

    if config["camera"]["type"] == "pi":
        return PiCamera()

    raise ValueError("config.camera.type was not a valid option")


def get_drive():
    """ Provides a drive train as defined in the config object """

    if config["drive"]["type"] == "pwm":

        # This import fails if we aren't on a jetson/pi so only include when configured
        from Drive.dc_motor import DCMotor

        # Left motor pinout
        left_config = config["drive"]["left"]
        left_motor = DCMotor(
            left_config["pwm_pin"], left_config["forward_pin"], left_config["reverse_pin"])

        # Right motor pinout
        right_config = config["drive"]["right"]
        right_motor = DCMotor(
            right_config["pwm_pin"], right_config["forward_pin"], right_config["reverse_pin"])

        return DriveTrain(left_motor, right_motor, config["drive"]["log"])

    if config["drive"]["type"] == "mock":
        return DriveTrain(MockMotor(), MockMotor(), config["drive"]["log"])

    raise ValueError("config.drive.type was not a valid option")
