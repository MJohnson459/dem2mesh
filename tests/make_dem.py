"""Write a small synthetic DSM in UTM so dem2mesh has matching horizontal and vertical units."""
import sys

import numpy as np
from osgeo import gdal, osr

out = sys.argv[1]
size = 64
y, x = np.mgrid[0:size, 0:size].astype("float32")
dem = 100 + 10 * np.sin(x / 8) + 5 * np.cos(y / 6)

driver = gdal.GetDriverByName("GTiff")
ds = driver.Create(out, size, size, 1, gdal.GDT_Float32)
ds.SetGeoTransform((500000, 1.0, 0, 6200000, 0, -1.0))
srs = osr.SpatialReference()
srs.ImportFromEPSG(32630)
ds.SetProjection(srs.ExportToWkt())
ds.GetRasterBand(1).WriteArray(dem)
ds.FlushCache()
