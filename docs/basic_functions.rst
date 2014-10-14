Basic functions
===============

Drawing a point in a map
------------------------

Drawing a point in a map is usually done using the `plot method <http://matplotlib.org/basemap/api/basemap_api.html#mpl_toolkits.basemap.Basemap.plot>`_:

.. literalinclude:: ../code_examples/basic_functions/point.py
	:emphasize-lines: 11-13
.. image:: images/basic_functions/point.png

* Use the Basemap instance to calculate the position of the point in the map coordinates when you have the longitude and latitude of the point
* The *plot* method needs the x and y position in the map coordinates, the marker and the color
	* By default, the marker is a point. `This page explains all the options <http://matplotlib.org/api/markers_api.html>`_
	* By default, the color is black (k). `This page explains all the color options <http://matplotlib.org/api/colors_api.html>`_
	
If you have more than one point, you may prefer the `scatter method <http://matplotlib.org/basemap/api/basemap_api.html#mpl_toolkits.basemap.Basemap.scatter>`_. Passing an array of point into the plot method creates a line connecting them, which may be interesting, but is not a point cloud:

.. literalinclude:: ../code_examples/basic_functions/scatter.py
	:emphasize-lines: 11-16
.. image:: images/basic_functions/scatter.png

* Remember that calling the *Basemap* instance can be done with lists, so the coordinate transformation is done at once
* The format options in the *scatter* method are the same as in plot

Plotting raster data
--------------------

