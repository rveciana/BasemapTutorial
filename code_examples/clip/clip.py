from mpl_toolkits.basemap import Basemap
from matplotlib.path import Path
from matplotlib.patches import PathPatch
import matplotlib.pyplot as plt
from osgeo import gdal
import numpy
import shapefile

fig = plt.figure()
ax = fig.add_subplot(111)

sf = shapefile.Reader("ne_10m_admin_0_countries")

for shape_rec in sf.shapeRecords():
    if shape_rec.record[3] == 'Andorra':
        vertices = []
        codes = []
        pts = shape_rec.shape.points
        prt = list(shape_rec.shape.parts) + [len(pts)]
        for i in range(len(prt) - 1):
            for j in range(prt[i], prt[i+1]):
                vertices.append((pts[j][0], pts[j][1]))
            codes += [Path.MOVETO]
            codes += [Path.LINETO] * (prt[i+1] - prt[i] -2)
            codes += [Path.CLOSEPOLY]
        clip = Path(vertices, codes)
        clip = PathPatch(clip, transform=ax.transData)


m = Basemap(llcrnrlon=1.4,
    llcrnrlat=42.4,
    urcrnrlon=1.77,
    urcrnrlat=42.7,
    resolution = None, 
    projection = 'cyl')

ds = gdal.Open('srtm_37_04.tif')
data = ds.ReadAsArray()

gt = ds.GetGeoTransform()
x = numpy.linspace(gt[0], gt[0] + gt[1] * data.shape[1], data.shape[1])
y = numpy.linspace(gt[3], gt[3] + gt[5] * data.shape[0], data.shape[0])

xx, yy = numpy.meshgrid(x, y)

cs = m.contourf(xx,yy,data,range(0, 3600, 200))

for contour in cs.collections:
        contour.set_clip_path(clip)

plt.show()
