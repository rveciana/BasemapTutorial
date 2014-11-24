.. _inset_locator:

Inset locators
--------------
Insert locator is a cool class that zooms a part of the plot and draws it on the plot itself, showing the zoomed zone.

.. literalinclude:: ../code_examples/cookbook/locator.py 

* The base scatter and map is a regular :ref:`scatter` plot
* The inset locator is created using the method zoomed_inset_axes
    * ax is the axis to be zoomed by the inset locator
    * 7 is a zoom level (to be overwritten later)
    * loc is the position of the inset locator (upper right in this case)
* set_xlim and set_ylim change the zone to cover by the inset locator. Since we are working with the cyl projection, longitudes and latitudes can be used directly, without any transformation
* xticks and yticks are set to false to delete the new axis labels, which are not necessary on a map
* A new map is created using the zoomed limits and the axis created by zoomed_inset_axes. Now, all the methods will be using this new zoomed map, matching the correct zone
* The map is drawn again using the new basemap instance, to plot the zoomed zone
* mark_inset draws the lines showing the zoomed zone

.. image:: images/cookbook/locator.png