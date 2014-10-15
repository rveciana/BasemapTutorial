from osgeo import gdal
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

wrf_out_file = "wrfout_v2_Lambert.nc"

ds_lon = gdal.Open('NETCDF:"'+wrf_out_file+'":XLONG')
ds_lat = gdal.Open('NETCDF:"'+wrf_out_file+'":XLAT')
ds_t2 = gdal.Open('NETCDF:"'+wrf_out_file+'":T2')

map = Basemap(llcrnrlon=-95.,llcrnrlat=24.,urcrnrlon=-66.,urcrnrlat=45.)

map.contourf(ds_lon.ReadAsArray()[1], ds_lat.ReadAsArray()[1], ds_t2.ReadAsArray()[1]) 

map.drawcoastlines()
 
plt.show()