#Python-Tools at INES

This project contains several small python scripts in the following domains:

## Website

 * *parseThesesCurrent.py*: Parses CSV file of current theses and produces HTML file to be copied and pasted to INES website
 * *parseThesesFinished.py*: Parses CSV file of finished theses and produces HTML file to be copied and pasted to INES website
   
## DEX

 * *dex_analyseStorageTimes.py*: Parses DEX market logfile and prints statistics (min, max, mean) of request processing to console
 * *dex_extractTimeChangedInfo.py*: Parses EMG logfile and write time synchronisation data to given CSV file.
 * *dex_generateClusterRunScript.py*: Create bash script to run DEX simulation on UniK Linux cluster based on Batch configuration table

## ENavi

 * *usecase-statistics.py*: Parses a catalog of use cases and category definition (category, cluster, and HLUC) and produces statistics with
the occurrences of category (column Occurrence) and cluster (column ClusterOccurrence) within the use cases in the catalog.

## Contact:

Sascha.Holzhauer@uni-kassel.de
