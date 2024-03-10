import json


class GeoJSONLWriter:
    def __init__(self, output_file):
        self.output_file = output_file

    def addFeature(self, id: int, name: str, description: str, x: float, y: float):
        feature = {
            "type": "Feature",
            "geometry": {"type": "Point", "coordinates": [x, y]},
            "properties": {"id": id, "name": name, "description": description},
        }
        self.output_file.write(json.dumps(feature) + "\n")
