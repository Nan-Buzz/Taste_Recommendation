import time
import sys
import os
import spacy
import re
import pandas as pd
import sys
import random


xyn_time_start = time.time()
###################################################################
ko = []
abc = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in range(26):
    user_id = '"user_id":"' + abc[i] + '"'
    for j in range(3):
        review_id = '"review_id":"'+abc[i]+str(j)+'", '
        we = ''
        for h in range(5):
            we += chr(random.randint(97, 122))
        text = '"text":"' + we + '", '
        date = '"date":' + str(random.randint(0, 2000)) + ', '
        end = '{'+review_id+text+date+user_id+'}'
        ko.append(end)
with open("ip2.txt", "a", encoding='utf8') as f:
    for i in ko:
        f.write(i + '\n')
###################################################################
xyn_time_end = time.time()
xyn_minute, xyn_seconds = divmod(xyn_time_end - xyn_time_start, 60)
xyn_hour, xyn_minute = divmod(xyn_minute, 60)
print("%02d:%02d:%02d" % (xyn_hour, xyn_minute, xyn_seconds))


