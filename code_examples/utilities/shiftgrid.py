from mpl_toolkits.basemap import Basemap
from mpl_toolkits.basemap import shiftgrid
import matplotlib.pyplot as plt
import numpy as np

map = Basemap(projection='sinu', 
              lat_0=0, lon_0=0)

lons = np.arange(30, 410, 30)
lons[1] = 70
lats = np.arange(0, 100, 10)

data = np.indices((lats.shape[0], lons.shape[0]))
data = data[0] + data[1]

print data
print lons

data, lons = shiftgrid(180., data, lons, start=False)

print data
print lons

llons, llats = np.meshgrid(lons, lats)

x, y = map(llons, llats)

map.contourf(x, y, data)
map.drawcoastlines()
plt.show()