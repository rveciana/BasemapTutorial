
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from osgeo import gdal
import numpy

map = Basemap(projection='tmerc', 
              lat_0=0, lon_0=3,
              llcrnrlon=1.819757266426611, 
              llcrnrlat=41.583851612359275, 
              urcrnrlon=1.841589961763497, 
              urcrnrlat=41.598674173123)

ds = gdal.Open("../sample_files/dem.tiff")
data = ds.ReadAsArray()

lon, lat = map.makegrid(data.shape[1], data.shape[0])
xx, yy = map(lon, lat)

map.contourf(xx, yy, data)

plt.show()

