import os
import unittest

from openpyxl import load_workbook


class TestInterpolater(unittest.TestCase):

    def test_interpolater(self):
        help_text = os.system('python interpolate.py tests/HsTe.txt, tests/ht_matrix.xlsx -h')
        expected_help_text = ''
        self.assertEqual(help_text, expected_help_text)

        os.system('python interpolate.py tests/HsTe.txt tests/ht_matrix.xlsx')

        workbook = load_workbook(filename='tests/ht_matrix.xlsx')

        for worksheet in workbook:
            observed_column = worksheet.columns[2]
            observed_interpolated_values = []
            for cell in observed_column:
                cell_value = cell.value
                observed_interpolated_values.append(cell_value)

        expected_interpolated_values = [
            u'Percent',
            1.0649999999999995,
            0.9254999999999993,
            0.002100000000000003,
            3.5359999999999996,
            0.4849999999999998,
            0.0125,
            5.56,
            0.6937499999999999,
            0.020000000000000004,
            2.9289999999999985,
            0.7780000000000001,
            0.08825000000000001,
            0.25259999999999977,
            0.03199999999999998,
            0
        ]

        self.assertEqual(observed_interpolated_values, expected_interpolated_values)

        os.system('python interpolate.py tests/HsTe.txt, tests/ht_matrix.xlsx -c')

        self.assertEqual(len(worksheet.columns), 2)
