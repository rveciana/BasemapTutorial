from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

map = Basemap(projection='ortho', 
              lat_0=0, lon_0=0)

map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='#cc9955',lake_color='aqua')
map.drawcoastlines()

lon = 3.4
lat = 3.4

x, y = map(lon, lat)

plt.text(x, y, 'Lagos',fontsize=12,fontweight='bold',
                    ha='left',va='bottom',color='k')

lon = 2.1
lat = 41.

x, y = map(lon, lat)

plt.text(x, y, 'Barcelona',fontsize=12,fontweight='bold',
                    ha='left',va='center',color='k',
                    bbox=dict(facecolor='b', alpha=0.2))
plt.show()