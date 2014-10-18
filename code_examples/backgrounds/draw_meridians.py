from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

map = Basemap(projection='aeqd', 
              lon_0=0.0, lat_0=0,             
              width=25000000, height=25000000)

map.drawmeridians(range(0, 360, 20))

plt.show()