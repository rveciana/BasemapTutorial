The sample files for the examples where used for the [8as Jornadas Sig Libre](http://www.sigte.udg.edu/jornadassiglibre/), at the workshop [Introduction to Python for geospatial uses](https://github.com/rveciana/introduccion-python-geoespacial), and are courtesy of [Servei Metrorològic de Catalunya](http://www.meteo.cat) and [Institut Cartogràfic de Catalunya](http://www.icc.es/)

- **lightnings.shp** Lighning strokes of the day 17/11/2013 from the [SMC](http://www.meteo.cat)'s [network](http://www20.gencat.cat/portal/site/meteocat/menuitem.0733ee5bfae8638c5c121577b0c0e1a0/?vgnextoid=9a14c95252b67210VgnVCM1000008d0c1e0aRCRD&vgnextchannel=9a14c95252b67210VgnVCM1000008d0c1e0aRCRD&vgnextfmt=default)
- **comarques.shp** Catalan *comarques* or regions
- **dem.tiff** Digital Elevation Model at 5 meters of resolution for the zone of Montserrat, downloaded from[vissir, by ICC](http://www.icc.cat/vissir/)

- **by.png** is the Creative Commons Attribution logo, [taken from their web page](https://creativecommons.org/about/downloads)

The file **wrf.tiff** is a converted version from the [original WRF in NetCDF format from the UNIDATA site](http://www.unidata.ucar.edu/software/netcdf/examples/files.html). The original file is large, about 76MB, so I took only a part of it to show some examples. To generate it, i looked at the metadata file, and executed:

    gdal_translate -b 2 'NETCDF:"wrfout_v2_Lambert.nc":XLONG' lon.tiff
    gdal_translate -b 2 'NETCDF:"wrfout_v2_Lambert.nc":XLAT' lat.tiff
    gdal_translate -b 2 'NETCDF:"wrfout_v2_Lambert.nc":T2' t2.tiff
    gdal_translate -b 2 'NETCDF:"wrfout_v2_Lambert.nc":U10' u10.tiff
    gdal_translate -b 2 'NETCDF:"wrfout_v2_Lambert.nc":V10' v10.tiff
    gdal_merge.py -separate -o wrf.tiff u10.tiff v10.tiff t2.tiff lon.tiff lat.tiff

    gdal_edit.py -a_ullr 415262.44023 1030630.87528 2605262.44023 -769369.12472 -a_srs "+lon_0=-98.0 +R=6370997.0 +proj=lcc +units=m +lat_2=60.0 +lat_1=30.0 +lat_0=34.83158" wrf.tiff

    python

    from osgeo import gdal
    ds = gdal.Open('wrf.tiff')
    band = ds.GetRasterBand(1)
    band.SetMetadataItem("var","u10")
    band = ds.GetRasterBand(2)
    band.SetMetadataItem("var","v10")
    band = ds.GetRasterBand(3)
    band.SetMetadataItem("var","t2")
    band = ds.GetRasterBand(4)
    band.SetMetadataItem("var","lon")
    band = ds.GetRasterBand(5)
    band.SetMetadataItem("var","lat")
    ds = None

The file Ebola.py has the information of the 2014 ebola cases, taken from the web http://www.cdc.gov/vhf/ebola/outbreaks/2014-west-africa/case-counts.html the  22th November 2014