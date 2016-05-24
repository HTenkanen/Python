"""
This script is for testing that all the required python modules are working. Prints out the results of the test.
"""


# Lists for succeeded and failed modules
succeed = []
failed = []

# Numpy
try:
    import numpy as np
    succeed.append('numpy')
except:
    failed.append('numpy')

# Pandas
try:
    import pandas as pd
    succeed.append('pandas')
except:
    failed.append('pandas')

# Scipy
try:
    import scipy
    succeed.append('scipy')
except:
    failed.append('scipy')

# Matplotlib
try:
    import matplotlib
    succeed.append('matplotlib')
except:
    failed.append('matplotlib')

# Bokeh
try:
    import bokeh
    succeed.append('bokeh')
except:
    failed.append('bokeh')

# GDAL
try:
    import gdal
    succeed.append('gdal')
except:
    failed.append('gdal')

# Fiona
try:
    import fiona
    succeed.append('fiona')
except:
    failed.append('fiona')

# Shapely
try:
    import shapely
    succeed.append('shapely')
except:
    failed.append('shapely')

# Pyproj
try:
    import pyproj
    succeed.append('pyproj')
except:
    failed.append('pyproj')

# Psycopg2
try:
    import psycopg2
    succeed.append('psycopg2')
except:
    failed.append('psycopg2')

# Descartes
try:
    import descartes
    succeed.append('descartes')
except:
    failed.append('descartes')

# Geopandas
try:
    import geopandas as gpd
    succeed.append('geopandas')
except:
    failed.append('geopandas')

# Print the results
if len(failed) == 0:
    print("All the modules are properly installed.\nThe installed modules (excluding their dependencies) are:\n%s" % "\n".join(succeed))
else:
    print("Some of the modules weren't properly installed.\nIncorrectly installed modules are:\n%s\n\nCorrectly installed modules are:\n%s" %
          ("\n".join(failed), "\n".join(succeed)))
