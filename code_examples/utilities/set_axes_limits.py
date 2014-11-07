from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
fig = plt.figure()

map = Basemap(projection='ortho', 
              lat_0=0, lon_0=0)

map.drawlsmask(land_color = "#ddaa66", 
               ocean_color="#7777ff",
               resolution = 'c')


x1, y1 = map(-60, -30)
x2, y2 = map(0, 0)
x3, y3 = map(45, 45)

plt.plot([x1, x2, x3], [y1, y2, y3], color='k', linestyle='-', linewidth=2)

ax1 = fig.add_axes([0.1, 0., 0.15, 0.15])
ax1.set_xticks([])
ax1.set_yticks([])

ax1.plot([x1, x2, x3], [y1, y2, y3], color='k', linestyle='-', linewidth=2)

map.set_axes_limits(ax=ax1)

ax2 = fig.add_axes([0.3, 0., 0.15, 0.15])
ax2.set_xticks([])
ax2.set_yticks([])

ax2.plot([x1, x2, x3], [y1, y2, y3], color='k', linestyle='-', linewidth=2)

ax3 = fig.add_axes([0.5, 0., 0.15, 0.15])
ax3.set_xticks([])
ax3.set_yticks([])

map.plot([x1, x2, x3], [y1, y2, y3], color='k', linestyle='-', linewidth=2, ax=ax3)

plt.show()
