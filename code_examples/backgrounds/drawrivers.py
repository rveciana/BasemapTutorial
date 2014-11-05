from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt


map = Basemap(llcrnrlon=-93.,llcrnrlat=40.,urcrnrlon=-75.,urcrnrlat=50.,
             resolution='i', projection='tmerc', lat_0 = 40., lon_0 = -80)

map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='#ddaa66', lake_color='#0000ff')

map.drawcountries()
map.drawrivers(color='#0000ff')

plt.show()

