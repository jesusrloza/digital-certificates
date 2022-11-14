#!/usr/bin/env python3
import os
from lib.transform_data import xlsx_to_csv
from lib.csv_list import csv_col_names

# Paths to the directories and files that are needed for the program to run
start = ".."
pathQR =    os.path.join(start, "qrcodes")
absPathQR = os.path.abspath(pathQR)
pathData = os.path.join(start, "data")
pathExcel = os.path.join(pathData, "participants.xlsx")
pathCSV =   os.path.join(pathData, "participants.csv")
pathSeparateCerts = os.path.join(start, "pdfs", "separate")

def check_env():
    '''check_env()
    
    1. It checks if the required directories exist, if not it creates them. 
    1. It also checks if the excel file exists, if not it prints an error message and exits. 
    1. If the excel file exists, creates csv file from it. 
    1. Finally, it checks if the csv file has all the required 
    columns, if not it prints an error message and exits. 
    
    If all the above checks pass, it prints a success message and exits.
    '''
    
    if not os.path.exists(pathQR): os.mkdir(pathQR)
    if not os.path.exists(pathData): os.mkdir(pathData)

    if not os.path.exists(pathExcel):
        print('Did not find: {}'.format(pathExcel))
        print('Without xlsx file process cannot continue')
        return 1

    print('Creating csv from xlsx')
    xlsx_to_csv(pathExcel, pathCSV, absPathQR)
    
    # Check required columns
    csv_columns = csv_col_names(pathCSV)
    required_columns = [
        'Global', 'Año', 'Foja', 'No.', 'Curso', 'Duración en horas',
        'Participante', 'Constancia', 'QR'
    ]
    
    # If not all required columns exist, print out message and exit
    if not all(el in csv_columns for el in required_columns):
        print("Missing a column from: {}.".format(
            ', '.join(required_columns)
        ))
        return 1

    print("Environment validated successfully, you can continue")
    return
