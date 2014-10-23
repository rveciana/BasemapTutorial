Background methods
==================

I'va called background methods those functions useful for drawing borders, lands, etc. to distinguish them from those aimed to draw user data.

drawcoastlines
--------------

Draws the coastlines.

The function has the following arguments:

`drawcoastlines(linewidth=1.0, linestyle='solid', color='k', antialiased=1, ax=None, zorder=None) <http://matplotlib.org/basemap/api/basemap_api.html#mpl_toolkits.basemap.Basemap.drawcoastlines>`_

* linewidth sets, of course, the line width in pixels
* linestyle sets the line type. By default is solid, but can be dashed, o rany matplotlib option
* color is k (black) by default. Follows also matplotlib conventions
* antialiased is true by default
* zorder sets the layer position. By default, the order is set by Basemap

.. literalinclude:: ../code_examples/first_map/first_map.py

.. image:: images/first_map/first_map.png

drawcountries
--------------

Draws the coastlines from the layer included with the library.

The function has the following arguments:

`drawcountries(linewidth=1.0, linestyle='solid', color='k', antialiased=1, ax=None, zorder=None) <http://matplotlib.org/basemap/api/basemap_api.html#mpl_toolkits.basemap.Basemap.drawcoastlines>`_

* linewidth sets, of course, the line width in pixels
* linestyle sets the line type. By default is solid, but can be dashed, o rany matplotlib option
* color is k (black) by default. Follows also matplotlib conventions
* antialiased is true by default
* zorder sets the layer position. By default, the order is set by Basemap

Note that:

* The resolution indicated when creating the :ref:`basemap` instance makes the layer to have a better or coarser resolution
* The coastline is in another function, and the country coasts are not considered coast, which makes necessary to combine the the moethod with others to get a good map

.. literalinclude:: ../code_examples/backgrounds/drawcountries.py
	:emphasize-lines: 10
	
.. image:: images/backgrounds/drawcountries.png

Without drawing the coastline, the result is a bit weird:

.. image:: images/backgrounds/drawcountries_alone.png

.. _drawmeridians:

drawmeridians
-------------

Draws the meridians on the map

`drawmeridians(meridians, color='k', linewidth=1.0, zorder=None, dashes=[1, 1], labels=[0, 0, 0, 0], labelstyle=None, fmt='%g', xoffset=None, yoffset=None, ax=None, latmax=None, **kwargs) <http://matplotlib.org/basemap/api/basemap_api.html#mpl_toolkits.basemap.Basemap.drawmeridians>`_

* meridians is a list with the longitudes to plot. This can be created with *range()* if the values are integers. If you need floats, *np.arange()* is a good option
* color sets the color of the line. `This page explains all the color options <http://matplotlib.org/api/colors_api.html>`_
* linewidth sets, of course, the line width in pixels
* zorder changes the position of the lines, to be able, fot instance, to make the land to cover the meridians, or the opposite
* Sets the dashing style. The first element is the number of pixels to draw, and the second, the number of pixels to skip
* labels change the positions where the labels are drawn. Setting the value to 1 makes the labels to be drawn at the selected edge of the map. The four positions are [left, right, top, bottom]

.. literalinclude:: ../code_examples/backgrounds/draw_meridians.py

.. image:: images/backgrounds/draw_meridians.png

This example shows the simplest way to use the function, using the Azimuthal equidistant projection. To see a more complex example, take a look at :ref:`drawparallels`

.. _drawparallels:

drawparallels
-------------

Draws the parallels on the map

`drawparallels(circles, color='k', linewidth=1.0, zorder=None, dashes=[1, 1], labels=[0, 0, 0, 0], labelstyle=None, fmt='%g', xoffset=None, yoffset=None, ax=None, latmax=None, **kwargs) <http://matplotlib.org/basemap/api/basemap_api.html#mpl_toolkits.basemap.Basemap.drawparallels>`_

* parallels is a list with the longitudes to plot. This can be created with *range()* if the values are integers. If you need floats, *np.arange()* is a good option
* color sets the color of the line. `This page explains all the color options <http://matplotlib.org/api/colors_api.html>`_
* linewidth sets, of course, the line width in pixels
* zorder changes the position of the lines, to be able, fot instance, to make the land to cover the parallels, or the opposite
* Sets the dashing style. The first element is the number of pixels to draw, and the second, the number of pixels to skip
* labels change the positions where the labels are drawn. Setting the value to 1 makes the labels to be drawn at the selected edge of the map. The four positions are [left, right, top, bottom]

.. literalinclude:: ../code_examples/backgrounds/draw_parallels.py

.. image:: images/backgrounds/draw_parallels.png

The example shows some avance functions, such as labeling or zorder, using the `polyconic projection <http://matplotlib.org/basemap/users/poly.html>`_. To see a simpler example, take a look ar :ref:`drawmeridians`
