from Vision.web_cam import WebCamera
from Vision.video_feed import VideoFeed
import Stream.stream as stream

try:
    cam = WebCamera(1)
    feed = VideoFeed(cam)
    stream.start(feed.get_generator)
except KeyboardInterrupt:
    print('Shutting down')
    feed.close()
