from threading import Thread
from time import sleep
from .video_feed import VideoFeed


class CameraFeed(VideoFeed):
    """
    Represents a video feed by wrapping a camera and updating it a seperate thread. 
    The feed can be consumed by adding a delegate with the add_subscriber method.
    """

    def __init__(self, camera):
        """
        Creates a video feed that wraps the provided camera

        Args:
            camera (camera): Either a PiCam or a WebCam
        """

        # Save camera
        self._camera = camera

        # Create a flag used to shutdown the thread
        self._shutdown_flag = False

        # Construct parent object
        super().__init__()

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
                sleep(.02)

            if self._shutdown_flag:
                break

    def close(self):
        """
        Closes the video feed
        """
        self._shutdown_flag = True
