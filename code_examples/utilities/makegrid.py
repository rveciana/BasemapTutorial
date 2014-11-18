from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

fig=plt.figure(figsize=(9, 3))

map = Basemap(width=12000000,height=8000000,
            resolution='l',projection='stere',
            lat_ts=50,lat_0=50,lon_0=-107.)

lons, lats, x, y = map.makegrid(30, 30, returnxy=True)

ax = fig.add_subplot(121)
ax.set_title('The regular grid')
map.scatter(x, y, marker='o')
map.drawcoastlines()


ax = fig.add_subplot(122)
ax.set_title('Projection changed')

map = Basemap(width=12000000,height=9000000,projection='aeqd',
            lat_0=50.,lon_0=-105.)
x, y = map(lons, lats)
map.scatter(x, y, marker='o')
map.drawcoastlines()

plt.show()