from mindat import MindatAPI
import os
from itertools import islice
import logging
import geopandas as gpd
from tqdm.auto import tqdm
from typing import Optional
import geopandas as gpd
from shapely.geometry import Point
from typing import Iterator
from locality import Locality
from dataclasses import asdict
import pandas as pd
import warnings
import os
import json

warnings.simplefilter(action="ignore", category=FutureWarning)


def cache_to_jsonl(file_path):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Check if the cache file exists
            if os.path.exists(file_path):
                logging.info(f"Loading cached data from {file_path}")
                # Load and return the DataFrame from the JSONL file
                return pd.read_json(file_path, lines=True, orient="records")
            else:
                logging.info(f"Cache file {file_path} not found, running function")
                # Execute the function to get the DataFrame
                df = func(*args, **kwargs)
                # Save the DataFrame to a JSONL file
                logging.info(f"Caching data to {file_path}")
                df.to_json(file_path, lines=True, orient="records")
                return df

        return wrapper

    return decorator


def convert_object_to_string(df):
    # Check each column in the DataFrame
    for column in df.columns:
        if pd.api.types.is_object_dtype(df[column]):
            df[column] = df[column].apply(lambda x: str(x) if not pd.isnull(x) else x)
    return df


def build_geodataframe_from_dataframe(localities: pd.DataFrame) -> gpd.GeoDataFrame:
    gdf = gpd.GeoDataFrame(localities)
    gdf["geometry"] = gpd.points_from_xy(gdf["longitude"], gdf["latitude"])
    gdf.set_geometry("geometry", inplace=True)
    gdf.crs = "WGS84"

    return gdf


@cache_to_jsonl("extracts/localities.jsonl")
def localities_to_pandas() -> pd.DataFrame:
    logging.info("Starting extraction")
    api = MindatAPI(api_key=os.getenv("MINDAT_API_KEY"))

    localities = tqdm(api.get_localities(), desc="Extracting localities")
    logging.info("Extraction complete")
    df = pd.DataFrame([asdict(l) for l in localities])

    return df


@cache_to_jsonl("extracts/geomaterials.jsonl")
def geomaterials_to_pandas(limit: Optional[int] = None) -> pd.DataFrame:
    logging.info("Starting extraction")
    api = MindatAPI(api_key=os.getenv("MINDAT_API_KEY"))

    geomaterials = tqdm(
        islice(api.get_geomaterials(), limit), desc="Extracting geomaterials"
    )

    logging.info("Extraction complete")
    df = pd.DataFrame(geomaterials)

    return df


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    localities = localities_to_pandas()
    print(localities)
    # localities.to_file("extracts/localities.gpkg", driver="GPKG")

    geomaterials = geomaterials_to_pandas()
    geomaterials.rename(columns={"id": "geomaterial_id"}, inplace=True)
    # geomaterials contains a column 'locality' which is a list of locality IDs
    # We need to augment the localities to add a column that lists geomaterial ids for each location
    # We will also create a column in localities that lists the names of the geomaterials found at each location
    # We will then write the augmented localities to a GeoPackage file

    logging.info("Building map of locality to geomaterials")
    exploded_geomaterials = geomaterials.explode("locality")
    exploded_geomaterials.rename(columns={"locality": "locality_id"}, inplace=True)
    merged = pd.merge(localities, exploded_geomaterials, on="locality_id", how="inner")
    aggregated = (
        merged.groupby("locality_id")[["geomaterial_id", "name"]]
        .agg(lambda x: ",".join([str(y) for y in x]))
        .reset_index()
        .rename(
            columns={"geomaterial_id": "geomaterial_ids", "name": "geomaterial_names"}
        )
    )

    logging.info("Augmenting localities with geomaterials for that locality")
    localities_augmented = pd.merge(
        localities, aggregated, on="locality_id", how="left"
    )

    # Fiona/OGR does not support datetime64[ns] data types,apparently
    localities_augmented = convert_object_to_string(localities_augmented)
    gdf = build_geodataframe_from_dataframe(localities_augmented)

    logging.info("Writing augmented localities to GeoPackage")
    gdf.to_file("extracts/localities_augmented.gpkg", driver="GPKG")
    logging.info("Done")
