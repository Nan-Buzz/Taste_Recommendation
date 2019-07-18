import time
import os
import sys
import pandas as pd
import spacy
import re


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
# dir_name_in = "./review-step2"
# dir_name_out = "./review-step3"
file_name = 'review12.json'
# os.makedirs(dir_name_out)

cc = pd.read_json(file_name, orient="records", lines=True, chunksize=10000)
ii_list = []
for count1, ii1 in enumerate(cc, start=1):
    sys.stdout.write(f'\rcomplete percent:{count1:.0f}')
    ii1["text_step1"] = ii1.apply(lambda row: xyn_io(kk=row["text"]), axis=1)
    ii_list.append(ii1[['user_id', 'text_step1', 'date']])

sys.stdout.flush()
Xyn_date = pd.concat(ii_list)
Xyn_date.to_json("review-12.json", orient="records", lines=True)
###################################################################
xyn_time_end = time.time()
xyn_minute, xyn_seconds = divmod(xyn_time_end - xyn_time_start, 60)
xyn_hour, xyn_minute = divmod(xyn_minute, 60)
print("%02d:%02d:%02d" % (xyn_hour, xyn_minute, xyn_seconds))
