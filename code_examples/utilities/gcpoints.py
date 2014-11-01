from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

map = Basemap(projection='merc', 
              lat_0=0, lon_0=0,
              llcrnrlon=-20.,llcrnrlat=0.,urcrnrlon=180.,urcrnrlat=80.)

map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='coral',lake_color='aqua')
map.drawcoastlines()

x, y = map.gcpoints(2.3, 48.9, 139.7, 35.6, 300)

print x, y

map.plot(x, y)
plt.show()