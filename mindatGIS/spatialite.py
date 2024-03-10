# FIXME: Doens't work yet

# from osgeo import ogr, osr


# class SpatialiteWriter:
#     def __init__(self, db: str):
#         self.db = db
#         drvr = ogr.GetDriverByName("SQLite")
#         self.ds = drvr.CreateDataSource(db, options=["SPATIALITE=yes"])
#         self.ds = drvr.Open(db, 1)

#         srs = osr.SpatialReference()
#         srs.ImportFromEPSG(27700)  # FIXME: This should be a parameter
#         lr = self.ds.CreateLayer("pts", srs, geom_type=ogr.wkbPoint)
#         lr.CreateField(ogr.FieldDefn("id", ogr.OFTInteger))
#         lr.CreateField(ogr.FieldDefn("name", ogr.OFTString))
#         lr.CreateField(ogr.FieldDefn("description", ogr.OFTString))
#         self.lr = lr

#     def __del__(self):
#         del self.lr
#         self.ds.Destroy()

#     def addFeature(self, id: int, name: str, description: str, x: float, y: float):
#         featureDefn = self.lr.GetLayerDefn()
#         feature = ogr.Feature(featureDefn)
#         feature.SetGeometry(ogr.CreateGeometryFromWkt(f"POINT ({x} {y})"))
#         feature.SetField("id", id)
#         feature.SetField("name", name)
#         feature.SetField("description", description)
#         self.lr.CreateFeature(feature)
