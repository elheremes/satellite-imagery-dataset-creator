import sys
from PySide2.QtWidgets import QApplication

from src.styles import app_styles
from src.interface import MainWindow
from src.imgproc import intersect_rasters, reproject_raster, get_spatial_resolution, generate_image_slices


def main(args):
    root = QApplication(args)

    app = MainWindow()
    app.show()

    root.setStyleSheet(app_styles)
    sys.exit(root.exec_())


if __name__ == '__main__':
    main(sys.argv)

    # raster1_path = "/home/pedropeter/Documentos/PUC/Dissertação/Satellite_Imagens/Landsat_8/LC09_L1TP_228065_20221120_20221120_02_T1_B1.TIF"
    # raster2_path = "/home/pedropeter/Documentos/PUC/Dissertação/Satellite_Imagens/Sentinel_2/S2A_MSIL1C_20221210T140711_N0509_R110_T21MWN_20221210T155008.SAFE/GRANULE/L1C_T21MWN_A039003_20221210T140708/IMG_DATA/T21MWN_20221210T140711_B02.jp2"

    # res1 = get_spatial_resolution(raster1_path)
    # res2 = get_spatial_resolution(raster2_path)

    # print(res1, res2)

    # overlap_1, overlap_2, bands = intersect_rasters(raster1_path, raster2_path)

    # from PIL import Image
    # import numpy as np

    # if bands == 1:
    #     overlap_1 = overlap_1.reshape((overlap_1.shape[1], overlap_1.shape[2]))
    #     overlap_2 = overlap_2.reshape((overlap_2.shape[1], overlap_2.shape[2]))

    #     overlap_1 = np.asarray(Image.fromarray(overlap_1 * 255), 'L')
    #     overlap_2 = np.asarray(Image.fromarray(overlap_2 * 255), 'L')

    # elif bands == 3:
    #     overlap_1 = overlap_1.reshape(
    #         (overlap_1.shape[1], overlap_1.shape[2], overlap_1.shape[0]))
    #     overlap_2 = overlap_2.reshape(
    #         (overlap_2.shape[1], overlap_2.shape[2], overlap_2.shape[0]))

    # generate_image_slices(overlap_1, overlap_2, res1, res2,
    #                       lr_size=128, save_dir='/home/pedropeter/Documentos/tmp')
