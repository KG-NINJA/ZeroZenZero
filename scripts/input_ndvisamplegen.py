import os
os.makedirs("data/raw", exist_ok=True)
import numpy as np
import rasterio

arr = np.random.uniform(low=-1, high=1, size=(10, 10)).astype(np.float32)
with rasterio.open(
    "data/raw/input_ndvi.tif",
    'w',
    driver='GTiff',
    height=arr.shape[0],
    width=arr.shape[1],
    count=1,
    dtype=arr.dtype,
    crs='+proj=latlong',
    transform=rasterio.transform.from_origin(0, 0, 1, 1)
) as dst:
    dst.write(arr, 1)

print("Dummy NDVI data generated: data/raw/input_ndvi.tif")
