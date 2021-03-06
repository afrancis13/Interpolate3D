===================
Interpolate3D
===================
.. image:: https://travis-ci.org/afrancis13/Interpolate3D.svg?branch=master
    :target: https://travis-ci.org/afrancis13/Interpolate3D

The following project is a Python script that is used to modify an excel document. It takes value of H (wave height) and T (wave period) from a predetermined matrix of probabilities of occurrence (percentages, normalized to 100) and interpolates the values for values not in the matrix.

This process can be generalized to n dimensional joint density data. This project was the motivation for an upcoming project, ``py-interpolate``.

CalWave
------------
This project was a small part of a semester working with CalWave at UC Berkeley. The more complete picture of my research on energy analytics can be seen in the document CalWave2015.pdf, which is attached to this repository.

Requirements
------------
* openpyxl_ 1.8.5+
* matplotlib_ 1.4.3+

In terminal to run the program. This is the library used to read from and write to Excel documents. In the program's current form, the Excel document must have the following form:

.. image:: media/firstchart.png
   :height: 100px
   :width: 200 px
   :scale: 50 %
   :alt: alternate text
   :align: center

Run
-------
.. code-block:: python

    python interpolate.py density_matrix values_to_interpolate [-c] [-p] [-h]

See the tests for the formats of these documents.

This will print the values of the percentages and write these values to the third column of the Excel document.

.. image:: media/secondchart.png
   :height: 100px
   :width: 200 px
   :scale: 50 %
   :alt: alternate text
   :align: center

An image displaying the joint densities from the matrix (blue) and those interpolated from this data matrix (red) is seen below.

.. image:: media/Interpolate3D.png
   :height: 100px
   :width: 200 px
   :scale: 50 %
   :alt: alternate text
   :align: center

These files have been attached in the tests and can be used for demo purposes. Note that you can substitute any Excel document for the demo one as long as it holds the format specified above.

Happy interpolating!

.. _openpyxl: https://openpyxl.readthedocs.org/en/default/
.. _matplotlib: http://matplotlib.org/index.html