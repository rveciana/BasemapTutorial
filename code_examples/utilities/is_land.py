from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

map = Basemap(projection='aeqd', lon_0 = 10, lat_0 = 50, resolution='h')

x, y = map(0, 0)

print map.is_land(x, y)