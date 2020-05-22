'''
Created on 21.05.2019

DEX script

Create bash script to run DEX simulation on UniK Linux cluster based on Batch configuration table

Instructions:
- Autofilter batch run configuration CSV file
- Filter desired rows
- Copy these rows including header (only 2nd header row) 
- Run this script

@author: Sascha Holzhauer
'''

import pandas as pd
import os
import argparse

parser = argparse.ArgumentParser(description='Cluster Run Script Generation')

parser.add_argument('--verbose', action='store_true',
                    help='Show more information')
args = parser.parse_args()

batchConfigFile = "/daten/INES/X/DEX/config/So-EASY_DEX_BatchConfigs.ods"
paramDir="/daten/INES/X/DEX/config/parameters"

configFilename="/daten/INES/X/DEX/config/parameters/neis2020/DEX_Param_Configs_NEIS2020.ods"
remoteUserName = "uk052959"
scriptTmpDir="/tmp/"

verbose = args.verbose
makeParamDirs = False

if __name__ == '__main__':
   
    # read clipboard    
    data = pd.read_clipboard()
    if verbose: print(data)
    
    # define filename
    scriptFilename = scriptTmpDir + data.ix[0, "IDs"].replace("-","_") + "-" + data.ix[len(data.index)-1, "IDs"].rsplit("-",1)[1] + ".sh"
    print("Write script to " + scriptFilename)
    
    # extract fields and write to script file
    scriptFile = open(scriptFilename, "w")
    scriptFile.write('#!/bin/sh\n\n')
    
    for drow in range(0, len(data.index)):
        # create parameter folder if not existing:
        if makeParamDirs:
            os.makedirs(paramDir + "/" + data.ix[drow, "Version"] + "/" + data.ix[drow, "IDs"], exist_ok=True)
            
        if verbose: print(data.ix[drow, "PythonScriptCall"])
        # transfer parameter folders
        if verbose: print("scp -r " + paramDir + "/" + data.ix[drow, "Version"] + "/" + data.ix[drow, "IDs"] + " " + remoteUserName + 
              "@its-cs1.its.uni-kassel.de:/home/users/0033/uk052959/dex/config/parameters")
        os.system("scp -r " + paramDir + "/" + data.ix[drow, "Version"] + "/" + data.ix[drow, "IDs"] + " " + remoteUserName + 
              "@its-cs1.its.uni-kassel.de:/home/users/0033/uk052959/dex/config/parameters/" + data.ix[drow, "Version"])
        
        if verbose: print("Append to script...")
        scriptFile.write(data.ix[drow, "PythonScriptCall"] + "\n")
    scriptFile.write("\ncd ../\n")
    
    for drow in range(0, len(data.index)):
        if verbose: print(data.ix[drow, "BatchScript"])
        scriptFile.write(data.ix[drow, "BatchScript"] + "\n")
    
    scriptFile.write("\necho 'Done'")
    scriptFile.close()
    os.chmod(scriptFilename, 0o755)
    
    # transfer script file to server
    os.system("scp " + scriptFilename + " " + remoteUserName + 
              "@its-cs1.its.uni-kassel.de:/home/users/0033/uk052959/dex/config/cluster")
   
    # transfer Config file
    os.system("scp " + configFilename + " " + remoteUserName + 
              "@its-cs1.its.uni-kassel.de:/home/users/0033/uk052959/dex/config/parameters")
    
    if verbose: print("Done.")
    