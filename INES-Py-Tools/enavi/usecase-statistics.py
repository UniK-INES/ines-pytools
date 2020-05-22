'''
Created on 27.06.2018

Parses a catalog of use cases and category definition (category, cluster, and HLUC) and produces statistics with
the occurrences of category (column Occurrence) and cluster (column ClusterOccurrence) within the use cases in the catalog.

Requirements:
- use case catalog with columns (left to right; (at least)):
Cluster1
UC1
Cluster2
UC2
Cluster3
UC3

- use case categories file with columns (at least):
Category
ClusterName

@author: Sascha Holzhauer
'''

import csv
import re
import glob, os
import pandas as pd

importDir   = "/home/sascha/_INES/Projekte/ENavi/AP9/UseCases/"

csvFileUseCaseCatalog = "ENavi_UseCasesCatalog_SH.csv"
csvFileUseCaseCategories = "ENavi_UseCasesCategories_SH.csv"

csvFileStatistic = "ENavi_UseCasesStatistics_SH.csv"

csvUseCaseCatalog = open(importDir + csvFileUseCaseCatalog, 'r')
csvUseCaseCategories = open(importDir + csvFileUseCaseCategories, 'r')

# read categories:
ucCategories = pd.read_csv(csvUseCaseCategories, delimiter=',')
ucCategories.loc[:,'Occurrence'] = 0
ucCategories.loc[:,'ClusterOccurrence'] = 0

ucCategories.Cluster.apply(int)
ucCategories.HLUC.apply(int)

# parse catalog
with csvUseCaseCatalog as csvfile:
    catalogReader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
    for row in catalogReader:
        if (row['Cluster1']!=''):
            ucCategories.loc[ucCategories['Cluster']==int(row['Cluster1']),'ClusterOccurrence'] += 1
            if row['UC1'] == '':
                # all HLUC of a cluster
                ucCategories.loc[ucCategories['Cluster']==int(row['Cluster1']),'Occurrence'] += 1
            elif '-' in row['UC1']: 
                first = int(row['UC1'][0])
                last = int(row['UC1'][2])
                ucCategories.loc[(ucCategories.Cluster==int(row['Cluster1'])) & 
                                 (ucCategories.HLUC >= first) & (ucCategories.HLUC <= last),'Occurrence'] += 1
            else:
                ucCategories.loc[(ucCategories.Cluster==int(row['Cluster1'])) &
                                 (ucCategories.HLUC == int(row['UC1'])),'Occurrence'] += 1
     
        if (row['Cluster2']!=''):
            ucCategories.loc[ucCategories['Cluster']==int(row['Cluster2']),'ClusterOccurrence'] += 1
            if row['UC2'] == '':
                # all HLUC of a cluster
                ucCategories.loc[ucCategories['Cluster']==int(row['Cluster2']),'Occurrence'] += 1
            elif '-' in row['UC2']: 
                first = int(row['UC2'][0])
                last = int(row['UC2'][2])
                ucCategories.loc[(ucCategories.Cluster==int(row['Cluster2'])) & 
                                 (ucCategories.HLUC >= first) & (ucCategories.HLUC <= last),'Occurrence'] += 1
            else:
                ucCategories.loc[(ucCategories.Cluster==int(row['Cluster2'])) &
                                 (ucCategories.HLUC == int(row['UC2'])),'Occurrence'] += 1
                                 
        if (row['Cluster3']!=''):
            ucCategories.loc[ucCategories['Cluster']==int(row['Cluster3']),'ClusterOccurrence'] += 1
            if row['UC3'] == '':
                # all HLUC of a cluster
                ucCategories.loc[ucCategories['Cluster']==int(row['Cluster3']),'Occurrence'] += 1
            elif '-' in row['UC3']: 
                first = int(row['UC3'][0])
                last = int(row['UC3'][3])
                ucCategories.loc[(ucCategories.Cluster==int(row['Cluster3'])) & 
                                 (ucCategories.HLUC >= first) & (ucCategories.HLUC <= last),'Occurrence'] += 1
            else:
                ucCategories.loc[(ucCategories.Cluster==int(row['Cluster3'])) &
                                 (ucCategories.HLUC == int(row['UC3'])),'Occurrence'] += 1
                                 
csvUseCaseCatalog.close()
ucCategories.to_csv(importDir + csvFileStatistic)
print("...finished")