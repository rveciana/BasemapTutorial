from osgeo import gdal
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

wrf_out_file = "wrfout_v2_Lambert.nc"

ds_lon = gdal.Open('NETCDF:"'+wrf_out_file+'":XLONG')
ds_lat = gdal.Open('NETCDF:"'+wrf_out_file+'":XLAT')

ds_u = gdal.Open('NETCDF:"'+wrf_out_file+'":U10')
ds_v = gdal.Open('NETCDF:"'+wrf_out_file+'":V10')

map = Basemap(llcrnrlon=-93.7, llcrnrlat=28., urcrnrlon=-66.1, urcrnrlat=39.5,
              resolution = 'l',
              projection='lcc', lat_1=30., lat_2=60., lat_0=34.83158, lon_0=-98.)

x, y = map(ds_lon.ReadAsArray()[1], ds_lat.ReadAsArray()[1])


u = ds_u.ReadAsArray()[1]
v = ds_v.ReadAsArray()[1]

yy = np.arange(0, y.shape[0], 4)
xx = np.arange(0, x.shape[1], 4)

points = np.meshgrid(yy, xx) 

map.contourf(x, y, np.sqrt(u*u + v*v), alpha = 0.4) 
map.barbs(x[points], y[points], u[points], v[points]) 

map.drawcoastlines(color = '0.15')
plt.show()
