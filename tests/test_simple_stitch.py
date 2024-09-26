import os
from pathlib import Path

import cv2
import pytest

from ground_control.simple_stitch import stitch_images

DATA_DIR = Path(os.environ["DATA_DIR"])
UAV_VISLOC_DATASET_DIR = DATA_DIR / "uav_visloc_dataset"


@pytest.fixture
def mock_images():
    """Fixture that creates mock images for stitching."""
    image_dir = Path(UAV_VISLOC_DATASET_DIR / "01" / "drone")
    image_paths = [image_dir / Path(name) for name in os.listdir(image_dir)]
    image_paths = image_paths[:3]

    return [cv2.imread(path) for path in image_paths]


def test_stitch_images_success(mock_images, tmp_path):
    """Test the stitching function with valid images."""
    stitched_image = stitch_images(mock_images)
    assert stitched_image is not None, "Stitched image should not be None"

    output_path = tmp_path / "stitched_image.jpg"
    cv2.imwrite(output_path, stitched_image)
