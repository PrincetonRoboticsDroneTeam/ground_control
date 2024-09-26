import cv2


def read_images(image_paths):
    """Reads a list of images from the given file paths."""
    images = []
    for path in image_paths:
        image = cv2.imread(path)
        if image is None:
            error_message = f"Could not read image from {path}"
            raise ValueError(error_message)
        images.append(image)
    return images


def stitch_images(images):
    """Stitches a list of images together and returns the stitched image."""
    stitcher = cv2.Stitcher.create()
    status, stitched_image = stitcher.stitch(images)
    if status != cv2.Stitcher_OK:
        error_message = "Error in stitching images"
        raise RuntimeError(error_message)
    return stitched_image


def save_image(output_path, image):
    """Saves the stitched image to the given file path."""
    cv2.imwrite(output_path, image)


def simple_stitch(image_paths, output_path):
    """Main function to read, stitch, and save images."""
    images = read_images(image_paths)
    stitched_image = stitch_images(images)
    save_image(output_path, stitched_image)
