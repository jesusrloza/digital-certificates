#!/usr/bin/env python3
import pandas as pd
import os

def xlsx_to_csv(Excel, CSV, absPathQR):
    ''' xlsx_to_csv(Excel, CSV, absPathQR)
    
    It writes a csv file with an extra column for the QR codes path
    
    :param Excel: the path to the excel file
    :param CSV: the name of the csv file to be created
    :param absPathQR: absolute path to the folder containing the QR codes
    '''

    # We're interested in the Windows equivalent of the absolute path
    pathQrWSL = absPathQR.replace('/mnt/c/', 'C:/')

    # Build dataframe from xlsx
    df = pd.DataFrame(pd.read_excel(Excel))

    # Build a list of strings from the 'Global' column
    qr_Column = [
        os.path.join('{}'.format(pathQrWSL), '{:04d}.png'.format(int(g))).replace('/', '\\\\')
        for g in df['Global']
    ]  
    #   when writing csvfiles, the '\' character is escaped
    #   for that reason we write 4 of them


    # Include list as a new column
    df['QR'] = qr_Column

    # Write csv file
    df.to_csv(CSV)
    return

