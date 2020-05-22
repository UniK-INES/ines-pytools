'''
Created on 10.05.2019

TODO implement

@author: Sascha Holzhauer
'''

import netCDF4 as nc4

if __name__ == '__main__':
    
    
    f = nc4.Dataset('home/sascha/_INES/X/DEX/Services/Weather/Datenquellen/REMO/RE_UBA_A1B_D3_1H_WIND_SPEED.160656-166536.nc','r')
    tempgrp = f.groups['Temp_data']

    dates = num2date(rootgrp.variables['time'][:],units=rootgrp.variables['time'].units)
var1=rootgrp.variables['var1']
var2=rootgrp.variables['var2']

cpy = cStringIO.StringIO()

for timeindex, time in enumerate(dates):

    validtimes=np.empty(var1[timeindex].size, dtype="object")
    validtimes.fill(time)

    #  Transponse and stack the arrays of parameters
    #    [a,a,a,a]        [[a,b,c],
    #    [b,b,b,b]  =>     [a,b,c],
    #    [c,c,c,c]         [a,b,c],
    #                      [a,b,c]]

    a = np.hstack((
              validtimes.reshape(validtimes.size,1),
              stationnames.reshape(stationnames.size,1),
              var1[timeindex].reshape(var1[timeindex].size,1),
              var2[timeindex].reshape(var2[timeindex].size,1)
    ))

    # Fill the cStringIO with text representation of the created array
    for row in a:
            cpy.write(row[0].strftime("%Y-%m-%d %H:%M")+'\t'+ row[1] +'\t' + '\t'.join([str(x) for x in row[2:]]) + '\n')


conn = psycopg2.connect("host=postgresserver dbname=nc user=user password=passwd")
curs = conn.cursor()

cpy.seek(0)
curs.copy_from(cpy, 'ncdata', columns=('validtime', 'stationname', 'var1', 'var2'))
conn.commit()