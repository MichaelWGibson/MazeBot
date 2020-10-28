import math
import numpy as np
import cv2


class BallCollector():
    """ 
        Uses a video feed to drive relentlessly at a pingpong ball
    """

    def __init__(self, drive_train):
        self._drive_train = drive_train

    def pink_filter(self, image):
        """
        Filters an image for pink pixels

        Args:
            image (Image): The image to filter

        Returns:
            Image: The filtered image
        """

        # Blur the the image to reduce noise
        image = cv2.GaussianBlur(image, (3, 3), 0)

        # Define bounds for the color pink in hsv
        lower = np.uint8([145, 40, 120])
        upper = np.uint8([175, 220, 255])

        # Convert input image to hsv
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # Build a mask for only pink pixels
        mask = cv2.inRange(hsv, lower, upper)

        # Apply the mask to the image because it looks cool
        res = cv2.bitwise_or(image, image, mask=mask)

        # Find contours on the mask
        raw_contours, _ = cv2.findContours(
            mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # Filter contours to only thoose lager than 600
        contours = [contour for contour in raw_contours if cv2.contourArea(contour) > 600]

        # Todo move this code out of the pink_filter function
        if len(contours) != 0:
            cv2.drawContours(res, contours, -1, (0, 255, 0), 3)

            c = max(contours, key=cv2.contourArea)
            x, y, w, h = cv2.boundingRect(c)

            print(cv2.contourArea(c))

            # draw the biggest contour's bounding box in red
            cv2.rectangle(res, (x, y), (x+w, y+h), (0, 0, 255), 2)

            image_center = image.shape[1] / 2
            ball_center = x + (w/2)

            offset = image_center - ball_center

            angle = -math.copysign(math.pi/2, offset)

            speed = 0

            if abs(offset) > 200:
                speed = .50

            elif abs(offset) > 300:
                speed = .55

            elif cv2.contourArea(c) < 10000:
                angle = 0
                speed = .35

            self._drive_train.set_heading(speed, angle)
        else:
            self._drive_train.set_heading(0, 0)

        return res
