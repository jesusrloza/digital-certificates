#!/usr/bin/sh

# create directories for all and separate digital certificates
# just in case they're missing
mkdir -p ../pdfs/separate

# separate pages of the file with all certificates  
pdfseparate ../pdfs/all.pdf ../pdfs/separate/%04d.pdf

# rename individual files with relevant data instead of generic names 
./renamePDFs.py

