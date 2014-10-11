from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

map = Basemap(projection='aeqd',
              lon_0 = 0,
              lat_0 = 90,
              width = 10000000,
              height = 10000000)

map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='coral',lake_color='aqua')
map.drawcoastlines()

for i in range(0, 10000000, 1000000):
    map.plot(i, i, marker='o',color='k')

plt.show()