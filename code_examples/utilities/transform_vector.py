from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from osgeo import gdal
import numpy as np

map = Basemap(projection='sinu', 
              lat_0=0, lon_0=0)

lons = np.linspace(-180, 180, 8)
lats = np.linspace(-90, 90, 8)

v10 = np.ones((lons.shape)) * 15
u10 = np.zeros((lons.shape))

u10, v10 = np.meshgrid(u10, v10)

u10_rot, v10_rot, x_rot, y_rot = map.transform_vector(u10, v10, 
                                                      lons, lats, 
                                                      15, 15, 
                                                      returnxy=True)

map.drawmapboundary(fill_color='#9999FF')
map.fillcontinents(color='#ddaa66', lake_color='#9999FF', zorder = 0)
map.drawcoastlines(color = '0.15')

#Drawing the original points
lons, lats = np.meshgrid(lons, lats)
x, y = map(lons, lats)
map.barbs(x, y, u10, v10, 
    pivot='middle', barbcolor='#333333')

#Drawing the rotated & interpolated points
map.barbs(x_rot, y_rot, u10_rot, v10_rot, 
    pivot='middle', barbcolor='#ff5555')

plt.show()
