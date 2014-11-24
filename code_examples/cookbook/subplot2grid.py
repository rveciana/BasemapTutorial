import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.path import Path
import matplotlib.patches as patches

fig = plt.figure()

ax1 = plt.subplot2grid((2,2), (0,0))
ax2 = plt.subplot2grid((2,2), (1,0))
ax3 = plt.subplot2grid((2,2), (0,1), rowspan=2)

map1 = Basemap(projection='ortho', lon_0 = 0, lat_0 = 40, ax=ax1)

map1.drawmapboundary(fill_color='#9999FF')
map1.fillcontinents(color='#ddaa66',lake_color='#9999FF')
map1.drawcoastlines()

map2 = Basemap(projection='cyl', llcrnrlon=-15,llcrnrlat=30,urcrnrlon=15.,urcrnrlat=50., resolution='i', ax=ax2)

map2.drawmapboundary(fill_color='#9999FF')
map2.fillcontinents(color='#ddaa66',lake_color='#9999FF')
map2.drawcoastlines()


map3 = Basemap(llcrnrlon= -1., llcrnrlat=37.5, urcrnrlon=4.5, urcrnrlat=44.5,
             resolution='i', projection='tmerc', lat_0 = 39.5, lon_0 = 3, ax=ax3)

map3.drawmapboundary(fill_color='#9999FF')
map3.fillcontinents(color='#ddaa66',lake_color='#9999FF')
map3.drawcoastlines()


#Drawing the zoom rectangles:

lbx1, lby1 = map1(*map2(map2.xmin, map2.ymin, inverse= True))
ltx1, lty1 = map1(*map2(map2.xmin, map2.ymax, inverse= True))
rtx1, rty1 = map1(*map2(map2.xmax, map2.ymax, inverse= True))
rbx1, rby1 = map1(*map2(map2.xmax, map2.ymin, inverse= True))

verts1 = [
    (lbx1, lby1), # left, bottom
    (ltx1, lty1), # left, top
    (rtx1, rty1), # right, top
    (rbx1, rby1), # right, bottom
    (lbx1, lby1), # ignored
    ]

codes2 = [Path.MOVETO,
         Path.LINETO,
         Path.LINETO,
         Path.LINETO,
         Path.CLOSEPOLY,
         ]

path = Path(verts1, codes2)
patch = patches.PathPatch(path, facecolor='r', lw=2)
ax1.add_patch(patch)

lbx2, lby2 = map2(*map3(map3.xmin, map3.ymin, inverse= True))
ltx2, lty2 = map2(*map3(map3.xmin, map3.ymax, inverse= True))
rtx2, rty2 = map2(*map3(map3.xmax, map3.ymax, inverse= True))
rbx2, rby2 = map2(*map3(map3.xmax, map3.ymin, inverse= True))

verts2 = [
    (lbx2, lby2), # left, bottom
    (ltx2, lty2), # left, top
    (rtx2, rty2), # right, top
    (rbx2, rby2), # right, bottom
    (lbx2, lby2), # ignored
    ]

codes2 = [Path.MOVETO,
         Path.LINETO,
         Path.LINETO,
         Path.LINETO,
         Path.CLOSEPOLY,
         ]

path = Path(verts2, codes2)
patch = patches.PathPatch(path, facecolor='r', lw=2)
ax2.add_patch(patch)

plt.show()