.. _basemap:

Basemap
-------
Any map created with the Basemap library must start with the creation of a Basemap instance

`mpl_toolkits.basemap.Basemap(llcrnrlon=None, llcrnrlat=None, urcrnrlon=None, urcrnrlat=None, llcrnrx=None, llcrnry=None, urcrnrx=None, urcrnry=None, width=None, height=None, projection='cyl', resolution='c', area_thresh=None, rsphere=6370997.0, ellps=None, lat_ts=None, lat_1=None, lat_2=None, lat_0=None, lon_0=None, lon_1=None, lon_2=None, o_lon_p=None, o_lat_p=None, k_0=None, no_rot=False, suppress_ticks=True, satellite_height=35786000, boundinglat=None, fix_aspect=True, anchor='C', celestial=False, round=False, epsg=None, ax=None) <http://matplotlib.org/basemap/api/basemap_api.html#mpl_toolkits.basemap.Basemap>`_

The class constructor has many possible arguments, and all of them are optional:

* resolution: The resolution of the included coastlines, lakes, and so on. The options are c (crude, the default), l (low), i (intermediate), h (high), f (full) or None.
	* None option is a good one if a Shapefile will be used instead of the included files, since no data must be loaded and the performance rises a lot.
* area_thresh: The threshold under what no coast line or lake will be drawn. Default 10000,1000,100,10,1 for resolution c, l, i, h, f.
* rsphere: Radius of the sphere to be used in the projections. Default is 6370997 meters. If a sequence is given, the first two elements are taken as the radius of the ellipsoid.
* ellps: An ellipsoid name, such as 'WGS84'. The allowed values are defined at pyproj.pj_ellps
* suppress_ticks: Suppress automatic drawing of axis ticks and labels in map projection coordinates
* fix_aspect: Fix aspect ratio of plot to match aspect ratio of map projection region (default True)
* anchor: The place in the plot where the map is anchored. Default is C, which means map is centered. Allowed values are C, SW, S, SE, E, NE, N, NW, and W
* celestial: Use the astronomical conventions for longitude (i.e. negative longitudes to the east of 0). Default False. Implies resolution=None
* ax: set default axes instance

Passing the bounding box
^^^^^^^^^^^^^^^^^^^^^^^^
The following arguments are used to set the extent of the map.

To see some examples and explanations about setting the bounding box, take a look at the :ref:`extension` section.

The first way to set the extent is by defining the map bounding box in geographical coordinates:

========= ===========
Argument  Description
========= ===========
llcrnrlon The lower left corner geographical longitude
llcrnrlat The lower left corner geographical latitude
urcrnrlon The upper right corner geographical longitude
urcrnrlat The upper right corner geographical latitude
========= ===========

An other option is setting the bounding box, but using the projected units:

========= ===========
Argument  Description
========= ===========
llcrnrx   The lower left corner x coordinate, in the projection units
llcrnry   The lower left corner y coordinate, in the projection units
urcrnrx   The upper right corner x coordinate, in the projection units
urcrnry   The upper right corner y coordinate, in the projection units
========= ===========

Finally, the last option is to set the bounding box giving the center point in geographical coordinates, and the width and height of the domain in the projection units

========= ===========
Argument  Description
========= ===========
width     The width of the map in the projection units
height    The height of the map in the projection units
lon_0     The longitude of the center of the map
lat_0     The latitude  of the center of the map
========= ===========

.. _converting_units:

Using the Basemap instance to convert units
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The basemap instance can be used to calculate positions on the map and the inverse operation, converting positions on the map to geographical coordinates.

.. code-block:: python

	from mpl_toolkits.basemap import Basemap
	import matplotlib.pyplot as plt

	map = Basemap(projection='aeqd', lon_0 = 10, lat_0 = 50)

	print map(10, 50)
	print map(20015077.3712, 20015077.3712, inverse=True)

The output will be:

	(20015077.3712, 20015077.3712)
	(10.000000000000002, 50.000000000000014)

When inverse is False, which is its default value, the input values are a longitude and a latitude, and the output, the position of this point in the map coordinates. When *inverse* is set to true, the behavior is the opposite, the arguments are an x and y positions in the map coordinates, and the output is the position of this point in geographical coordinates.

Basemap object fields
^^^^^^^^^^^^^^^^^^^^^
When a Basemap object is created, has some fields with data:

* Some of them contain the polygons with the resolution set with the resolution parameter. They are all matplotlib Polygon objects:
	* landpolygons
	* lakepolygons
	* boundarylons
	* coastpolygons
	* coastpolygontypes
	* coastsegs
* Other fields give information about the used projection
	* proj4string A string that can be used with proj4 (or GDAL) to have the used projection definition
	* projection The code of the used projection, as indicated in the projection argument
	* projparams A dict with the projection parameters. The ones passed and the ones put by default by Basemap
	* rmajor The semi-major axis of the ellipsoid used with the projection
	* rminor The semi-minor axis of the ellipsoid used with the projection
	* xmax, ymax, xmin, ymin The bounding box in the projection units
	* anchor The point on the map where the axis coordinates start. By default is the center of the map, but can be changed to any corner or side
	* celestial indicates if the longitudes west of Greenwich are negative
