===================
Interpolate3D
===================

The following project is a Python script that is used to modify an excel document. It takes value of H (wave height) and T (wave period) from a predetermined matrix of probabilities of occurrence (percentages, normalized to 100) and interpolates the values for values not in the matrix.

This process can be generalized to n dimensional joint density data. This project was the motivation for ``py

Install Dependencies
-------
.. code-block:: python

    pip install openpyxl

In terminal to run the program. This is the library used to read from and write to Excel documents. In the program's current form, the Excel document must have the following form:

==============  ==============
:math:`H`       :math:`T`     
==============  ==============
:math:`H_1`     :math:`T_1`   
:math:`H_2`     :math:`T_2`   
:math:`\ldots` 	:math:`\ldots`
:math:`\ldots`  :math:`\ldots`
:math:`H_n`     :math:`T_n`   
==============  ==============
Run
-------
.. code-block:: python

    python interpolate.py HsTe.txt ht_matrix.xlsx

This will print the values of the percentages and write these values to the third column of the Excel document.

==============  ==============  ============================
:math:`H`       :math:`T`       :math:`\mathbb{P}[H, T]` 
==============  ==============  ============================ 
:math:`H_1`     :math:`T_1`     :math:`\mathbb{P}[H_1, T_1]`
:math:`H_2`     :math:`T_2`     :math:`\mathbb{P}[H_2, T_2]`
:math:`\ldots` 	:math:`\ldots`  :math:`\ldots`
:math:`\ldots`  :math:`\ldots`  :math:`\ldots`
:math:`H_n`     :math:`T_n`     :math:`\mathbb{P}[H_n, T_n]`
==============  ==============  ============================

These files have been attached in the tests and can be used for demo purposes. Note that you can substitute any Excel document for the demo one as long as it holds the format specified above.

Happy interpolating!