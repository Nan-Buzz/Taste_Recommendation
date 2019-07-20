import time
import sys
import os
import spacy
import re
import pandas as pd
import sys
import random
import psutil


xyn_time_start = time.time()
###################################################################
# Xyn_memory = psutil.Process(os.getpid()).memory_full_info().uss / 1048576.
# print('Memory used: {:.2f} MB'.format(Xyn_memory))

dir_name_in = "./review-step2"
dir_name_out = "./review-step3"
dir_name_temp = "./temp"
file_name_list = os.listdir(dir_name_in)
file_name_first = sys.argv[1]
file_name_last = '.json'
file_name_list.remove(file_name_first+file_name_last)
os.makedirs(dir_name_temp)

out_num = len(os.listdir(dir_name_out))
for count1, xyn_num in enumerate(file_name_list, start=0):
    if count1 == out_num:
        break
    os.rename(dir_name_out+'/'+file_name_first+str(count1)+file_name_last, dir_name_temp+'/'+xyn_num)
###################################################################
xyn_time_end = time.time()
xyn_minute, xyn_seconds = divmod(xyn_time_end - xyn_time_start, 60)
xyn_hour, xyn_minute = divmod(xyn_minute, 60)
print(("%02d:%02d:%02d" % (xyn_hour, xyn_minute, xyn_seconds)))


