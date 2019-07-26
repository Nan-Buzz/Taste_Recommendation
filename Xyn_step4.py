import time
import sys
import os
import pandas as pd
import math
import collections

def shannon_entropy(seq):
    C, n = collections.Counter(seq), float(len(seq))
    return -sum(c / n * math.log(c / n, 2) for c in list(C.values()))

def entropy(seq, lambdas=False):
    N = len(seq)
    L = []
    for i, w in enumerate(seq):
        seen = True
        prevSeq = " %s " % " ".join(seq[0:i])
        c = i
        while seen and c < N:
            c += 1
            seen = (" %s " % " ".join(seq[i:c])) in prevSeq
        l = c - i
        L.append(l)

    if lambdas:
        return L
    return (1.0 * N / sum(L)) * math.log(N, 2)

def xyn_shannon(kk):
    temp = []
    for iii in kk:
        temp.extend(iii)
    return shannon_entropy(temp)

def xyn_entropy(kk):
    temp = []
    for iii in kk:
        temp.extend(iii)
    return entropy(temp)


xyn_time_start = time.time()
###################################################################
dir_name_in = "./review-step4"
dir_name_out = "./review-step5"
file_name_list = os.listdir(dir_name_in)
os.makedirs(dir_name_out)

for count1, ii1 in enumerate(file_name_list, start=1):
    sys.stdout.write(f'\rcomplete percent:{count1:.0f}')
    Xyn_date = pd.read_json(dir_name_in+'/'+ii1, orient="records", lines=True)
    Xyn_date["shannon"] = Xyn_date.apply(lambda row: xyn_shannon(kk=row["text_sort"]), axis=1)
    Xyn_date["entropy"] = Xyn_date.apply(lambda row: xyn_entropy(kk=row["text_sort"]), axis=1)
    Xyn_date[['user_id', 'shannon', 'entropy']].to_json(dir_name_out + '/' + ii1, orient="records", lines=True)

sys.stdout.flush()
###################################################################
xyn_time_end = time.time()
xyn_minute, xyn_seconds = divmod(xyn_time_end - xyn_time_start, 60)
xyn_hour, xyn_minute = divmod(xyn_minute, 60)
print("%02d:%02d:%02d" % (xyn_hour, xyn_minute, xyn_seconds))
