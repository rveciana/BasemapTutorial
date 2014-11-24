import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

fig, axes = plt.subplots(2, 1)

ax1 = axes[0]
ax1.set_title("Hammer projection")
map = Basemap(projection='hammer', lon_0 = 10, lat_0 = 50, ax=ax1)

map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='coral',lake_color='aqua')
map.drawcoastlines()

ax2 = axes[1]
ax2.set_title("Robinson projection")
map = Basemap(projection='robin', lon_0 = 10, lat_0 = 50, ax=ax2)

map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='coral',lake_color='aqua')
map.drawcoastlines()

plt.show()