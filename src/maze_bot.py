import config
from Vision.video_feed import VideoFeed
import Stream.stream as stream

try:
    drive_train = config.get_drive()
    cam = config.get_camera()
    feed = VideoFeed(cam)
    stream.start(feed.get_generator, drive_train)
except KeyboardInterrupt:
    print('Shutting down')
    feed.close()
