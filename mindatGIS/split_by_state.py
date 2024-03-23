# %%
import geopandas as gpd

# Load a GeoDataFrame that contains the boundaries of U.S. states
states_gdf = gpd.read_file(
    "https://raw.githubusercontent.com/PublicaMundi/MappingAPI/master/data/geojson/us-states.json"
)
# %%
states_gdf.rename(columns={"name": "state_name"}, inplace=True)

# %%
mindat_locations = gpd.read_file("../extracts/localities_access.gpkg")

# %%

with_states = gpd.sjoin(
    mindat_locations, states_gdf[["state_name", "geometry"]], predicate="within"
)

# %%

with_states = with_states.drop(columns=["index_right"])

# %%
import fiona

fiona.supported_drivers["KML"] = "rw"

# Write to a file per state
for state_name, per_state_df in with_states.groupby("state_name"):
    # Write to a KML file
    per_state_df.to_file(
        f"../extracts/per_state/localities_access_{state_name}.kml", driver="KML"
    )

# %%
