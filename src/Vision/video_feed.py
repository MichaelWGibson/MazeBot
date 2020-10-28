from time import sleep
import cv2


class VideoFeed():
    """
    The feed can be consumed by adding a delegate with the add_subscriber method.
    """

    def __init__(self):
        """
        Creates a video feed
        """

        # Create a list of callbacks to notify on new frames
        self._subscribers = []

        # Holds the latest frame
        self._frame = None


    def _notify(self, image):
        """
        Notify all delegates of a new frame in the video feed.

        Args:
            image (image): The image to broadcast to subscribers
        """
        for subscriber in self._subscribers:
            subscriber(image)

    def get_generator(self):
        """
        Returns a generator that produces a jpg stream for web consumption
        """
        while True:
            if self._frame is not None:
                jpg = cv2.imencode('.jpg', self._frame)[1].tobytes()
                yield b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + jpg + b'\r\n'
            sleep(.2)

    def add_subscriber(self, sub):
        """
        Adds a subscriber to the video feed

        Args:
            sub (function): Delegate to call when a frame is recieved
        """
        self._subscribers.append(sub)

    def remove_subscriber(self, sub):
        """
        Removes a subscriber

        Args:
            sub (function): Delegate to remove
        """
        self._subscribers.remove(sub)
