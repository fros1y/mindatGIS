from mindat import MindatAPI
from geojsonl import GeoJSONLWriter
import os
from itertools import islice
import logging
import json
from tqdm.auto import tqdm

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    logging.info("Starting extraction")
    api = MindatAPI(api_key=os.getenv("MINDAT_API_KEY"))

    # print(api.get_geomaterial(1, params={"expand": "locality"}))
    with open("extracts/geomaterials.jsonl", "w") as output_file:
        geomaterials = api.get_geomaterials()
        # geomaterials = islice(api.get_geomaterials(), 10)
        for geo in tqdm(geomaterials):
            output_file.write(json.dumps(geo) + "\n")
