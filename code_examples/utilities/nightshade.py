from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from datetime import datetime

map = Basemap(projection='vandg',lon_0=0,resolution='c')

map.drawmapboundary(fill_color="#7777ff")
map.fillcontinents(color="#ddaa66",lake_color="#7777ff")

map.drawcoastlines()

map.nightshade(datetime.now(), delta=0.2)

plt.show()

