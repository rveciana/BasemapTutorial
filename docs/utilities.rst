Basemap utility functions
=========================

.. _makegrid:

makegrid 
--------

makegrid method creates an arbitrary grid of equally spaced points in the map projection

drawmapscale
------------

Draws the scale of the map at the indicated position

`drawmapscale(lon, lat, lon0, lat0, length, barstyle='simple', units='km', fontsize=9, yoffset=None, labelstyle='simple', fontcolor='k', fillcolor1='w', fillcolor2='k', ax=None, format='%d', zorder=None) <http://matplotlib.org/basemap/api/basemap_api.html#mpl_toolkits.basemap.Basemap.drawmapscale>`_

* lon and lat indicate the position of the scale on the map. The fact that the geographical coordinates must be used is a problem, since there's no possibility to put the scale outside the map
* lon0 lat0 indicate the location where the scale is calculated
* length is the number of kilometers to represent in the scale
* barstyle can be 'simple' or 'fancy', and changes the scalebar style. Both styles are represented in the example
* units indicates the units to represent in the scale, kilometers by default
* fontsize changes the font size of the units drawn on the scale bar
* fontcolor sets the font color of the units drawn on the scale bar
* yoffset controls the height of the scalebar. By default is 0.02 times the height of the map. It doesn't seem to work properly in all the versions
* fillcolor1 and fillcolor2 set the colors of the bar at the scale bar when the style is 'fancy'
* format sets the number format on the scale bar

.. note:: The projection *cyl* (lat/lon), which is the default, can't use this method. More informatino `here <http://sourceforge.net/p/matplotlib/mailman/message/23863531/>`_. 

.. literalinclude:: ../code_examples/utilities/drawmapscale.py

.. image:: images/utilities/drawmapscale.png 

greatcircle
-----------

`A great circle <http://en.wikipedia.org/wiki/Great_circle>`_ is the maximum circle that can be drawn that passes through two points in a sphere (excepting when the points are the antipodes)

`drawgreatcircle(lon1, lat1, lon2, lat2, del_s=100.0, **kwargs) <http://matplotlib.org/basemap/api/basemap_api.html#mpl_toolkits.basemap.Basemap.drawgreatcircle>`_

* lon1 and lat1 are the longitude and latitude of the starting point
* lon2 and lat2 are the longitude and latitude of the ending point
* del_s is the number of kilometers that separe each point of the great circle. Defaults to 100
* linewidth argument sets the width of the line
* color sets the color of the line. `This page explains all the color options <http://matplotlib.org/api/colors_api.html>`_

.. note:: If the circle gets cut by the edges of the map, i.e. starts at longitude -179 and ends at 179, the method can't handle it properly

.. literalinclude:: ../code_examples/utilities/drawgreatcircle_mercator.py

When using mercator projection, the meridians and parallels are straight lines, but the great circles usually are not

.. image:: images/utilities/drawgreatcircle_mercator.png

.. literalinclude:: ../code_examples/utilities/drawgreatcircle_gnomonic.py

The gnomonic projection makes the great circles to be a straight line in any direction:

.. image:: images/utilities/drawgreatcircle_gnomonic.png 

tissot
------

`Tissot's indicatrix <http://en.wikipedia.org/wiki/Tissot%27s_indicatrix>`_, or Tissot's ellipse of distortion is the representation of a circle in a map, showing how the projection distorts it. Usually, many of them are represented to show how the distortion varies with the position.

The function has the following arguments:

`tissot(lon_0, lat_0, radius_deg, npts, ax=None, **kwargs) <http://matplotlib.org/basemap/api/basemap_api.html#mpl_toolkits.basemap.Basemap.tissot>`_

* lon_0 and lat_0 indicate the position of the Tissot's ellipse
* radius_deg indicates the radius of the polygon
* npts Is the number of vertices of the polygon that will be used to approximate the ellipse. A higher npts will make better approached ellipses

.. note:: If the circle gets cut by the edges of the map, i.e. starts at longitude -179 and ends at 179, the method can't handle it properly

.. literalinclude:: ../code_examples/utilities/tissot.py
    :emphasize-lines: 13
    
Tissot's indicatrices for the Orthographic projection:             

.. image:: images/utilities/tissot_orthographic.png 
	:scale: 50 %
	
Tissot's indicatrices for the Mercator projection:

.. image:: images/utilities/tissot_mercator.png
	:scale: 50 %
	
Tissot's indicatrices for the Albers Equal Area projection:

.. image:: images/utilities/tissot_albers_equal_area.png
	:scale: 50 %
