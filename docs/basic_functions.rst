Basic functions
===============

Drawing a point in a map
------------------------

Drawing a point in a map is usually done using the `plot method <http://matplotlib.org/basemap/api/basemap_api.html#mpl_toolkits.basemap.Basemap.plot>`_:

.. literalinclude:: ../code_examples/basic_functions/point.py
	:emphasize-lines: 11-13
.. image:: images/basic_functions/point.png

* Use the Basemap instance to calculate the position of the point in the map coordinates when you have the longitude and latitude of the point
	* If latlon keyword is set to True, x,y are intrepreted as longitude and latitude in degrees. Won't work in old *basemap* versions
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

There are two main methods for plotting a raster, *pcolor*, that creates a pseudocolor plot, and *contour/contourf*, that plots contour lines or filled contour lines (isobands).

.. literalinclude:: ../code_examples/basic_functions/contourf.py
	
.. image:: images/basic_functions/contourf.png

* The map is created with the same extension of the raster file, to make things easier.
* Before plotting the contour, two matrices have to be created, containing the positions of the x and y coordinates for each point in the data matrix.
	* `linspace <http://docs.scipy.org/doc/numpy/reference/generated/numpy.linspace.html>`_ is a numpy function that creates an array from an initial value to an end value with n elements. In this case, the map coordinates go from 0 to *map.urcrnrx* or *map.urcrnry*, and have the same size that the data array *data.shape[1]* and *data.shape[0]*
	* `meshgrid <http://docs.scipy.org/doc/numpy/reference/generated/numpy.meshgrid.html>`_ is a numpy function that take two arrays and create a matrix with them. This is what we need, since the *x* coordinates repeat in every column, and the *y* in every line
* The contourf method will take the *x*, *y* and *data* matrices and plot them in the default *colormap*, called jet

 pcolormesh:
	 