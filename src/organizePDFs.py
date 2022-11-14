#!/usr/bin/env python3
import os
from lib.env import pathSeparateCerts

def organize():
    '''
    It takes input for a start year, an end year, and a max instance amount, 
    and then it organizes all the files in the `pathSeparateCerts` directory 
    into folders named `Año_<year>/Foja_<instance>/<file>`
    '''
    
    startYear:int = int(input('Start year: '))
    endYear:int = int(input('End year: '))
    maxInstanceAmount:int = int(input('Max instance amount: '))

    # (`os.listir` does not return sorted results)
    names = sorted(os.listdir(pathSeparateCerts))


    years  = [str(x) for x in range(startYear, endYear + 1)]
    instances = [str(x).zfill(3) for x in range(1, maxInstanceAmount + 1)]

    for year in years:
        # if there isn't a year directory, create one
        pathYear = os.path.join(pathSeparateCerts, 'Año_' + year)
        if not os.path.exists(pathYear): os.mkdir(pathYear)

        for instance in instances:
            # if there isn't an instance directory, create one
            pathInstance = os.path.join(pathYear, 'Foja_' + instance)
            if not os.path.exists(pathInstance): os.mkdir(pathInstance)

            for name in names:
                pathFile = os.path.join(pathSeparateCerts, name)
                if "C{}F{}".format(year, instance) in name:
                    os.rename(pathFile, pathInstance + name)

    return

organize()
