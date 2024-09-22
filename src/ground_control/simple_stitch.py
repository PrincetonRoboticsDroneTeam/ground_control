import cv2


def read_images(image_paths):
    """Reads a list of images from the given file paths."""
    images = []
    for path in image_paths:
        image = cv2.imread(path)
        if image is None:
            raise ValueError(f"Could not read image from {path}")
        images.append(image)
    return images


def stitch_images(images):
    """Stitches a list of images together and returns the stitched image."""
    stitcher = cv2.Stitcher.create()
    status, stitched_image = stitcher.stitch(images)
    if status != cv2.Stitcher_OK:
        raise RuntimeError("Error in stitching images")
    return stitched_image


def save_image(output_path, image):
    """Saves the stitched image to the given file path."""
    cv2.imwrite(output_path, image)


def simple_stitch(image_paths, output_path):
    """Main function to read, stitch, and save images."""
    images = read_images(image_paths)
    stitched_image = stitch_images(images)
    save_image(output_path, stitched_image)


if __name__ == "__main__":
    image_paths = ["images/test1/image1.png", "images/test1/image2.png"]
    output_path = "images/test1/stitched.png"
    simple_stitch(image_paths, output_path)

