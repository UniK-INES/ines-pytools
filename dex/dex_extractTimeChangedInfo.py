'''
Created on 20.11.2018

DEX script

Parses EMG logfile and write time synchronisation data to given CSV file.

@author: Sascha Holzhauer
'''
import csv
import re

logfileName = "/home/sascha/_INES/X/DEX/data/output/stageA/logs/enavi_07-01/enavi_07-01_emg.log"
csvFileName = "/home/sascha/_INES/X/DEX/data/output/stageA/logs/enavi_07-01/TimesChanged_07-01.csv"


if __name__ == '__main__':
    # read source log file
    logFile = open(logfileName, 'r')
    
    # open csv table
    csvFile = open(csvFileName, 'w')
    csvKeys = ["type", "market_sim", "market_real", "emg_sim", "emg_sim_corr", "emg_real"]
    csvWriter = csv.DictWriter(csvFile, csvKeys)
    timeDict = dict.fromkeys(csvKeys)
   
    # parse log and write to csv table
    csvWriter.writeheader()
    for line in logFile:
        if line.find("Time changed:")>=0:
            changed = line[line.find("Time changed:"):(line.find("Time changed:")+19)]
            time = re.findall(r'\d\d:\d\d:\d\d', line)
            timeDict[csvKeys[0]] = changed.replace(";","")
            for i in range(0, len(timeDict)-1):
                timeDict[csvKeys[i + 1]]= time[i]
            
            csvWriter.writerow(timeDict)
    csvFile.close()
    logFile.close()
    print("Done.")