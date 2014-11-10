from mpl_toolkits.basemap import Basemap
from mpl_toolkits.basemap import maskoceans
from mpl_toolkits.basemap import interp
import matplotlib.pyplot as plt
from osgeo import gdal
import numpy as np


map = Basemap(llcrnrlon=-93.7, llcrnrlat=28., urcrnrlon=-66.1, urcrnrlat=39.5,
              projection='lcc', lat_1=30., lat_2=60., lat_0=34.83158, lon_0=-98., 
              resolution="h")

ds = gdal.Open("../sample_files/wrf.tiff")
lons = ds.GetRasterBand(4).ReadAsArray()
lats = ds.GetRasterBand(5).ReadAsArray()
data = ds.GetRasterBand(3).ReadAsArray()

x, y = map(lons, lats)

plt.figure(0)

mdata = maskoceans(lons, lats, data)

map.drawcoastlines(color = '0.15')
map.contourf(x, y, mdata)

plt.figure(1)

x2 = np.linspace(x[0][0],x[0][-1],x.shape[1]*5)
y2 = np.linspace(y[0][0],y[-1][0],y.shape[0]*5)

x2, y2 = np.meshgrid(x2, y2)

data2 = interp(data,  x[0], np.flipud(y[:, 0]), x2, np.flipud(y2),order=1)

lons2, lats2 = map(x2, y2, inverse=True)
mdata = maskoceans(lons2, lats2, data2, resolution = 'c', grid = 10, inlands=True)

map.drawcoastlines(color = '0.15')
map.contourf(x2, y2, mdata)

plt.figure(2)

mdata = maskoceans(lons2, lats2, data2, resolution = 'h', grid = 10, inlands=True)

map.drawcoastlines(color = '0.15')
map.contourf(x2, y2, mdata)

plt.figure(3)

mdata = maskoceans(lons2, lats2, data2, resolution = 'h', grid = 1.25, inlands=True)

map.drawcoastlines(color = '0.15')
map.contourf(x2, y2, mdata)

plt.show()