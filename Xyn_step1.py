import time
import os
import sys
import pandas as pd


xyn_time_start = time.time()
###################################################################
# file_name = 'review0102'   # 切分
# jkl = '.json'
# num = 3  # 拆的份数
# Xyn_date = pd.read_json(file_name+jkl, orient="records", lines=True)
# data = Xyn_date[['user_id']].drop_duplicates(keep='first')
# rol = len(data['user_id'])//num
# for iii in range(num):
#     if iii == (num-1): cc = data[rol*iii:]
#     else: cc = data[rol*iii:rol*(iii+1)]
#     Xyn_date['new'] = Xyn_date['user_id'].isin(cc['user_id'])
#     Xyn_date[Xyn_date.new == True][['date', 'review_id', 'text', 'user_id']].to_json(file_name+str(iii)+jkl, orient="records", lines=True)

file_name_list = ['review11.json', 'review0101.json', 'review01020.json', 'review01021.json']  # 合并
out_name = 'review12-011.json'
we = []
for i in file_name_list:
    cc = pd.read_json(i, orient="records", lines=True)
    we.append(cc)
end = pd.concat(we)
end.to_json(out_name, orient="records", lines=True)
###################################################################
xyn_time_end = time.time()
xyn_minute, xyn_seconds = divmod(xyn_time_end - xyn_time_start, 60)
xyn_hour, xyn_minute = divmod(xyn_minute, 60)
print("%02d:%02d:%02d" % (xyn_hour, xyn_minute, xyn_seconds))
