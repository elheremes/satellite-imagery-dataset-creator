"""
[AUTOR]
    Pedro Thiago Cutrim dos Santos
    Github: @elheremes

[DESCRIÇÃO]
    Controlador responsável pela comunicação dos
    processos de backend e a interface.

    Este script faz a gestão da fila de processos,
    salvamento de arquivos e criação de threads para
    o programa.
"""


import numpy as np
from PIL import Image

from PySide2.QtCore import QThreadPool

from src.imgproc import (
    intersect_rasters,
    reproject_raster,
    get_spatial_resolution,
    generate_image_slices
)

from src.controller import (
    Worker
)


class ProcessController:
    """
    Classe para o controlador de processos.

    Gerencia a fila de processos enviados pelo usuário,
    escolhe qual processo deve ser executado e salva os
    aruivos de resultado.

    [ATRIBUTOS]
        busy: booleano que informa se o controlador está
              executando um processo ou não.
        queue: lista com a fila de processos não ainda
               executados.
        thread_pool: QThreadPool para criação de threads de
                     processo para cada elemento.
    """

    def __init__(self):
        self.busy = False
        self.queue = []
        self.thread_pool = QThreadPool()

    def append_to_queue(self, process_item):
        self.queue.append(process_item)
        self.check_queue()

    def check_queue(self):
        if not self.busy and len(self.queue) > 0:
            self.busy = True
            worker = Worker(self.process_video)

            worker.signals.progress.connect(self.queue[0].update_progress)

            self.thread_pool.start(worker)

    def register_end_process(self):
        self.queue.pop(0)
        self.busy = False
        self.check_queue()

    def process_video(self, progress_callback):
        process = self.queue[0]

        process.disable_trash_btn()

        process.start_processing()

        res1 = get_spatial_resolution(process.raster1_name)
        res2 = get_spatial_resolution(process.raster2_name)

        overlap_1, overlap_2, bands = intersect_rasters(
            process.raster1_name, process.raster2_name)

        progress_callback.emit(40)

        if bands == 1:
            overlap_1 = overlap_1.reshape(
                (overlap_1.shape[1], overlap_1.shape[2]))
            overlap_2 = overlap_2.reshape(
                (overlap_2.shape[1], overlap_2.shape[2]))

            overlap_1 = np.asarray(Image.fromarray(overlap_1 * 255), 'L')
            overlap_2 = np.asarray(Image.fromarray(overlap_2 * 255), 'L')
        elif bands == 3:
            overlap_1 = overlap_1.reshape(
                (overlap_1.shape[1], overlap_1.shape[2], overlap_1.shape[0]))
            overlap_2 = overlap_2.reshape(
                (overlap_2.shape[1], overlap_2.shape[2], overlap_2.shape[0]))

            overlap_1 = np.asarray(Image.fromarray(overlap_1 * 255), 'RGB')
            overlap_2 = np.asarray(Image.fromarray(overlap_2 * 255), 'RGB')

        progress_callback.emit(50)

        generate_image_slices(overlap_1, overlap_2, res1, res2,
                              lr_size=128, save_dir=process.folder)

        process.update_progress(100)

        self.register_end_process()

        process.end_processing(None)

        process.enable_trash_btn()
