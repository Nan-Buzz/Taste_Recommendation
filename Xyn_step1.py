import time
import os
import sys
import pandas as pd


xyn_time_start = time.time()
###################################################################
data = pd.read_json("user_id.json", orient="records", lines=True)
file_name_list = ['review111.json', 'review222.json', 'review333.json']
rol = len(data['user_id'])//12


for kuy in range(3):
    Xyn_date = pd.read_json(file_name_list[kuy], orient="records", lines=True)
    for iii in range(12):
        if iii == 11: cc = data[rol*iii:]
        else: cc = data[rol*iii:rol*(iii+1)]
        Xyn_date['new'] = Xyn_date['user_id'].isin(cc['user_id'])
        Xyn_date[Xyn_date.new == True][['date', 'review_id', 'text', 'user_id']].to_json('./'+str(kuy+1)+'/review'+str(iii)+'.json', orient="records", lines=True)

Xyn_date = []
data = []
for i in range(12):
    sys.stdout.write(f'\rcomplete percent:{i:.0f}')
    dd1 = pd.read_json("./1/review" + str(i) + '.json', orient="records", lines=True)
    dd2 = pd.read_json("./2/review" + str(i) + '.json', orient="records", lines=True)
    dd3 = pd.read_json("./3/review" + str(i) + '.json', orient="records", lines=True)
    tt = pd.concat([dd1, dd2, dd3], axis=0).drop_duplicates(keep='last', subset=["review_id"])
    tt.to_json('review' + str(i) + '.json', orient="records", lines=True)
sys.stdout.flush()
###################################################################
xyn_time_end = time.time()
xyn_minute, xyn_seconds = divmod(xyn_time_end - xyn_time_start, 60)
xyn_hour, xyn_minute = divmod(xyn_minute, 60)
print("%02d:%02d:%02d" % (xyn_hour, xyn_minute, xyn_seconds))
