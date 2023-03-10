"""
[AUTOR]
    Pedro Thiago Cutrim dos Santos
    Github: @elheremes

[DESCRIÇÃO]
    Script responsável por realizar e salvar o janelamento
    das interseções de alta e baixa resolução dos rasters.
"""

from PIL import Image
import numpy as np

from src.imgproc import get_spatial_resolution, create_folder


def generate_image_slices(ar1, ar2, res1, res2, save_dir, lr_size=128):
    """
    Realiza o janelamento dos arrays numpy e salva em
    formato de imagens png, separando-os em alta resolução
    e baixa resolução através do fator calculado entre as
    resoluções espaciais de ambos rasters.

    [ARGUMENTOS]
        ar1: numpy array contendo os valores da interseção do
             primeiro raster.
        ar2: numpy array contendo os valores da interseção do
             segundo raster.
        res1: resolução espacial em inteiro do primeiro raster.
        res2: resolução espacial em inteiro do segundo raster.
        lr_size: resolução (lr_size x lr_size) da imagem de baixa
                 qualidade.
        save_dir: diretório onde serão salvos os resultados.
    """

    images_per_axis = int(ar1.shape[0] / lr_size)
    resolution_factor = int(res1 / res2)
    hr_size = lr_size * resolution_factor

    count_slice = 1

    create_folder(save_dir)
    create_folder(save_dir + "/lr")
    create_folder(save_dir + "/hr")

    for i in range(images_per_axis):
        for j in range(images_per_axis):
            slice1 = Image.fromarray(
                np.uint8(ar1[i*lr_size:(i+1)*lr_size, j*lr_size:(j+1)*lr_size]), 'L')

            slice2 = Image.fromarray(
                np.uint8(ar2[i*hr_size:(i+1)*hr_size, j*hr_size:(j+1)*hr_size]), 'L')

            slice1.save("{}/lr/slice_{}.png".format(save_dir, count_slice))
            slice2.save("{}/hr/slice_{}.png".format(save_dir, count_slice))

            count_slice = count_slice + 1
