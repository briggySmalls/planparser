import pytest
import yaml
from pathlib import Path

from planparser.planparser import PlanParser

_TEST_DIR = Path(__file__).parent
_TEST_DATA_DIR = _TEST_DIR / "test_data"
_TEST_IMAGES_DIR = _TEST_DATA_DIR / "floorplans"


def data_array():
    with open(_TEST_DATA_DIR / "floorplans.yaml", "r") as file:
        return yaml.safe_load(file)


_DATA_ARRAY = data_array()


@pytest.mark.parametrize("floorplan", _DATA_ARRAY["floorplans"], ids=[d["file"] for d in _DATA_ARRAY["floorplans"]])
def test_areas(floorplan):
    image_file = _TEST_IMAGES_DIR / floorplan["file"]
    result = PlanParser.parse(image_file)
    assert result.area == floorplan["area"]
