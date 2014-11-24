from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from osgeo import gdal
from numpy import linspace
from numpy import meshgrid
from os.path import exists
from matplotlib.colors import LinearSegmentedColormap


def readColorTable(color_file):
    '''
    The method for reading the color file.
    '''
    color_table = {}
    if exists(color_file) is False:
        raise Exception("Color file " + color_file + " does not exist")
    fp = open(color_file, "r")
    for line in fp:
        if line.find('#') == -1 and line.find('/') == -1:
            entry = line.split()
            if len(entry) == 5:
                alpha = int(entry[4])
            else:
                alpha=255
            color_table[eval(entry[0])]=[int(entry[1]),int(entry[2]),int(entry[3]),alpha]
    fp.close()

    return color_table

readColorTable("../sample_files/colorfile.clr")
cmap1 = LinearSegmentedColormap.from_list("my_colormap", ((0, 0, 0), (1, 1, 1)), N=200, gamma=1.0)

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

map.contourf(xx, yy, data, cmap=cmap1)

#plt.show()