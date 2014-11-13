from mpl_toolkits.basemap import Basemap
from mpl_toolkits.basemap import shiftgrid
import matplotlib.pyplot as plt
from osgeo import gdal
import numpy as np

fig=plt.figure(figsize=(9, 3))

map = Basemap(projection='merc', 
              lat_0=0,
              resolution='h',
              llcrnrlon=32, 
              llcrnrlat=31, 
              urcrnrlon=33, 
              urcrnrlat=32)

ds = gdal.Open("../sample_files/dem.tiff")
data = ds.ReadAsArray()

lons = np.linspace(0, 40, data.shape[1])
lats = np.linspace(0, 35, data.shape[0])

ax = fig.add_subplot(121)
ax.set_title('Without transform_scalar')

llons, llats = np.meshgrid(lons, lats)
x, y = map(llons, llats)

map.pcolormesh(x, y, data, vmin=900, vmax=950)

map.drawcoastlines()

ax = fig.add_subplot(122)
ax.set_title('Applying transform_scalar')

data_interp, x, y = map.transform_scalar(data, lons, lats, 40, 40, returnxy=True)

map.pcolormesh(x, y, data_interp, vmin=900, vmax=950)

map.drawcoastlines()

plt.show()