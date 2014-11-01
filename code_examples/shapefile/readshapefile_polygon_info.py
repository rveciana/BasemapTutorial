from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

map = Basemap(llcrnrlon=-0.5,llcrnrlat=39.8,urcrnrlon=4.,urcrnrlat=43.,
             resolution='i', projection='tmerc', lat_0 = 39.5, lon_0 = 1)

map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='#ddaa66',lake_color='aqua')
map.drawcoastlines()

map.readshapefile('../sample_files/comarques', 'comarques', drawbounds = False)

for info, shape in zip(map.comarques_info, map.comarques):
    if info['nombre'] == 'Selva':
        x, y = zip(*shape) 
        map.plot(x, y, marker=None,color='m')
plt.show()