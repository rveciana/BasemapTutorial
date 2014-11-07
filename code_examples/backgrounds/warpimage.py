from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import Image

map = Basemap(projection='ortho', 
              lat_0=0, lon_0=0)


tmpdir = '/tmp'

size = [600, 300]
im = Image.open("../sample_files/by.png")

im2 = im.resize(size, Image.ANTIALIAS)
im2.save(tmpdir+'/resized.png', "PNG")

map.warpimage(tmpdir+'/resized.png')

map.drawcoastlines()

plt.show()