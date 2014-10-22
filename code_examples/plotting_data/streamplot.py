from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from osgeo import gdal
import numpy


map = Basemap(llcrnrlon=-93.7, llcrnrlat=28., urcrnrlon=-66.1, urcrnrlat=39.5,
              projection='lcc', lat_1=30., lat_2=60., lat_0=34.83158, lon_0=-98.)

ds = gdal.Open("../sample_files/wrf.tiff")
lons = ds.GetRasterBand(4).ReadAsArray()
lats = ds.GetRasterBand(5).ReadAsArray()
u10 = ds.GetRasterBand(1).ReadAsArray()
v10 = ds.GetRasterBand(2).ReadAsArray()
speed = numpy.sqrt(u10*u10 + v10*v10)
xx, yy = map.makegrid(v10.shape[1], v10.shape[0], returnxy=True)[2:4]

map.streamplot(xx, yy, u10, v10, color=speed, cmap=plt.cm.autumn, linewidth=0.5*speed)

map.drawcoastlines(color = '0.15')

plt.show()

