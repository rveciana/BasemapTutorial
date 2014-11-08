from mpl_toolkits.basemap import Basemap
from mpl_toolkits.basemap import addcyclic
import matplotlib.pyplot as plt
import numpy as np

map = Basemap(projection='sinu', 
              lat_0=0, lon_0=0)

lons = np.arange(30, 390, 30)
lats = np.arange(0, 100, 10)

data = np.indices((lats.shape[0], lons.shape[0]))
data = data[0] + data[1]

data , lons = addcyclic(data, lons)

lons, data = map.shiftdata(lons, datain = data, lon_0=0)

llons, llats = np.meshgrid(lons, lats)

x, y = map(llons, llats)

map.contourf(x, y, data)

map.drawcoastlines()
plt.show()