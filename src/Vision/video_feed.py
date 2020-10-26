from threading import Thread
from time import sleep
import cv2


class VideoFeed():
    """
    Represents a video feed by wrapping a camera and updating it a seperate thread. 
    The feed can be consumed by adding a delegate with the add_subscriber method.
    """

    def __init__(self, camera):
        """
        Creates a video feed

        Args:
            camera (camera): Either a PiCam or a WebCam
        """

        # Save camera
        self._camera = camera

        # Create a list of callbacks to notify on new frames
        self._subscribers = []

        # Create a flag used to shutdown the thread
        self._shutdown_flag = False

        # Holds the latest frame
        self._frame = None

        # Start a thread running loop
        loop = Thread(target=self._loop)
        loop.start()

    def _loop(self):
        """
        Main processing loop
        """
        while True:
            self._frame = self._camera.get_frame()

            if self._frame is not None:
                self._notify(self._frame)
            else:
                sleep(.2)

            if self._shutdown_flag:
                break

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

    def close(self):
        """
        Closes the video feed
        """
        self._shutdown_flag = True
