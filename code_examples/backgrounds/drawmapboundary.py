from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

plt.figure(0)
map = Basemap(projection='ortho',lon_0=0,lat_0=0,resolution='c')
map.drawmapboundary()

plt.figure(1)
map = Basemap(projection='sinu',lon_0=0,resolution='c')
map.drawmapboundary(fill_color='aqua')

plt.show()

