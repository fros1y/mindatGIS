# %%
import geopandas as gpd

# %%
mindat_locations = gpd.read_file("../extracts/localities_access.gpkg")

# %%
# This seems okay for country, but second level data is garbage.
mindat_locations["country"] = mindat_locations["revtxtd"].str.split(",").str[0]

states_gdf = gpd.read_file(
    "https://raw.githubusercontent.com/PublicaMundi/MappingAPI/master/data/geojson/us-states.json"
)

# %%
states_gdf.rename(columns={"name": "state"}, inplace=True)

# %%
mindat_locations_with_states = gpd.sjoin(
    mindat_locations, states_gdf, how="left", predicate="within"
)
mindat_locations_with_states.drop(columns="index_right", inplace=True)


# %%
import simplekml


# AABBGGRR format (Alpha, Blue, Green, Red).
KMLRed = "ff0000ff"
KMLGreen = "ff00ff00"
KMLBlue = "ffff0000"
KMLYellow = "ff00ffff"
KMLWhite = "ffffffff"

KMLAccess = simplekml.Style()
KMLAccess.labelstyle.scale = 0
KMLAccess.iconstyle.color = KMLGreen
KMLAccess.iconstyle.scale = 1
KMLAccess.iconstyle.icon.href = (
    "http://maps.google.com/mapfiles/kml/shapes/placemark_circle.png"
)

KMLNoAccess = simplekml.Style()
KMLNoAccess.labelstyle.scale = 0
KMLNoAccess.iconstyle.color = KMLRed
KMLNoAccess.iconstyle.scale = 1
KMLNoAccess.iconstyle.icon.href = (
    "http://maps.google.com/mapfiles/kml/shapes/placemark_circle.png"
)

KMLRestrictedAccess = simplekml.Style()
KMLRestrictedAccess.labelstyle.scale = 0
KMLRestrictedAccess.iconstyle.color = KMLYellow
KMLRestrictedAccess.iconstyle.scale = 1
KMLRestrictedAccess.iconstyle.icon.href = (
    "http://maps.google.com/mapfiles/kml/shapes/placemark_circle.png"
)

KMLUnknownAccess = simplekml.Style()
KMLUnknownAccess.labelstyle.scale = 0
KMLUnknownAccess.iconstyle.color = KMLBlue
KMLUnknownAccess.iconstyle.scale = 1
KMLUnknownAccess.iconstyle.icon.href = (
    "http://maps.google.com/mapfiles/kml/shapes/placemark_circle.png"
)

KMLWhiteAccess = simplekml.Style()
KMLWhiteAccess.labelstyle.scale = 0
KMLWhiteAccess.iconstyle.color = KMLWhite
KMLWhiteAccess.iconstyle.scale = 1
KMLWhiteAccess.iconstyle.icon.href = (
    "http://maps.google.com/mapfiles/kml/shapes/placemark_circle.png"
)

# %%
import re


def cleanup(s):
    if s is None:
        return ""
    # remove html tags
    s = re.sub(r"<[^>]*>", "", s)
    # remove anything that looks like an entity
    s = re.sub(r"&[^;]*;", "", s)
    # remove #s
    s = re.sub(r"#", "", s)
    return ensureValidUTF8(s)


def ensureValidUTF8(s):
    return s.encode("utf-8", "ignore").decode("utf-8")


import tqdm


def write_kml(gdf, filename):
    kml = simplekml.Kml()
    print(f"Exporting {filename}")

    for index, row in gdf.iterrows():
        if row.locality_id == 159901:
            continue  # There is something strange in here that kills simplekml export
        # Assuming the geometry type is Point
        if row.geometry is None:
            continue
        if row.geometry.geom_type == "Point":
            pnt = kml.newpoint(
                name=cleanup(row["txt"]),
                coords=[(row.geometry.x, row.geometry.y)],
            )

            if row["geomaterial_names"] is None:
                geomaterial_hyperlinks = ""
            else:
                split_geomaterials = row["geomaterial_names"].split(",")
                split_geomaterial_ids = row["geomaterial_ids"].split(",")
                combined = zip(split_geomaterials, split_geomaterial_ids)
                geomaterial_hyperlinks = (
                    "<p><b>Geomaterials:</b> <ul>"
                    + "\n".join(
                        [
                            f"<li><a href='https://www.mindat.org/min-{x[1]}.html'>{x[0]}</a></li>"
                            for x in combined
                        ]
                    )
                    + "</ul></p>"
                )

            mindat_link = f"https://www.mindat.org/loc-{row['locality_id']}.html"
            pnt.description = f"""
            <html>
            <p><a href='{mindat_link}'>Mindat.org</a></p>
            <p><b>Description:</b> {cleanup(row["description_short"])}</p>
            
            {geomaterial_hyperlinks}
        
            </html>"""

            if row.access_level == "Open Access":
                pnt.style = KMLAccess
            elif row.access_level == "Restricted Access":
                pnt.style = KMLRestrictedAccess
            elif row.access_level == "No Access":
                pnt.style = KMLNoAccess
            elif row.access_level == "Unknown":
                pnt.style = KMLUnknownAccess
            else:
                pnt.style = KMLWhiteAccess

        else:
            print(f"Unhandled geometry type: {row.geometry.type}")
            continue
    kml.save(filename)


# %%
export = mindat_locations_with_states
# %%

write_kml(mindat_locations_with_states, "../extracts/localities_all.kml")
# %%

for country_name, per_country_df in export.groupby("country"):
    if country_name is None:
        continue
    country_name = re.sub(r"[^a-zA-Z0-9_\-\.]", "", country_name)
    if country_name == "":
        continue
    if country_name == "USA":
        for state_name, per_state_df in per_country_df.groupby("state"):
            try:
                write_kml(
                    per_state_df,
                    f"../extracts/localities_{country_name}_{state_name}.kml",
                )
            except Exception as e:
                print(f"Error writing {country_name}_{state_name}.kml: {e}")
                continue

    write_kml(per_country_df, f"../extracts/localities_{country_name}.kml")

    # Write to a KML file


# %%
