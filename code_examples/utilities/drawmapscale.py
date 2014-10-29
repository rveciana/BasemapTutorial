from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

map = Basemap(llcrnrlon=-10.5,llcrnrlat=35,urcrnrlon=4.,urcrnrlat=44.,
             resolution='i', projection='tmerc', lat_0 = 39.5, lon_0 = -3.25)

map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='#cc9955',lake_color='aqua')
map.drawcoastlines()

map.drawmapscale(-7., 35.8, -3.25, 39.5, 500, barstyle='fancy')

map.drawmapscale(-0., 35.8, -3.25, 39.5, 500, fontsize = 14)

plt.show()

