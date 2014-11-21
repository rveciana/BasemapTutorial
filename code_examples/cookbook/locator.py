from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np

map = Basemap(projection='cyl', 
              lat_0=0, lon_0=0)

map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='coral',lake_color='aqua', zorder=0)
map.drawcoastlines()

#http://www.cdc.gov/vhf/ebola/outbreaks/2014-west-africa/case-counts.html
lons = np.array([-13.7, -10.8, -13.2, -17.3, -3.6, -84.3, -8., 7.5])
lats = np.array([9.6, 6.3, 8.5, 14.7, 40.4, 33.7, 12.6, 9.8])
cases = np.array([1612, 2553, 4523, 1, 19, 1, 4, 2])
deaths = np.array([1142, 2836, 1169, 0, 8, 0, 1, 4])

colors = np.random.rand(len(deaths))
x, y = map(lons, lats)

map.scatter(x, y, s=cases, c=colors, alpha=0.5)

print cases, np.log(cases), colors
plt.show()