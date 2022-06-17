# rsFMRI-Numerical-Data-Code
The code used to view the k-means clustering of the numerical data from the first blogpost.

The original dataset used can be found here ( https://dataverse.harvard.edu/dataset.xhtml?persistentId=doi:10.7910/DVN/29352 ); however, the data will need to be preprocessed with a tool such as CONN Toolbox, as we have done.

Annotated explanations of the code can be found in the commented-out sections of main.py.

Each csv file corresponds to a right (R) or left (L) hippocampi of Alzheimer's Disease (AD) or healthy control (HC) patients. 

You may need to place 2 of the 4 csv files in a separate folder, then place that folder in a larger directory in which main.py is included for the concatenation of csv files to successfully form a dataframe.

You may have to delete DegreeEfficiencyClusters.csv so that the code will process a new csv file of the same name.

You can replace 'Degree' and/or 'GlobalEfficiency' with other variables to observe other plots of the data. If you find anything of interest, let us know!
