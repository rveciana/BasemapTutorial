#Idea taken from this post at StackOverflow: http://stackoverflow.com/questions/13796315/plot-only-on-continent-in-matplotlib/13811775#13811775
#I've re-written it to work with modern matplotlib versions

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from matplotlib.path import Path
import numpy as np

map = Basemap(projection='aeqd', lon_0 = 10, lat_0 = 50, resolution='h')

lons = [0., 0., 16., 76.]
lats = [0., 41., 19., 51.]

x, y = map(lons, lats)
locations = np.c_[x, y]

polygons = [Path(p.boundary) for p in map.landpolygons]

result = np.zeros(len(locations), dtype=bool) 

for polygon in polygons:
    result += np.array(polygon.contains_points(locations))

print result


