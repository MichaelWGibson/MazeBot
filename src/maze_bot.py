import config
from Vision.camera_feed import CameraFeed
from Vision.filter_feed import FilterFeed
import Vision.filters as filters
import Stream.stream as stream

try:
    drive_train = config.get_drive()
    cam = config.get_camera()
    feed = CameraFeed(cam)
    filtered = FilterFeed(feed, [filters.pink_filter])
    stream.start(filtered.get_generator, drive_train)
except KeyboardInterrupt:
    print('Shutting down')
    feed.close()
