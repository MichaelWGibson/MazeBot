import cv2

class PiCamera():
    """
    Represents a rasberry pi v2 camera module
    """
    def __init__(self,     
        capture_width=1280,
        capture_height=720,
        display_width=1280,
        display_height=720,
        framerate=15,
        flip_method=0
    ):
        """
        Initalizes a camera module with g-streamer

        Args:
            capture_width (int, optional): Capture width. Defaults to 1280.
            capture_height (int, optional): Caputre Height. Defaults to 720.
            display_width (int, optional): Display width. Defaults to 1280.
            display_height (int, optional): Display height. Defaults to 720.
            framerate (int, optional): Frame rate. Defaults to 15.
            flip_method (int, optional): Flip method. Defaults to 0.
        """
        gstream = (
            "nvarguscamerasrc ! "
            "video/x-raw(memory:NVMM), "
            "width=(int)%d, height=(int)%d, "
            "format=(string)NV12, framerate=(fraction)%d/1 ! "
            "nvvidconv flip-method=%d ! "
            "video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGRx ! "
            "videoconvert ! "
            "video/x-raw, format=(string)BGR ! appsink"
            % (
                capture_width,
                capture_height,
                framerate,
                flip_method,
                display_width,
                display_height,
            )
        )

        self._capture = cv2.VideoCapture(gstream, cv2.CAP_GSTREAMER)

    def is_open(self):
        """
        Checks if a connection to the camera is open

        Returns:
            [bool]: A bool representing the camera's open state
        """
        return self._capture.isOpened()

    def get_frame(self):
        """
        Reads a frame from the camera
        """
        ret, img = self._capture.read()

        if ret is True:
            return img

        return None
        