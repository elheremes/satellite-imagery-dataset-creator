"""
[AUTOR]
    Pedro Thiago Cutrim dos Santos
    Github: @elheremes

[DESCRIÇÃO]
    Script responsável por conter funções auxiliares para
    utlização de ambos backend e frontend do programa.
"""

import rasterio
import os

from rasterio.warp import (
    calculate_default_transform,
    reproject,
    Resampling
)


def reproject_raster(raster, dst_crs):
    """
    Reprojeta o CRS original do raster para o CRS informado.

    [ARGUMENTOS]
        raster: DatasetReader do raster carregado pelo rasterio.
        dst_crs: string informando o sistema de coordenadas desejado.

    [RETORNO]
        Retorna um DatasetReader convertido para o CRS desejado.
    """

    transform, width, height = calculate_default_transform(
        raster.crs, dst_crs, raster.width, raster.height, *raster.bounds)

    kwargs = raster.meta.copy()

    kwargs.update({
        'crs': dst_crs,
        'transform': transform,
        'width': width,
        'height': height
    })

    with rasterio.open('/home/pedropeter/Documentos/teste.tif', 'w', **kwargs) as dst:
        for i in range(1, raster.count + 1):
            reproject(
                source=rasterio.band(raster, i),
                destination=rasterio.band(dst, i),
                src_transform=raster.transform,
                src_crs=raster.crs,
                dst_transform=transform,
                dst_crs=dst_crs,
                resampling=Resampling.nearest)

    raster.close()

    return rasterio.open('/home/pedropeter/Documentos/teste.tif')


def get_spatial_resolution(raster_path):
    """
    Obtém a resolução espacial do raster informado.

    [ARGUMENTOS]
        raster_path: caminho para o arquivo raster.

    [RETORNO]
        Retorna em inteiro a resolução espacial do
        raster (em metros).
    """

    with rasterio.open(raster_path) as raster:
        return int(raster.res[0])


def create_folder(path):
    """
    Verifica se a pasta existe e, caso não, realiza
    a criação do diretório.

    [ARGUMENTOS]
        path: caminho do diretório a ser checado ou
              criado.
    """

    if not os.path.exists(path):
        os.makedirs(path)
