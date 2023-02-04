import rasterio
from shapely.geometry import box

from src.imgproc import reproject_raster


def intersect_rasters(raster1_path, raster2_path):
    """
    Calcula a interseção georreferenciada entre dois rasters de 1 ou 3 bandas.
    """

    ras1 = rasterio.open(raster1_path)
    ras2 = rasterio.open(raster2_path)

    if ras1.count != ras2.count:
        raise Exception("Número de bandas entre os dois rasters é diferente. ({} != {})".format(
            ras1.count, ras2.count))

    aux_ras = reproject_raster(ras2, ras1.crs)
    ras2.close()
    ras2 = aux_ras

    ext1 = box(*ras1.bounds)
    ext2 = box(*ras2.bounds)

    intersection = ext1.intersection(ext2)

    win1 = rasterio.windows.from_bounds(*intersection.bounds, ras1.transform)
    win2 = rasterio.windows.from_bounds(*intersection.bounds, ras2.transform)

    overlap_1 = ras1.read(window=win1)
    overlap_2 = ras2.read(window=win2)

    bands = ras1.count

    ras1.close()
    ras2.close()

    return (overlap_1, overlap_2, bands)
