Basemap utility functions
=========================

.. _makegrid:

makegrid 
--------

makegrid method creates an arbitrary grid of equally spaced points in the map projection

colorbar
--------

Draws the color legend at one of the edges of the map. The use is almost the same as in matplotlib colorbar

`colorbar(mappable=None, location='right', size='5%', pad='2%', fig=None, ax=None, **kwargs) <http://matplotlib.org/basemap/api/basemap_api.html#mpl_toolkits.basemap.Basemap.colorbar>`_

* mappable is the most important argument. Is the field on the map to be explained with the colorscale. It can be a contourf, a pcolormesh, contour, etc. If the value is None, the last drawn field is represented
* location sets the border of the map where the color scale is drawn. Can be top, right, left or bottom
* size sets the width of the color bar, in % of the parent axe
* pad sets the separation between the axes and the color bar, also in % of the parent axe
* fig is the figure the colorbar is associated with

Most of the matplotlib.colorbar arguments will work too, such as label

The colorbar method returns an object, which has some interesting methods too:

* add_lines adds to the color bar, the lines from an other field (look at the example to see how does it work)
* set_ticks changes the positions of the ticks and labels on the color bar

.. literalinclude:: ../code_examples/utilities/colorbar.py

.. image:: images/utilities/colorbar.png 

* A colormesh and a contour fields are plotted, to be able to use some advenced colorbar attributes
* The first colorbar (line 27), shows the default use of the colorbar. The pcolormesh is passed as the argument, to force the method to draw this one instead of the contour field
* The second colorbar uses some more arguments
	* The position is changed to bottom
	* A label is set
	* The method add_lines is used with the contour field, so the colorbar shows the pcolormesh and contour field legends at once
	* The ticks are set at random positions, to show how to change them
	
To see an example with logarithmic scales, take a look at the :ref:`hexbin` example
 
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

gcpoints
--------

Calculates n points along a great circle given two coordinates

`gcpoints(lon1, lat1, lon2, lat2, npoints) <http://matplotlib.org/basemap/api/basemap_api.html#mpl_toolkits.basemap.Basemap.gcpoints>`_

* lon1 and lat1 are the geographical coordinates of the initial point
* lon2 and lat2 are the geographical coordinates of the final point
* npoints is the number of points to calculate

.. note:: To draw a great circle, the :ref:`greatcircle` function it may be easier to use. This function is useful to get the points values, or draw cases when greatcircle fails because of edges problems

.. literalinclude:: ../code_examples/utilities/gcpoints.py
	:emphasize-lines: 10
	
.. image:: images/utilities/gcpoints.png 

.. _greatcircle:

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

is_land
-------

Returns *True* if the indicated point is on the land, and *False* if on an ocean or lake

`is_land(xpt, ypt) <http://matplotlib.org/basemap/api/basemap_api.html#mpl_toolkits.basemap.Basemap.is_land>`_

* xpt and ypt are the point coordinates where the land/water has to be calculated. 
	* The coordinates must be in the map coordinates
	* The resolution indicated in the Basemap constructor must not be None
	* The indicated resolution polygon will be used to calculated if the point is on a land zone, so the results change depending on that
* No arrays of coordinates are allowed, so the query must be done point by point
* `There is an alternative way to calculate this for many points <http://stackoverflow.com/questions/13796315/plot-only-on-continent-in-matplotlib/13811775#13811775>`_ using the landpolygons attribute and the matplotlib PATH.contains_points method

.. literalinclude:: ../code_examples/utilities/is_land.py

The alternative way, which accepts multiple points and, in fact could be used with any polygon get from a shapefile (See :ref:`fillingpolygons`)

.. literalinclude:: ../code_examples/utilities/is_land_alternative.py

* locations is a numpy array containing numpy arrays with the projected points
* The PATH objects are calculated for each of the polygons 
* For each PATH, all the points are evaluated using contains_points. The result is casted into a numpy array so can be added with the previous evaluations. If one of the polygons contains the point, the result element will be true

nightshade
----------

Draws the regions of the map which are dark at the specified date

`nightshade(date, color='k', delta=0.25, alpha=0.5, ax=None, zorder=2) <http://matplotlib.org/basemap/api/basemap_api.html#mpl_toolkits.basemap.Basemap.nightshade>`_

* date is a `datetime.datetime <https://docs.python.org/2/library/datetime.html>`_ object
* color is the color of the drawn shadow
* delta is the resolution to which the shadow zone is calculated. By default is 0.25, and small values fail easily
* alpha is the transparency value
* zorder can change the layer vertical position

The example shows the current dark zones in the `van der Grinten Projection <http://matplotlib.org/basemap/users/vandg.html>`_:

.. literalinclude:: ../code_examples/utilities/nightshade.py

.. image:: images/utilities/nightshade.png 


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
	
Tissot's indicatrices for the Mercator projection:

.. image:: images/utilities/tissot_mercator.png
	
Tissot's indicatrices for the Albers Equal Area projection:

.. image:: images/utilities/tissot_albers_equal_area.png

