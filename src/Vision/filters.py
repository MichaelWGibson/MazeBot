import numpy as np
import cv2

def pink_filter(image):
    """
    Filters an image for pink pixels

    Args:
        image (Image): The image to filter

    Returns:
        Image: The filtered image
    """
    
    
    image = cv2.GaussianBlur(image,(3,3),0)

    lower = np.uint8([145,40,120])
    upper = np.uint8([175,220,255])

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(hsv, lower, upper)
    
    res = cv2.bitwise_or(image, image, mask=mask)
    return res
