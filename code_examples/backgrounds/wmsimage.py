from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

map = Basemap(llcrnrlon=8.35,llcrnrlat=41.225,urcrnrlon=10.01,urcrnrlat=43.108,
              projection='cyl', epsg=4326)

wms_server = "http://www.ga.gov.au/gis/services/topography/Australian_Topography/MapServer/WMSServer"
wms_server = "http://wms.geosignal.fr/metropole?"

map.wmsimage(wms_server, layers=["Communes", "Nationales", "Regions"], verbose=True)
plt.show()

