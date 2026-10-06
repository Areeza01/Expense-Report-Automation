import cv2


def clean_image(image):

    return cv2.GaussianBlur(
        image,
        (5, 5),
        0
    )