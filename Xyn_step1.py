import time
import os
import sys
import pandas as pd


xyn_time_start = time.time()
###################################################################
dir_name_in = "./review-step1"
dir_name_out = "./review-step5"
file_name = 'review.json'
os.makedirs(dir_name_out)


cc = pd.read_json(dir_name_in+"/"+file_name, orient="records", lines=True, chunksize=10000, encoding='utf-8')
ii_list = []
for count1, ii1 in enumerate(cc, start=1):
    sys.stdout.write(f'\rcomplete percent:{count1:.0f}')
    ii1.dropna(axis=0, how='any', subset=ii1.columns.values.tolist(), inplace=True)  # 删除缺失值
    ii_list.append(ii1)
    if count1 == 223:  # 只能分别跑3次，也不知道是啥原因
        break
    if count1 == 446:
        break

sys.stdout.flush()
Xyn_date = pd.concat(ii_list)
Xyn_date[['review_id', 'text', 'date', 'user_id']].to_json(dir_name_out + "/review1.json", orient="records", lines=True)
###################################################################
xyn_time_end = time.time()
xyn_minute, xyn_seconds = divmod(xyn_time_end - xyn_time_start, 60)
xyn_hour, xyn_minute = divmod(xyn_minute, 60)
print("%02d:%02d:%02d" % (xyn_hour, xyn_minute, xyn_seconds))
