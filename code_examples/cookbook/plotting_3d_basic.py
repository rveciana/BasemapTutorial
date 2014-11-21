import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.basemap import Basemap

map = Basemap()

fig = plt.figure()
ax = Axes3D(fig)

'''
ax.azim = 270
ax.elev = 90
ax.dist = 5
'''

ax.add_collection3d(map.drawcoastlines(linewidth=0.25))
ax.add_collection3d(map.drawcountries(linewidth=0.35))

plt.show()