#!/usr/bin/env python3
import os 
from lib.env import pathSeparateCerts, pathCSV
from lib.csv_list import csv_to_list

def rename():
    '''
    Iterate through the list of files in the directory `pathSeparateCerts/` and
    rename them according to the list of new names in `new_names`

    :return: A list of dictionaries.
    '''
    
    # List of dictionaries that represent each row of the excel file
    rows = csv_to_list(pathCSV)

    # Creating a list of strings that will be the new names of the files
    new_names = [
        "{:04d}_C{}F{:03d}R{:03d}.pdf".format(
            int(row["Global"]),row["Año"],int(row["Foja"]),int(row["No."]))
        for row in rows
    ]

    # Createa list of files in the directory `pathSeparateCerts/` 
    # (`os.listir` does not return sorted results)
    pdfs = sorted(os.listdir(pathSeparateCerts))

    # Iterating through the two lists and renaming the files.
    for i in range(len(pdfs)):
        os.rename(
            os.path.join(pathSeparateCerts, pdfs[i]),
            os.path.join(pathSeparateCerts, new_names[i])
        )

rename()
