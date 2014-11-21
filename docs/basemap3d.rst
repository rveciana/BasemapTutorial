Basemap in 3D
=============

Even though many people don't like them, maps with 3d elements can be created using basemap and the `matplotlib mplot3d <http://matplotlib.org/mpl_toolkits/mplot3d/>`_ toolkit.

Creating a basic map
--------------------

The most important thing to know when starting with 3d matplotlib plots is that the *Axes3D* class has to be used. 
To add geographical data to the map, the method *add_collection3d* will be used:

.. literalinclude:: ../code_examples/cookbook/plotting_3d_basic.py 

* The ax variable is in this example, an Axes3D instance. All the methods will be used from this instance, so they need to support 3D operations, which doesn't occur in many cases on the basemap methods
* The commented block shows how to rotate the resulting map so the view is better
* To draw lines, just use the add_collection3d method with the output of any of the basemap methods that return an matplotlib.patches.LineCollection object, such as drawcountries

.. figure:: images/cookbook/plotting_3d_basic.png
    :figclass: align-center

    Basic usage, the axis rotation is the one by default

.. figure:: images/cookbook/plotting_3d_basic2.png
    :figclass: align-center

    The axis rotation is set so the map is watched from the z axis, like when drawing it in 2D

Filling the polygons
--------------------

Unfortunately, the basemap :ref:`fillcontinents` method doesn't return an object supported by `add_collection3d <http://matplotlib.org/mpl_toolkits/mplot3d/api.html#mpl_toolkits.mplot3d.axes3d.Axes3D.add_collection3d>`_ (PolyCollection, LineColleciton, PatchCollection), but a lsit of `matplotlib.patches.Polygon <http://matplotlib.org/api/patches_api.html#matplotlib.patches.Polygon>`_ objects.
