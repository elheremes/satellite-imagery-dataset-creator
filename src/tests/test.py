"""
[AUTOR]
    Pedro Thiago Cutrim dos Santos
    Github: @elheremes

[DESCRIÇÃO]
    Script responsável pelos testes de unidade do
    programa.
"""

import unittest
import os


class TestFilesQuantity(unittest.TestCase):
    def test_results_size(self):
        """
        Este método realiza o teste verificando a quantidade
        dos resultados de processamento salvos na pasta 'tmp'
        do programa.

        A verificação consiste em verificar se o número de
        arquivos das pastas 'lr' e 'hr' coincidem, caso não
        então o teste retorna um erro.
        """

        results_lr = []
        results_hr = []

        if os.path.isfile('tmp'):
            ids = [int(name)
                   for name in os.listdir("tmp/") if os.path.isdir(os.path.join("tmp/", name))]

            for i in ids:
                aux = len([name for name in os.listdir("tmp/{}/lr/".format(i))
                          if os.path.isdir(os.path.join("tmp/{}/lr/".format(i), name))])

                results_lr.append(aux)

                aux = len([name for name in os.listdir("tmp/{}/hr/".format(i))
                          if os.path.isdir(os.path.join("tmp/{}/hr/".format(i), name))])

                results_hr.append(aux)

        self.assertEqual(results_lr, results_hr)


class TestFilesNames(unittest.TestCase):
    def test_results_names(self):
        """
        Este método realiza o teste verificando se o nome dos
        pares 'lr' e 'hr' coincidem em todos os itens de processamento.
        """

        results_lr = []
        results_hr = []

        if os.path.isfile('tmp'):
            ids = [int(name)
                   for name in os.listdir("tmp/") if os.path.isdir(os.path.join("tmp/", name))]

            for i in ids:
                aux = [name for name in os.listdir("tmp/{}/lr/".format(i))
                       if os.path.isdir(os.path.join("tmp/{}/lr/".format(i), name))]

                results_lr.append(aux)

                aux = [name for name in os.listdir("tmp/{}/hr/".format(i))
                       if os.path.isdir(os.path.join("tmp/{}/hr/".format(i), name))]

                results_hr.append(aux)

        self.assertEqual(results_lr, results_hr)


if __name__ == '__main__':
    unittest.main()
