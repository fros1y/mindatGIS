# %%
import geopandas as gpd
import rasterio.warp
from shapely.geometry import shape

# Available here https://www.usgs.gov/programs/gap-analysis-project/science/pad-us-data-download
# Download the GeoPackage Zip and extract the PADUS3_0Geopackage.gpkg file
padus = gpd.read_file("../extracts/PADUS3_0Geopackage.gpkg")

# %%
localities = gpd.read_file("../extracts/mindat_localities.gpkg")

# %%
padus["Pub_Access"] = padus["Pub_Access"].map(
    {
        "OA": "Open Access",
        "RA": "Restricted Access",
        "XA": "No Access",
        "UK": "Unknown",
    }
)

access_regions = padus[["Unit_Nm", "Pub_Access", "geometry"]]
access_regions.columns = ["area_name", "access_level", "geometry"]

# %%

from tqdm import tqdm

# destination_crs = "EPSG:4326"
# geometry = list(
#     tqdm(
#         rasterio.warp.transform_geom(
#             src_crs=access_regions.crs,
#             dst_crs=destination_crs,
#             geom=access_regions.geometry.values,
#         )
#     )
# )

# import logging

# from shapely.geometry import shape, area


# %%
# def convert_geom(geom):
#     try:
#         return shape(geom) if area(geom) < 1e6 else None
#     except:
#         print(f"Failed to convert geometry: {geom}")
#         return None


# converted = [convert_geom(geom) for geom in geometry]

# %%

# access_regions_4326 = access_regions.set_geometry(
#     converted,
#     crs=destination_crs,
# )

access_regions_4326 = access_regions.to_crs("EPSG:4326")

# %%
# filter out where geometry.area is over 1000.  There are some coding errors in the data

access_regions_4326_filtered = access_regions_4326[
    access_regions_4326.geometry.area < 1000
]
# %%
joined = localities.sjoin(access_regions_4326_filtered, predicate="within", how="left")
joined.drop("index_right", axis=1, inplace=True)

# %%
joined.to_file("../extracts/localities_access.gpkg", driver="GPKG")

# %%
