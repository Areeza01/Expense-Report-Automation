import os


def allowed_file(filename):

    valid_extensions = (
        ".png",
        ".jpg",
        ".jpeg"
    )

    return filename.lower().endswith(
        valid_extensions
    )