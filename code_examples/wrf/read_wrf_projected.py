from osgeo import gdal
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

wrf_out_file = "wrfout_v2_Lambert.nc"

ds_lon = gdal.Open('NETCDF:"'+wrf_out_file+'":XLONG')
ds_lat = gdal.Open('NETCDF:"'+wrf_out_file+'":XLAT')

ds_t2 = gdal.Open('NETCDF:"'+wrf_out_file+'":T2')

map = Basemap(llcrnrlon=-95.,llcrnrlat=27.,urcrnrlon=-65.,urcrnrlat=40.,
              projection='lcc', lat_1=30.,lat_2=60.,lat_0=34.83158,lon_0=-98.)

x, y = map(ds_lon.ReadAsArray()[1], ds_lat.ReadAsArray()[1])

map.contourf(x, y, ds_t2.ReadAsArray()[1]) 

map.drawcoastlines()
plt.show()
