Basemap utility functions
=========================

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