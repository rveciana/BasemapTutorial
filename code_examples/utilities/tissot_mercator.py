from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

map = Basemap(projection='merc', 
              lat_0=0, lon_0=0,
              llcrnrlon=-180.,llcrnrlat=-80.,urcrnrlon=180.,urcrnrlat=80.,)

map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='coral',lake_color='aqua')
map.drawcoastlines()

for lon in range(-160, 180, 30):
    for lat in range(-60, 90, 30):
        map.tissot(lon, lat, 4, 50)
        
plt.show()