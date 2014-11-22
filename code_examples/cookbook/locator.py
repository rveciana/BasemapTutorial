from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

map = Basemap(projection='cyl', 
              lat_0=0, lon_0=0)

map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='coral',lake_color='aqua', zorder=0)
map.drawcoastlines()

#http://www.cdc.gov/vhf/ebola/outbreaks/2014-west-africa/case-counts.html,  22 Nov 2014
lons = np.array([-13.7, -10.8, -13.2, -96.8, -7.99, 7.5, -17.3, -3.7])
lats = np.array([9.6, 6.3, 8.5, 32.7, 12.5, 8.9, 14.7, 40.39])
cases = np.array([1971, 7069, 6073, 4, 6, 20, 1, 1])
deaths = np.array([1192, 2964, 1250, 1, 5, 8, 0, 0])
places = np.array(['Guinea', 'Liberia', 'Sierra Leone','United States', 'Mali', 'Nigeria', 'Senegal', 'Spain'])


colors = np.random.rand(len(deaths))
x, y = map(lons, lats)

map.scatter(x, y, s=cases, c=colors, alpha=0.5)

print cases, np.log(cases), colors
plt.show()