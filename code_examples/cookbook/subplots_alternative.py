import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

fig, axes = plt.subplots(2, 1)

axes[0].set_title("Hammer projection")
map = Basemap(projection='hammer', lon_0 = 10, lat_0 = 50, ax=axes[0])

map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='coral',lake_color='aqua')
map.drawcoastlines()

axes[1].set_title("Robinson projection")
map = Basemap(projection='robin', lon_0 = 10, lat_0 = 50, ax=axes[1])

map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='coral',lake_color='aqua')
map.drawcoastlines()

plt.show()