# coding: utf-8
'''
Created on 19.01.2018

Parses CSV file of finished theses and produces HTML file to be copied and pasted to INES website
Works with python 3.x

Requirements:
- A CSV file INES_Abschlussarbeiten4Website_<createdate>.csv in directory defined in inputFile with columns 
Abschluss (first column)
Nachname (2nd column)
Vorname (3rd column)
Titel (4th column)
Abschlussdatum (5th column)

Steps to adapt:
- Edit createdate according to input data
- Adapt directory in inputFile

@author: Sascha Holzhauer

https://docs.python.org/2/library/csv.html#csv-fmt-params

TODO: Stand (datum) ausgeben
'''

import csv
from operator import itemgetter
import math
#from asn1crypto._ffi import null

createdate = '2020-08-21'

inputFile = '/daten/INES/Außendarstellung/Website/Inhalte/Abschlussarbeiten/' + createdate + '/INES_Abschlussarbeiten4Website_' + createdate + '.csv'
# w/o extention!
outputFile = '/daten/INES/Außendarstellung/Website/Inhalte/Abschlussarbeiten/' + createdate + '/INES_Abschlussarbeiten4Website_' + createdate

types = {"BA": "Bachelor", "MA": "Master", "Dipl": "Diplomarbeiten", "Dis": "Dissertationen"}
typesPrio = {"BA": 3, "MA": 2, "Dipl": 4, "Dis": 1}

if __name__ == '__main__':
    
    # read CSV data
    reader = csv.reader(open(inputFile, 'r'), delimiter=';')
    header = next(reader)
    
    # sort by 'Abschluss' and 'Abschlussdatum'
    s = sorted(reader, key=lambda d: list(map(int,  [d[4].replace(".","/").split('/')[i] for i in [2,1,0]]) if "/" in d[4] or "." in d[4] else float("inf")), reverse=True)
    s = sorted(s, key=lambda d:typesPrio[d[0].strip()])
    
    # output HTML
    oldtype = ""
    output = open(outputFile + "_" + types["BA"] + ".html", 'w')
    for thesis in s:
        if thesis[0].strip() != oldtype:
            try:
                output
            except NameError:
                output.close()
            output = open(outputFile + "_" + types[thesis[0].strip()] + ".html", 'w')
            oldtype = thesis[0].strip()
        output.write("<p>" + thesis[1].strip() + ", " + thesis[2].strip() + "<br>" + "\n")
        output.write("<i>" + thesis[3].strip() + "</i> (" + thesis[4].strip().replace("/",".") + ")</p><br>\n")
          
print("Done")