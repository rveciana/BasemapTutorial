from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

map = Basemap(projection='merc', 
              lat_0=0, lon_0=0,
              llcrnrlon=-20.,llcrnrlat=0.,urcrnrlon=180.,urcrnrlat=80.)

map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='coral',lake_color='aqua')
map.drawcoastlines()

map.drawparallels(range(0, 90, 20))
map.drawmeridians(range(0, 180, 20))

#Paris-Tokyo
map.drawgreatcircle(2.3, 48.9, 139.7, 35.6,linewidth=2,color='r')
#Tokyo-Dubai
map.drawgreatcircle(139.7, 35.6, 55.2, 25.,linewidth=2,color='r')
#Dubai-Paris
map.drawgreatcircle(55.2, 25., 2.3, 48.9,linewidth=2,color='r')

plt.show()