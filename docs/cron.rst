Running scripts from the crontab
================================
The following script will fail when is run from the crontab:

.. code-block:: python

	from mpl_toolkits.basemap import Basemap
	import matplotlib.pyplot as plt
	
	map = Basemap()
	map.drawcoastlines()
	plt.savefig('out.png')
	
The error will be something like
	
	RuntimeError: could not open displayX
	
This is because *matplotlib.pyplot* assumes that a, active X server is opened to be able to open the window with the graph when *plt.show()* is called.

To avoid the problem, simply add importing pyplot:

.. code-block:: python

	import matplotlib as mpl
	mpl.use('Agg')
	
So the code will work even from the *cron* when written as:

.. code-block:: python

	from mpl_toolkits.basemap import Basemap
	import matplotlib as mpl
	mpl.use('Agg')
	import matplotlib.pyplot as plt
	
	map = Basemap()
	map.drawcoastlines()
	plt.savefig('out.png')
	
There is a `post at StackOverflow <http://stackoverflow.com/questions/4931376/generating-matplotlib-graphs-without-a-running-x-server>`_ explaining it better