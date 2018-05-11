************************************
NASA Global Temperature Measurements
************************************



.. contents::
    :local:


About the data
==============

Source landing page: https://climate.nasa.gov/vital-signs/global-temperature/

Source data file: http://climate.nasa.gov/system/internal_resources/details/original/647_Global_Temperature_Data_File.txt


Data transformations
====================


Original data
-------------

Stashed data file: `datastash/originals/647_Global_Temperature_Data_File.txt <_static/projects/nasa-global-temps/datastash/originals/647_Global_Temperature_Data_File.txt>`_


.. code-block:: text

    1880    -0.19   -0.11
    1881    -0.1    -0.14
    1882    -0.1    -0.17
    1883    -0.19   -0.21
    1884    -0.28   -0.24



Parsed data
-----------

.. Parsed data file: :doc:`./datastash/parsed/nasa_global_temps.csv`


.. csv-table:: Parsed data
   :header: year,annual_mean,lowess_smoothed

    1880,-0.19,-0.11
    1881,-0.1,-0.14
    1882,-0.1,-0.17
    1951,-0.07,-0.08
    1952,0.01,-0.08
    1953,0.07,-0.08
    1954,-0.15,-0.07
    2014,0.73,0.77
    2015,0.86,0.83
    2016,0.99,0.89
    2017,0.9,0.95





