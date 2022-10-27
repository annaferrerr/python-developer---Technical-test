#!/usr/bin/env python
# coding: utf-8

# ## Technical Test  - Python Developer

# In[20]:


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import json
import PIL


# In[21]:


import rasterio as rio
ds=rio.open("S2L2A_2022-06-09.tiff")
from rasterio.plot import show
show(ds.read((4,3,2))/4000)


# In[22]:


#1. An /attributes endpoint that reads the image and returns the following attributes as a JSON object: 
#image size (width and height), number of bands, 
#coordinate reference system and georeferenced bounding box.


# In[23]:


#1. An /attributes endpoint that reads the image and returns the following attributes as a JSON object: 
#image size (width and height), number of bands, 
#coordinate reference system and georeferenced bounding box.
from PIL import Image
im = Image.open("S2L2A_2022-06-09.tiff")
bands = Image.Image.getbands(im)
w, h =im.size
coord_system=(0,0) #cartesian
#print("Multiband image", bands)
print("width: ",w,"\nheight: ", h, "\nMultiband image ", bands, "\nCoordinate system:" , coord_system)
im.show()


# In[24]:


#2. A /thumbnail endpoint that returns a PNG thumbnail of the image.
size=(100,100)
im.thumbnail(size)
im.show()
im.save('thumb_image.png')


# In[25]:


#3. An /ndvi endpoint that computes an NDVI on the image and returns the result as a PNG.
    ## Band 1 - Blue, Band 2 - Green, Band 3 - Red, Band 4 - Near Infrared
with rio.open("S2L2A_2022-06-09.tiff") as src:
    band_red = src.read(3)# Get red band
    band_nir = src.read(4) # Get NIR band

    ndvi = (band_nir.astype(float) - band_red.astype(float)) / (band_nir + band_red)# Calculate NDVI
    
ndvi[ndvi > 1] = np.nan
ndvi[ndvi < -1] = np.nan

# Plot raster
plt.imshow(ndvi)
plt.title("NDVI")
plt.show()
# Show raster values
print("Raster values:\n", ndvi)


# In[ ]:




