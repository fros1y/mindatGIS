import pytest

import mindatGIS.spatialite as spl


def test_spatialite():
    path = pytest.tmpdir_factory.mktemp("data").join("spatialite_test.sqlite")
    with spl.SpatialiteWriter(path) as writer:
        writer.addFeature(1, "testPt", "description of testPt")
    assert path.exists()
