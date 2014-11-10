from mpl_toolkits.basemap import Basemap
from mpl_toolkits.basemap import interp
import matplotlib.pyplot as plt
from osgeo import gdal
import numpy as np


map = Basemap(llcrnrlon=-82., llcrnrlat=28., urcrnrlon=-79., urcrnrlat=29.5,
              projection='lcc', lat_1=30., lat_2=60., lat_0=34.83158, lon_0=-98.,
              resolution='i')

ds = gdal.Open("../sample_files/wrf.tiff")
lons = ds.GetRasterBand(4).ReadAsArray()
lats = ds.GetRasterBand(5).ReadAsArray()
u10 = ds.GetRasterBand(1).ReadAsArray()
v10 = ds.GetRasterBand(2).ReadAsArray()

x, y = map(lons, lats)

x2 = np.linspace(x[0][0],x[0][-1],x.shape[1]*2)
y2 = np.linspace(y[0][0],y[-1][0],y.shape[0]*2)

x2, y2 = np.meshgrid(x2, y2)

u10_2 = interp(u10,  x[0], np.flipud(y[:, 0]), x2, np.flipud(y2),order=1)
v10_2 = interp(v10,  x[0], np.flipud(y[:, 0]), x2, np.flipud(y2),order=1)

map.drawmapboundary(fill_color='#9999FF')
map.fillcontinents(color='#cc9955', lake_color='#9999FF', zorder = 0)
map.drawcoastlines(color = '0.15')

map.barbs(x, y, u10, v10, 
    pivot='middle', barbcolor='#555555')

map.barbs(x2, y2, u10_2, v10_2, 
    pivot='middle', barbcolor='#FF3333')

plt.show()