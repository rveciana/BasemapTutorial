from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt


map = Basemap(width=12000000,height=9000000,
            rsphere=(6378137.00,6356752.3142),\
            resolution='l',area_thresh=1000.,projection='lcc',\
            lat_1=45.,lat_2=55,lat_0=50,lon_0=-107.)

map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='#ddaa66', lake_color='aqua')

map.drawcountries()
map.drawstates(color='0.5')

plt.show()


