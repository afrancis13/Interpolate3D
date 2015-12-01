The following project is a Python script that is used to modify an excel document. It takes value of H and T from a predetermined matrix of probabilities of occurrence (percentages, normalized to 100) and interpolates the values for values not in the matrix.

You will need to type the command:

pip install openpyxl

In terminal to run the program. This is the library used to read from and write to Excel documents.In the program's current form, the Excel document must have the following form:

Header for H      Header for T
H1				  T1
.  				  .
.				  .
.                 . 

To run:

python interpolate.py HsTe.txt ht_matrix.xlsx

This will print the values of the percentages and write these values to the third column of the Excel document.

These files have been attached and can be used for demo purposes. Note that you can substitute any Excel document for the demo one as long as it holds the format specified above.

Happy interpolating!