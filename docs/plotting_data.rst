Plotting data
=============

.. _annotate:

annotate
--------

Creates text with an arrow indicating the point of interest. To create a :ref:`text` without an arrow, look at the :ref:`text` section.

`annotate(*args, **kwargs) <http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.annotate>`_

* The text method does not belong to Basemap, but directly to matplotlib, so it must be called from the plot or axe instance
* The first argument is the text string
* xy is a list with the x and y coordinates of the point pointed by the arrow. This will be interprete depending on the xycoords argument
* xycoords indicates the type of coordinates used in xy:
    * data means the coordinates are the ones used by the data (the projection coordinates)
    * offset points means an offset in points
    * axes pixels indicates pixels from the lower left corner of the axes
    * The other options are at the `annotation docs <http://matplotlib.org/api/text_api.html#matplotlib.text.Annotation>`_
* xytext a list with the x and y coordinates of the text, an the beginning of the arrow
* textcoords indicates the type of coordinates used in xytext, with the same options as in xycoords
* arrowprops this optional argument sets the arrow properties, as explained in the `Line2D <matplotlib.org/api/lines_api.html#matplotlib.lines.Line2D>`_ docs
* color the color of the text. `This page explains all the color options <http://matplotlib.org/api/colors_api.html>`_

.. literalinclude:: ../code_examples/plotting_data/annotate.py

.. image:: images/plotting_data/annotate.png

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

streamplot
----------

Plots streamlines from a vectorial field. 

`streamplot(x, y, u, v, *args, **kwargs) <http://matplotlib.org/basemap/api/basemap_api.html#mpl_toolkits.basemap.Basemap.streamplot>`_

* x and y are matrices of the same size as *u* and *v* data, containing the positions of the elements in the map coordinates. 
	* `As the docs explain <http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.streamplot>`_, x and y must be evenly spaced. This mean that when the original values come from a different projection, the data matrix must be re-projected, and the x and y matrices re-calculated, as you can see in the example.
	* To calculate an evenly spaced grid, the method :ref:`makegrid` can be used. It's better to use the *returnxy=True* attribute to get the grid in the map projection units.  
* u and v are the x and y velocities. The dimensions must be the same as *x* and *y*
* color can set the same color for the streamlines, or change depending of the data:
	* If the value is a scalar, all the streamlines will have the indicated color, depending on the colormap
	* If the value is an array of the same size as data (the module of the wind in the example), the color will change according to it, using the color map
* cmap sets the `color map <http://matplotlib.org/api/colors_api.html>`_
* linewidth sets the width of the streamlines in a similar way as the color
	* If is a scalar, all the streamlines have the indicated width
	* If is an array, the streamline width will change according to the values of the array
* density sets the closeness of streamlines to plot. a 1 value means the domains is divided in 30x30, with only one streamline crossing each sector. If a list with two elements is passed, the x and y densities are set to different values
* norm  Normalizes the scale to set luminance data
* arrowsize scales thearrow size
* arrowstyle stes the arrow style. The docs are at `FancyArrowPatch <http://matplotlib.org/1.3.0/api/artist_api.html#matplotlib.patches.FancyArrowPatch>`_
* minlength sets the minimum length of the streamline in the map coordinates
* The best documentation for the function is not `the one in Basemap <http://matplotlib.org/basemap/api/basemap_api.html#mpl_toolkits.basemap.Basemap.streamplot>`_, but in `matplotlib <http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.streamplot>`_

.. literalinclude:: ../code_examples/plotting_data/streamplot.py
	:emphasize-lines: 15-19
.. image:: images/plotting_data/streamplot.png

.. note:: The matplotlib and basemap versions must be quite new to use this function. From Ubuntu 14.04, for instance you need to use *sudo pip install --upgrade matplotlib*. Do then the same with Basemap

.. _text:

text
----

Plots a text on the map

`text(x, y, s, fontdict=None, withdash=False, **kwargs) <http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.text>`_

* The text method does not belong to Basemap, but directly to matplotlib, so it must be called from the plot or axe instance
* x and y are the coordinates in the map projection. Arrays of coordinates are not accepted, so to add multiple labels, call the metho multiple times
* s is the text string
* withdash creates a text with a dash when set to true
* fontdict can be used to group the text properties

The text can have many many options such as:

* fontsize the font size
* fontweight font wheight, such as bold
* ha horitzontal align, like center, left or right
* va vertical align, like center, top or bottom
* color the color. `This page explains all the color options <http://matplotlib.org/api/colors_api.html>`_
* bbox creates a box around the text: bbox=dict(facecolor='red', alpha=0.5)

.. literalinclude:: ../code_examples/plotting_data/text.py

.. image:: images/plotting_data/text.png

To draw a text label with an arrow, use :ref:`annotate`.