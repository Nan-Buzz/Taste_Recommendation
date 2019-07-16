import time
import sys
import os
import pandas as pd


def xyn_merge_step1(kk, hh):
    cc = hh[hh['user_id'] == kk]
    kong = []
    for index, row in cc.iterrows():
        kong.append(row["text_step1"])
    return kong

def xyn_merge_step2(kk, hh):
    cc = hh[hh['user_id'] == kk]
    kong = []
    for index, row in cc.iterrows():
        kong.append(row["date"])
    return kong


xyn_time_start = time.time()
###################################################################
dir_name_in = "./review_step1"
dir_name_out = "./review_step2"
file_name_list = os.listdir(dir_name_in)
if 'error_log.txt' in file_name_list: file_name_list.remove('error_log.txt')
if 'right_log.txt' in file_name_list: file_name_list.remove('right_log.txt')
file_name_list.sort()
os.makedirs(dir_name_out)
txt_error = []
txt_right = []
data_list = []

for count1, ii1 in enumerate(file_name_list, start=1):
    sys.stdout.write(f'\rcomplete percent:{count1:.0f}')
    try:
        Xyn_date = pd.read_json(dir_name_in+"/"+ii1, orient="records", lines=True)
        data_list.append(Xyn_date)

    except:
        txt_error.append(ii1)
        with open(dir_name_out+'/'+"error_log.txt", "w", encoding='utf8') as f:
            for i in txt_error:
                f.write(i + '\n')
    else:
        txt_right.append(ii1)
sys.stdout.flush()

df_concat = pd.concat(data_list)
fgh = df_concat[['user_id']].drop_duplicates(keep='first')
fgh["text_all"] = fgh.apply(lambda row: xyn_merge_step1(kk=row["user_id"], hh=df_concat), axis=1)
fgh["date_all"] = fgh.apply(lambda row: xyn_merge_step2(kk=row["user_id"], hh=df_concat), axis=1)
fgh[['user_id', 'text_all', 'date_all']].to_json(dir_name_out+'/review_concat.json', orient="records", lines=True)
###################################################################
with open(dir_name_out+'/'+"right_log.txt", "w", encoding='utf8') as f:
    for i in txt_right:
        f.write(i + '\n')
xyn_time_end = time.time()
xyn_minute, xyn_seconds = divmod(xyn_time_end - xyn_time_start, 60)
xyn_hour, xyn_minute = divmod(xyn_minute, 60)
print("%02d:%02d:%02d" % (xyn_hour, xyn_minute, xyn_seconds))
