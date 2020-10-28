import config
from Vision.camera_feed import CameraFeed
from Vision.filter_feed import FilterFeed
import Stream.stream as stream
from collect_ball import BallCollector

try:
    drive_train = config.get_drive()
    cam = config.get_camera()
    feed = CameraFeed(cam)
    collector = BallCollector(drive_train)
    filtered = FilterFeed(feed, [collector.pink_filter])
    stream.start(filtered.get_generator, drive_train)
except KeyboardInterrupt:
    print('Shutting down')
    feed.close()
