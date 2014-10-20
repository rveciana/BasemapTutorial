Basemap utility functions
=========================

.. _makegrid:

makegrid 
--------

makegrid method creates an arbitrary grid of equally spaced points in the map projection

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
