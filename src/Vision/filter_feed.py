from .video_feed import VideoFeed


class FilterFeed(VideoFeed):
    """
    Represents an image stream that applies filters to an underlying stream
    """

    def __init__(self, base_feed, filters):
        """
        Creates a stream that subscribes to the base feed and provides its frame passed
        through the configured filters

        Args:
            base_feed (VideoFeed): The base image stream
            filters (List{Filter}): A list of filters with wich to process the image
        """

        # Save base feed
        self._base_feed = base_feed

        # Save filters
        self._filters = filters

        # Initialize parent
        super().__init__()

        # Setup processing
        base_feed.add_subscriber(self.process_frame)

    def process_frame(self, image):
        """
        Apply filters to provided image

        Args:
            image (Image): The image to process
        """
        for filt in self._filters:
            image = filt(image)

        self._frame = image

        self._notify(self._frame)
