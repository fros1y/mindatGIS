from mindat import MindatAPI
from geojsonl import GeoJSONLWriter
import os
from itertools import islice
import logging


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    logging.info("Starting extraction")
    api = MindatAPI(api_key=os.getenv("MINDAT_API_KEY"))

    with open("extracts/localities.geojsonl", "w") as output_file:
        db = GeoJSONLWriter(output_file)
        locations = islice(api.get_localities(), 10)
        for loc in locations:
            db.addFeature(
                loc["id"],
                loc["txt"],
                loc["description_short"],
                loc["longitude"],
                loc["latitude"],
            )
    logging.info("Extraction complete")
