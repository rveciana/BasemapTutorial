from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

map = Basemap(llcrnrlon=-10.5,llcrnrlat=33,urcrnrlon=10.,urcrnrlat=46.,
             resolution='i', projection='cass', lat_0 = 39.5, lon_0 = 0.)

map.bluemarble()

map.drawcoastlines()

plt.show()