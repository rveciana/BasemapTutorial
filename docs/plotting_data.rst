Plotting data
=============

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