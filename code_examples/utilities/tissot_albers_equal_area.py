from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

map = Basemap(width=8000000,height=7000000,
            resolution='l',projection='aea',\
            lat_1=40.,lat_2=60,lon_0=35,lat_0=50)

map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='coral',lake_color='aqua')
map.drawcoastlines()

for lon in range(-160, 180, 20):
    for lat in range(-60, 90, 10):
        map.tissot(lon, lat, 2, 50)
     
plt.show()