import time
import sys
import os
import pandas as pd


def Pandas_Xyn_Split(name, num):
    file_name = name.split(".")[0]
    file_Suffix = '.csv'
    PBD_data = pd.read_csv(name, chunksize=num)
    os.makedirs(file_name)
    for count, ii in enumerate(PBD_data, start=1):
        sys.stdout.write(f'\rcomplete percent:{count:.0f}')
        ii.dropna(axis=0, how='any', subset=ii.columns.values.tolist(), inplace=True)
        ii.to_csv("./"+file_name+"/"+str(count)+file_Suffix, index=False)
    sys.stdout.flush()
    return True

xyn_time_start = time.time()
###################################################################
Pandas_Xyn_Split("review.csv", 10000)
###################################################################
xyn_time_end = time.time()
xyn_minute, xyn_seconds = divmod(xyn_time_end - xyn_time_start, 60)
xyn_hour, xyn_minute = divmod(xyn_minute, 60)
print("%02d:%02d:%02d" % (xyn_hour, xyn_minute, xyn_seconds))
