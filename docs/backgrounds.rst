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