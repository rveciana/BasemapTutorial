from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
fig = plt.figure()

map = Basemap(projection='ortho', 
              lat_0=0, lon_0=0)

map.drawlsmask(land_color = "#ddaa66", 
               ocean_color="#7777ff",
               resolution = 'l')

x0, y0 = map(1., 31.)
x1, y1 = map(15., 39.)

plt.imshow(plt.imread('../sample_files/by.png'),  extent = (x0, x1, y0, y1))
        
axicon = fig.add_axes([0.1, 0., 0.15, 0.15])
axicon.imshow(plt.imread('../sample_files/by.png'), origin = 'upper')
axicon.set_xticks([])
axicon.set_yticks([])

plt.show()
