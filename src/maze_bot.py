import config
from Vision.video_feed import VideoFeed
import Stream.stream as stream

try:
    cam = config.get_camera()
    feed = VideoFeed(cam)
    stream.start(feed.get_generator)
except KeyboardInterrupt:
    print('Shutting down')
    feed.close()
