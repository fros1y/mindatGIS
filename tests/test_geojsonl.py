import pytest
import json
from mindatGIS.geojsonl import GeoJSONLWriter


@pytest.fixture
def output_file(tmp_path):
    file_path = tmp_path / "output.geojsonl"
    yield file_path


def test_addFeature(output_file):
    writer = GeoJSONLWriter(output_file)
    writer.addFeature(1, "testPt", "description of testPt", 10.0, 20.0)

    with open(output_file, "r") as file:
        feature = json.loads(file.readline())

    assert feature["type"] == "Feature"
    assert feature["geometry"]["type"] == "Point"
    assert feature["geometry"]["coordinates"] == [10.0, 20.0]
    assert feature["properties"]["id"] == 1
    assert feature["properties"]["name"] == "testPt"
    assert feature["properties"]["description"] == "description of testPt"
