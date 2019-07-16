import time
import sys
import os
import spacy
import re
import pandas as pd


def xyn_io(kk):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(kk)
    text_temp = []
    for ii3 in doc:
        hj = re.findall(r'[A-Za-z]+', ii3.lemma_)
        if hj != []:
            text_temp.append(hj[0].lower())
    return text_temp

xyn_time_start = time.time()
###################################################################
dir_name_in = "./review"
dir_name_out = "./review_step1"
file_name_list = os.listdir(dir_name_in)
if 'error_log.txt' in file_name_list: file_name_list.remove('error_log.txt')
if 'right_log.txt' in file_name_list: file_name_list.remove('right_log.txt')
file_name_list.sort()
os.makedirs(dir_name_out)
txt_error = []
txt_right = []

for count1, ii1 in enumerate(file_name_list, start=1):
    sys.stdout.write(f'\rcomplete percent:{count1:.0f}')
    try:
        Xyn_date = pd.read_csv(dir_name_in+"/"+ii1, usecols=['user_id', 'text', 'date'])
        ############################################
        Xyn_date["text_step1"] = Xyn_date.apply(lambda row: xyn_io(kk=row["text"]), axis=1)
        Xyn_date[['user_id', 'text_step1', 'date']].to_json(dir_name_out+'/'+str(count1)+'.json', orient="records", lines=True)
    except:
        txt_error.append(ii1)
        with open(dir_name_out+'/'+"error_log.txt", "w", encoding='utf8') as f:
            for i in txt_error:
                f.write(i + '\n')
    else:
        txt_right.append(ii1)
sys.stdout.flush()
###################################################################
with open(dir_name_out+'/'+"right_log.txt", "w", encoding='utf8') as f:
    for i in txt_right:
        f.write(i + '\n')
xyn_time_end = time.time()
xyn_minute, xyn_seconds = divmod(xyn_time_end - xyn_time_start, 60)
xyn_hour, xyn_minute = divmod(xyn_minute, 60)
print("%02d:%02d:%02d" % (xyn_hour, xyn_minute, xyn_seconds))
