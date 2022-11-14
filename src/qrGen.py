#!/usr/bin/env python3
import sys, subprocess
from lib.csv_list import csv_to_list
from lib.env import check_env, pathCSV, pathQR

def generateQR():
    # Checks if the files needed to run the program are present
    if check_env():
        print("It's imposible to continue")
        sys.exit()

    # Reads CSV file and creates a list of dictionaries
    rows = csv_to_list(pathCSV)

    # Iterating over the rows of the CSV file and creating a QR code for each row
    for row in rows:
        # Cleanup unique IDs that start with an apostrophe
        if "'" in row['Constancia']: row['Constancia'] = row['Constancia'][1:]
        
        # Four digit name assignation for `qrcode-file.png`
        qrname = "{:04d}".format(int(row['Global']))

        
        # determine if time unit is singular or plural
        if '1.0' in row['Duración en horas']:
            row["Duración en horas"] = int(row["Duración en horas"])
            hr_hrs = 'hora'        
        else:
            hr_hrs = 'horas'

        # Define encoded text by using variables from each column
        qrstring = (
            "° Dirección de Profesionalización, SFA Michoacán {} | Foja {} - {} ({} {}) | Participante: {} | ID: {}".format(
                row['Año'], row["Foja"], row["Curso"], row["Duración en horas"], hr_hrs, row["Participante"], row["Constancia"]
            )
        )
        
        # Calling the `qrencode` program to create qrcodes for each row
        subprocess.run(
            ["qrencode", "-o", "{}/{}.png".format(pathQR, qrname), "{}".format(qrstring)]
        )

generateQR()