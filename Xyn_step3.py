import time
import sys
import os
import pandas as pd

def xyn_merge_step1(kk, hh):
    cc = hh[hh['user_id'] == kk].sort_values(by='date', ascending=False)
    return cc['text_step1'].values.tolist()

def xyn_merge_step2(kk, hh):
    cc = hh[hh['user_id'] == kk].sort_values(by='date', ascending=False)
    return cc['date'].values.tolist()

xyn_time_start = time.time()
###################################################################
dir_name_in = "./review-step3"
dir_name_out = "./review-step4"
file_name_list = os.listdir(dir_name_in)
os.makedirs(dir_name_out)

for count1, ii1 in enumerate(file_name_list, start=1):
    sys.stdout.write(f'\rcomplete percent:{count1:.0f}')
    Xyn_date = pd.read_json(dir_name_in+'/'+ii1, orient="records", lines=True)
    data = Xyn_date[['user_id']].drop_duplicates(keep='first')
    data["text_sort"] = data.apply(lambda row: xyn_merge_step1(kk=row["user_id"], hh=Xyn_date), axis=1)
    data["date_sort"] = data.apply(lambda row: xyn_merge_step2(kk=row["user_id"], hh=Xyn_date), axis=1)
    Xyn_date = []
    data[['user_id', 'text_sort', 'date_sort']].to_json(dir_name_out + '/' + ii1, orient="records", lines=True)

sys.stdout.flush()
###################################################################
xyn_time_end = time.time()
xyn_minute, xyn_seconds = divmod(xyn_time_end - xyn_time_start, 60)
xyn_hour, xyn_minute = divmod(xyn_minute, 60)
print("%02d:%02d:%02d" % (xyn_hour, xyn_minute, xyn_seconds))
