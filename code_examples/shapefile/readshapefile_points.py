from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

map = Basemap(llcrnrlon=-0.5,llcrnrlat=39.8,urcrnrlon=4.,urcrnrlat=43.,
             resolution='i', projection='tmerc', lat_0 = 39.5, lon_0 = 1)

map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='#ddaa66',lake_color='aqua')
map.drawcoastlines()

map.readshapefile('../sample_files/comarques', 'comarques')

lightning_info = map.readshapefile('../sample_files/lightnings', 'lightnings')

print lightning_info

for info, lightning in zip(map.lightnings_info, map.lightnings):
    if float(info['amplitude']) < 0:
        marker = '_'
    else:
        marker = '+'
    map.plot(lightning[0], lightning[1], marker=marker, color='m', markersize=8, markeredgewidth=2)

plt.show()