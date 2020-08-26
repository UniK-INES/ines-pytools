# coding: utf-8
'''
Created on 19.01.2018

Parses CSV file of current theses and produces HTML file to be copied and pasted to INES website

Requirements:
- A CSV file INES_AbschlussarbeitenLaufend_<createdate>.csv in directory defined in inputFile with columns 
Abschluss (first column)
Nachname (2nd column)
Vorname (3rd column)
Titel (4th column)

Steps to adapt:
- Edit createdate according to input data
- Adapt directory in inputFile

@author: Sascha Holzhauer

TODO: Stand (datum) ausgeben
'''

import csv
from operator import itemgetter
import math

createdate = '2020-08-21'

inputFile = '/daten/INES/Außendarstellung/Website/Inhalte/Abschlussarbeiten/' + createdate + '/INES_AbschlussarbeitenLaufend_' + createdate + '.csv'
outputFile = '/daten/INES/Außendarstellung/Website/Inhalte/Abschlussarbeiten/' + createdate + '/INES_AbschlussarbeitenLaufend_' + createdate + '.html'


types = {"BA": "Bachelor", "MA": "Master", "Dipl": "Diplomarbeiten", "Dis": "Dissertationen"}
typesPrio = {"BA": 3, "MA": 2, "Dipl": 4, "Dis": 1}

if __name__ == '__main__':
    
    # read CSV data
    reader = csv.reader(open(inputFile, 'r'), delimiter=';')
    header = next(reader)
    
    # sort by 'Abschluss' and 'Name'
    s = sorted(reader, key=lambda d: d[1].strip()+d[2].strip(), reverse=False)
    s = sorted(s, key=lambda d:typesPrio[d[0].strip()])
    
    # output HTML
    output = open(outputFile, 'w')
    oldtype = ""

    for thesis in s:
        if thesis[0].strip() != oldtype:
            output.write("<h2>" + types[thesis[0].strip()] + "</h2>\n\n")
            oldtype = thesis[0].strip()
        output.write("<p>" + thesis[1].strip() + (", " if len(thesis[1].strip())>0 else "") + thesis[2].strip() + "<br>" + "\n")
        output.write("<i>" + thesis[3].strip() + "</i></p>\n")
          
    output.close()
print("Done")