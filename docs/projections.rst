Managing projections
=====================

All maps must have a projection. The projection and its features are all assigned when the object *Basemap* is created.
The way to do it is quite different from other libraries (i.e. GDAL), so understanding this point is very important for working with Basemap.

projection
----------

The projection argument sets the map projection to be used:

.. literalinclude:: ../code_examples/projections/cyl.py
    :emphasize-lines: 4
.. image:: images/projections/cyl.png

The default value is *cyl*, or `Cylindrical Equidistant projection <http://en.wikipedia.org/wiki/Equirectangular_projection>`_, also known as *Equirectangular projection* or *Plate Carrée*

Many projections require extra arguments:

.. literalinclude:: ../code_examples/projections/aeqd.py
    :emphasize-lines: 4
.. image:: images/projections/aeqd.png

The map has now an equidistant projection centered at longitude = 10 and laitude = 50, which is over Europe. Some projections require more parameters, described in `each projection page at the manual <http://matplotlib.org/basemap/users/mapsetup.html>`_.

All the examples until now take the whole globe. Drawing only a region can be done with two methods:

* Passing the width and height:

* Passing the bounding box:

