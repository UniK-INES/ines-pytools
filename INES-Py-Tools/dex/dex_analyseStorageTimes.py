'''
Created on 25.10.2019

DEX script

Parses DEX market logfile and prints statistics (min, max, mean) of request processing to console. 

@author: Sascha Holzhauer
'''
import statistics
import re

experiment = "10-65"
logfileName = "/home/sascha/_INES/X/DEX/data/output/multiEMGs/logs/enavi_" + experiment + "/enavi_" + experiment + "_1_market.log"

if __name__ == '__main__':
    # read source log file
    logFile = open(logfileName, 'r')
    
    # open csv table
    times = []
    print("Statistics for " + re.findall(r'\d\d-\d\d', logfileName)[1] + ":")
    for line in logFile:
        if line.find("Processing request")>=0:
            times.append(float(line[-7:-2]))
    print("Min: " + str(min(times)))
    print("Max: " + str(max(times)))
    print("Mean: " + str(statistics.mean(times)))
    print("Done.")