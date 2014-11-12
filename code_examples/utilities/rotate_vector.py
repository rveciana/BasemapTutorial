from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np


fig=plt.figure(figsize=(9, 3))


map = Basemap(projection='sinu', 
              lat_0=0, lon_0=0)

lons = np.linspace(-180, 180, 10)
lats = np.linspace(-90, 90, 10)

lons, lats = np.meshgrid(lons, lats)

v10 = np.ones((lons.shape)) * 15
u10 = np.zeros((lons.shape))

u10_rot, v10_rot, x, y = map.rotate_vector(u10, v10, lons, lats, returnxy=True)

ax = fig.add_subplot(121)
ax.set_title('Without rotation')

map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='#cc9955', lake_color='aqua', zorder = 0)
map.drawcoastlines(color = '0.15')


map.barbs(x, y, u10, v10, 
    pivot='middle', barbcolor='#333333')

ax = fig.add_subplot(122)
ax.set_title('Rotated vectors')

map.drawmapboundary(fill_color='9999FF')
map.fillcontinents(color='#ddaa66', lake_color='9999FF', zorder = 0)
map.drawcoastlines(color = '0.15')

map.barbs(x, y, u10_rot, v10_rot, 
    pivot='middle', barbcolor='#ff7777')

plt.show()
