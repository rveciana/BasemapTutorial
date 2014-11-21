import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.basemap import Basemap
from matplotlib.collections import PatchCollection
from matplotlib.collections import PolyCollection
import numpy as np

map = Basemap()

fig = plt.figure()
ax = Axes3D(fig)
ax.set_axis_off()

ax.azim = 270
ax.elev = 50
ax.dist = 8

ax.add_collection3d(map.drawcoastlines(linewidth=0.25))
ax.add_collection3d(map.drawcountries(linewidth=0.35))

polys = []
for polygon in map.landpolygons:
    polys.append(polygon.get_coords())


lc = PolyCollection(polys, edgecolor='black',
                    facecolor='#DDDDDD', closed=False)

ax.add_collection3d(lc)

lons = np.array([0, 2, -30])
lats = np.array([0, 41, 30])
values = np.array([5, 10, 15])

colors = ['r', 'g', 'b']
x, y = map(lons, lats)

ax.bar3d(x, y, np.zeros(len(x)), 5, 5, values, color= colors, alpha=0.8)

ax.set_zlabel('Height')

plt.show()