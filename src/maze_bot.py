import config
from Vision.video_feed import VideoFeed
from Drive.drive_train import DriveTrain
import Stream.stream as stream

try:
    drive_train = DriveTrain(None, None)
    cam = config.get_camera()
    feed = VideoFeed(cam)
    stream.start(feed.get_generator, drive_train)
except KeyboardInterrupt:
    print('Shutting down')
    feed.close()
