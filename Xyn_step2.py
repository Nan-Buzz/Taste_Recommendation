import time
import os
import sys
import pandas as pd
import spacy
import re


def xyn_io(kk):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(kk)
    nlp = []
    text_temp = []
    for ii3 in doc:
        hj = re.findall(r'[A-Za-z]+', ii3.lemma_)
        if hj != []:
            text_temp.append(hj[0].lower())
            hj = []
    return text_temp


def xyn_all(ii1):
    ii1["text_step1"] = ii1.apply(lambda row: xyn_io(kk=row["text"]), axis=1)
    return ii1[['user_id', 'text_step1', 'date']]


if __name__ == '__main__':
    xyn_time_start = time.time()
    ###################################################################
    dir_name_in = "./review-step2"
    dir_name_out = "./review-step3"
    file_name_list = os.listdir(dir_name_in)
    if os.path.exists(dir_name_out) == False:
        os.makedirs(dir_name_out)

    pool = mp.Pool(processes=6)
    cc = pd.read_json(dir_name_in + '/' + file_name_list[0], orient="records", lines=True, chunksize=100)
    data = pool.map(xyn_all, cc)
    Xyn_date = pd.concat(data)
    try:
        Xyn_date.to_json(dir_name_out + '/' + file_name_list[0], orient="records", lines=True)
    except:
        print("Failed!!!")
    else:
        print("File processing completed.")
    ###################################################################
    xyn_time_end = time.time()
    xyn_minute, xyn_seconds = divmod(xyn_time_end - xyn_time_start, 60)
    xyn_hour, xyn_minute = divmod(xyn_minute, 60)
    print(("%02d:%02d:%02d" % (xyn_hour, xyn_minute, xyn_seconds)))

########################################################################################################################
# xyn_time_start = time.time()
# ###################################################################
# dir_name_in = "./review-step2"
# dir_name_out = "./review-step3"
# file_name_list = os.listdir(dir_name_in)
# file_name_first = file_name_list[0].split('.')[0]
# file_name_last = '.json'
# if os.path.exists(dir_name_out) == False:
#     os.makedirs(dir_name_out)
#
#
# num = 50
# Xyn_date = pd.read_json(dir_name_in+'/'+file_name_first+file_name_last, orient="records", lines=True, chunksize=1000)
# data = []
# for iii in Xyn_date:
#     data.append(iii)
# Xyn_date = pd.concat(data)
# data = Xyn_date[['user_id']].drop_duplicates(keep='first')
# rol = len(data['user_id'])//num
# for iii in range(num):
#     if iii == (num-1): cc = data[rol*iii:]
#     else: cc = data[rol*iii:rol*(iii+1)]
#     Xyn_date['new'] = Xyn_date['user_id'].isin(cc['user_id'])
#     Xyn_date[Xyn_date.new == True][['date', 'review_id', 'text', 'user_id']].to_json(dir_name_in+'/'+file_name_first+str(iii)+file_name_last, orient="records", lines=True)
#
# file_name_list = os.listdir(dir_name_in)
# file_name_list.remove(file_name_first+file_name_last)
# Xyn_date = []
# data = []
# cc = []
# print("File Segmentation Completion.")
# ###################################################################
# xyn_time_end = time.time()
# xyn_minute, xyn_seconds = divmod(xyn_time_end - xyn_time_start, 60)
# xyn_hour, xyn_minute = divmod(xyn_minute, 60)
# print("%02d:%02d:%02d" % (xyn_hour, xyn_minute, xyn_seconds))
