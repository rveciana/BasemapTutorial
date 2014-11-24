import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

fig = plt.figure()

ax = fig.add_subplot(211)
ax.set_title("Hammer projection")
map = Basemap(projection='hammer', lon_0 = 10, lat_0 = 50)

map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='coral',lake_color='aqua')
map.drawcoastlines()

ax = fig.add_subplot(212)
ax.set_title("Robinson projection")
map = Basemap(projection='robin', lon_0 = 10, lat_0 = 50)

map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='coral',lake_color='aqua')
map.drawcoastlines()

plt.show()