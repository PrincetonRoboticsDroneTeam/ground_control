import cv2


def simple_stitch():
    image_paths = ["images/test1/image1.png", "images/test1/image2.png"]
    images = []

    for path in image_paths:
        image = cv2.imread(path)
        images.append(image)

    stitcher = cv2.Stitcher.create()
    _, stitched_image = stitcher.stitch(images)

    cv2.imwrite("images/test1/stitched.png", stitched_image)


if __name__ == "__main__":
    simple_stitch()
