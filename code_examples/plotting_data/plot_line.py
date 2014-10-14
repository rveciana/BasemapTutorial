from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

map = Basemap(projection='ortho', 
              lat_0=0, lon_0=0)

map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='coral',lake_color='aqua')
map.drawcoastlines()

lons = [-10, -20, -25, -10, 0, 10]
lats = [40, 30, 10, 0, 0, -5]

x, y = map(lons, lats)

map.plot(x, y, marker=None,color='m')

plt.show()