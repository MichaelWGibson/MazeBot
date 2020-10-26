from Vision.web_cam import WebCamera
from Vision.pi_cam import PiCamera

config = {
    "camera" : {
        "type" : "web", # [web, pi]
        "port" : 1 # Typically [0, 1], only relevant if type == web
    }
}

def get_camera():
    """ Provides the camera as defined in the config object """

    if config["camera"]["type"] == "web":
        return WebCamera(config["camera"]["port"])

    if config["camera"]["type"] == "pi":
        return PiCamera()

    raise ValueError("config.camera.type was not a valid option")
