#!/usr/bin/env python3
import csv

def csv_to_list(path_to_csv):
    ''' csv_to_list(path_to_csv)

    Reads csv file and returns a list of dictionaries, where 
    each dictionary is a row of the csv file.
    
    :param path_to_csv: the path to the csv file you want to convert to a list
    :return: A list of dictionaries.
    '''
    with open(path_to_csv) as participants_csv:
        participants_dict = csv.DictReader(participants_csv)
        participants_list = list(participants_dict)
        # participants_list:       [{row1}, {row2}, ...]
        # Each dict is a csv row:  {"Año":2020, "Foja":...}
    return participants_list

def csv_col_names(path_to_csv):
    ''' csv_col_names(path_to_csv)

    Reads csv file as a dictionary, and returns the column names.
    
    :param path_to_csv: the path to the csv file you want to read
    :return: A list of the column names in the csv file.
    '''
    with open(path_to_csv) as participants_csv:
        participants_dict = csv.DictReader(participants_csv)
        col_names = participants_dict.fieldnames
    return col_names

