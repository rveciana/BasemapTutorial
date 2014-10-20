Plotting data
=============

contour
--------

Creates a contour plot.

`contour(x, y, data) <http://matplotlib.org/basemap/api/basemap_api.html#mpl_toolkits.basemap.Basemap.contour>`_

* x and y are matrices of the same size as data, containing the positions of the elements in the map coordinates
* data is the matrix containing the data values to plot
* The default colormap is *jet*, but the argument *cmap* can be used to change the behaviour
* The argument tri = True makes the grid to be assumed as unstructured. See `this post <http://matplotlib.org/examples/pylab_examples/tricontour_vs_griddata.html>`_ to check the differences
* Other possible arguments are documented in the `matplotlib function docs <http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.contour>`__
* Labels can be added to the contour result, as in the :ref:`basic_contour` example at basic functions section

.. literalinclude:: ../code_examples/plotting_data/contour.py

.. image:: images/plotting_data/contour.png

contourf
--------

Creates a filled contour plot.

`contourf(x, y, data) <http://matplotlib.org/basemap/api/basemap_api.html#mpl_toolkits.basemap.Basemap.contourf>`_

* x and y are matrices of the same size as data, containing the positions of the elements in the map coordinates
* data is the matrix containing the data values to plot
* The default colormap is *jet*, but the argument *cmap* can be used to change the behaviour
* The argument tri = True makes the grid to be assumed as unstructured. See `this post <http://matplotlib.org/examples/pylab_examples/tricontour_vs_griddata.html>`_ to check the differences
* Other possible arguments are documented in the `matplotlib function docs <http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.contourf>`__

.. literalinclude:: ../code_examples/basic_functions/contourf.py
	:emphasize-lines: 22
.. image:: images/basic_functions/contourf.png



pcolor
------

The behaviour of this function is almost the same as in :ref:`pcolormesh`. A good explanation `here <http://thomas-cokelaer.info/blog/2014/05/matplotlib-difference-between-pcolor-pcolormesh-and-imshow/>`_

.. _pcolormesh:

pcolormesh
----------

Creates a pseudo-color plot

`pcolormesh(x, y, data, *args, **kwargs) <http://matplotlib.org/basemap/api/basemap_api.html#mpl_toolkits.basemap.Basemap.pcolormesh>`_

* x and y are matrices of the same size as data, containing the positions of the elements in the map coordinates
* data is the matrix containing the data values to plot
* The default colormap is *jet*, but the argument *cmap* can be used to change the behaviour
* Other possible arguments are documented in the `matplotlib function docs <http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.pcolormesh>`__

.. literalinclude:: ../code_examples/basic_functions/pcolormesh.py
	:emphasize-lines: 22
.. image:: images/basic_functions/pcolormesh.png

plot
----

Plots markers or lines on the map

The function has the following arguments:

`plot(x, y, *args, **kwargs) <http://matplotlib.org/basemap/api/basemap_api.html#mpl_toolkits.basemap.Basemap.plot>`_

* x and y can be either a float with the position of a marker in the projection units, or lists with the points form drawing a line
* If latlon keyword is set to True, x,y are intrepreted as longitude and latitude in degrees. Won't work in old *basemap* versions
* By default, the marker is a point. `This page explains all the options <http://matplotlib.org/api/markers_api.html>`_
* By default, the color is black (k). `This page explains all the color options <http://matplotlib.org/api/colors_api.html>`_

The first example shows a single point:

.. literalinclude:: ../code_examples/basic_functions/point.py
	:emphasize-lines: 11-13
.. image:: images/basic_functions/point.png

If the arguments are arrays, the output is a line (without markers in this case):

.. literalinclude:: ../code_examples/plotting_data/plot_line.py
	:emphasize-lines: 11-17
.. image:: images/plotting_data/plot_line.png

scatter
-------

Plot multiple markers on the map

`scatter(x, y, *args, **kwargs) <http://matplotlib.org/basemap/api/basemap_api.html#mpl_toolkits.basemap.Basemap.scatter>`_

* x and y is a list of points to add to the map as markers
* If latlon keyword is set to True, x,y are intrepreted as longitude and latitude in degrees. Won't work in old *basemap* versions
* By default, the marker is a point. `This page explains all the options <http://matplotlib.org/api/markers_api.html>`_
* By default, the color is black (k). `This page explains all the color options <http://matplotlib.org/api/colors_api.html>`_

.. literalinclude:: ../code_examples/basic_functions/scatter.py
	:emphasize-lines: 11-17
.. image:: images/basic_functions/scatter.png