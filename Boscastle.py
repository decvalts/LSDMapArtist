from osgeo import gdal
from mayavi import mlab
import numpy as np
import numpy.ma as ma

ds = gdal.Open('/mnt/SCRATCH/Dev/ExampleTopoDatasets/indian_creek.bil')
#ds = gdal.Open('/run/media/dav/SHETLAND/Analyses/HydrogeomorphPaper/peak_flood_maps/boscastle/peak_flood/Elevations0.asc')

ds_waterd = gdal.Open('/run/media/dav/SHETLAND/Analyses/HydrogeomorphPaper/peak_flood_maps/boscastle/peak_flood/WaterDepths2400_GRIDDED_HYDRO.asc')
data_waterd = ds_waterd.ReadAsArray()

data = ds.ReadAsArray()
ndv = -9999 
#masked_data = ma.masked_where(data == ndv, data)

nodata_mask = data == ndv
data[nodata_mask] = np.nan

nowater_mask = data_waterd == 0.0
data_waterd[nowater_mask] = np.nan
 
mlab.figure(size=(640, 800), bgcolor=(0.16, 0.28, 0.46))

mlab.surf(data, warp_scale=0.4, colormap='gist_gray')
mlab.surf(data_waterd, warp_scale=0.4, colormap='Blues')
mlab.show()

