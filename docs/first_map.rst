Drawing the first map
=======================
Let's create a the simplest map:

.. literalinclude:: ../code_examples/first_map/first_map.py


#. The first two lines include the Basemap library and matplotlib. Both are necessary
#. The map is created using the Basemap class, which has many options. Without passing any option, the map has the `Plate Carrée projection <http://en.wikipedia.org/wiki/Equirectangular_projection>`_ centered at longitude and latitude = 0
#. After setting the map, we can draw what we want. In this case, the coast lines layer, which comes already with the library, using the method *drawcoastlines()*
#. Finally, the map has to be shown or saved. The methods from mathplotlib are used. In this example, *plt.show()* opens a window to explore the result. *plt.savefig('file_name')* would save the map into an image.

.. image:: images/first_map/first_map.png

Changing the projection is easy, just add the *projection* argument and *lat_0* and *lon_0* to the *Basemap* contructor.

Even with the new projection, the map is still a bit poor, so let's fill the oceans and continents with some colors The methods *fillcontinents()* and *drawmapboundary()* will do it:

.. literalinclude:: ../code_examples/first_map/first_map_fill.py
	:emphasize-lines: 4-10
.. image:: images/first_map/first_map_fill.png
