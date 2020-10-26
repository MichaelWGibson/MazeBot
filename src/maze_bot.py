from Vision.pi_cam import PiCamera
from Vision.video_feed import VideoFeed
import Stream.stream as stream

try:
    cam = PiCamera()
    feed = VideoFeed(cam)
    stream.start(feed.get_generator)
except KeyboardInterrupt:
    print('Shutting down')
    feed.close()
    