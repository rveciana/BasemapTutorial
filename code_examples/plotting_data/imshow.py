from mpl_toolkits.basemap import Basemap
from mpl_toolkits.basemap import shiftgrid
import matplotlib.pyplot as plt
from osgeo import gdal
import numpy as np

map = Basemap(projection='tmerc', 
              lat_0=0, lon_0=3,
              llcrnrlon=1.819757266426611, 
              llcrnrlat=41.583851612359275, 
              urcrnrlon=1.841589961763497, 
              urcrnrlat=41.598674173123)

ds = gdal.Open("../sample_files/dem.tiff")
elevation = ds.ReadAsArray()

map.imshow(plt.imread('../sample_files/orthophoto.jpg'))

map.imshow(elevation, cmap = plt.get_cmap('terrain'), alpha = 0.5)

plt.show()



