from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from osgeo import gdal
from numpy import linspace
from numpy import meshgrid
from os.path import exists
from matplotlib.colors import LinearSegmentedColormap


def read_color_table(color_file):
    '''
    The method for reading the color file.
    '''
    colors = []
    levels = []
    if exists(color_file) is False:
        raise Exception("Color file " + color_file + " does not exist")
    fp = open(color_file, "r")
    for line in fp:
        if line.find('#') == -1 and line.find('/') == -1:
            entry = line.split()
            levels.append(eval(entry[0]))
            colors.append((int(entry[1])/255.,int(entry[2])/255.,int(entry[3])/255.))
       
    fp.close()

    cmap = LinearSegmentedColormap.from_list("my_colormap",colors, N=len(levels), gamma=1.0)
    
    return levels, cmap

levels, cmap = read_color_table("../sample_files/colorfile.clr")

map = Basemap(projection='tmerc', 
              lat_0=0, lon_0=3,
              llcrnrlon=1.819757266426611, 
              llcrnrlat=41.583851612359275, 
              urcrnrlon=1.841589961763497, 
              urcrnrlat=41.598674173123)

ds = gdal.Open("../sample_files/dem.tiff")
data = ds.ReadAsArray()

x = linspace(0, map.urcrnrx, data.shape[1])
y = linspace(0, map.urcrnry, data.shape[0])
xx, yy = meshgrid(x, y)

map.contourf(xx, yy, data, levels, cmap=cmap)

plt.show()