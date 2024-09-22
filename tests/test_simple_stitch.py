import pytest
import cv2
from ground_control.simple_stitch import stitch_images
from ground_control import IMAGES_DIR


@pytest.fixture
def mock_images():
    """Fixture that creates mock images for stitching."""
    img1 = cv2.imread(IMAGES_DIR / "test1/image1.png")
    img2 = cv2.imread(IMAGES_DIR / "test1/image2.png")
    return [img1, img2]


def test_stitch_images_success(mock_images):
    """Test the stitching function with valid images."""
    stitched_image = stitch_images(mock_images)
    assert stitched_image is not None, "Stitched image should not be None"
