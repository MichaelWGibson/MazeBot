import cv2

class WebCamera():
    """
    Represents a USB web cam
    """
    def __init__(self, port_num = 0):
        """
        Create a video capture object with the first usb camera available

        Args:
            port_num (int, optional): The port number of the web cam. Defaults to 0."""

        self._capture = cv2.VideoCapture(port_num)

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
        