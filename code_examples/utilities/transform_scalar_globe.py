from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np


fig=plt.figure(figsize=(9, 3))

map = Basemap(projection='robin', 
              lat_0=0, lon_0=0)

lons = np.arange(-180, 190, 60)
lats = np.arange(-90, 100, 30)

data = np.indices((lats.shape[0], lons.shape[0]))
data = data[0] + data[1]

llons, llats = np.meshgrid(lons, lats)

ax = fig.add_subplot(121)
ax.set_title('Without transform_scalar')

x, y = map(llons, llats)

map.pcolormesh(x, y, data, cmap='Paired')

map.drawcoastlines()

ax = fig.add_subplot(122)
ax.set_title('Applying transform_scalar')

data_interp, x, y = map.transform_scalar(data, lons, lats, 50, 30, returnxy=True, masked=True)

map.pcolormesh(x, y, data_interp, cmap='Paired')

map.drawcoastlines()

plt.show()