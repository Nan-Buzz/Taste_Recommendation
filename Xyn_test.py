import time
import sys
import os
import spacy
import re
import pandas as pd
import sys
import random
import psutil
import numpy as np
import matplotlib.pyplot as plt
import multiprocessing as mp
import threading as td


if __name__ == '__main__':
    xyn_time_start = time.time()
    ###################################################################
    # Xyn_memory = psutil.Process(os.getpid()).memory_full_info().uss / 1048576.
    # print('Memory used: {:.2f} MB'.format(Xyn_memory))

    # Xyn_date = pd.read_csv('user_id_plot.csv')
    #
    # X = Xyn_date['comment_num'].values
    # Y = Xyn_date['user_num'].values
    #
    # T = X.copy()
    # T[T <= 56] = 0
    # T[T > 56] = 10
    #
    # plt.rcParams['font.sans-serif'] = ['SimHei'] # 用来正常显示中文标签，这里面是字体
    # plt.rcParams['axes.unicode_minus'] = False # 用来正常显示负号
    #
    # figsize = 15, 9
    # figure, ax = plt.subplots(figsize=figsize)
    # # 设置坐标刻度值的大小以及刻度值的字体
    # plt.tick_params(labelsize=23)
    # labels = ax.get_xticklabels() + ax.get_yticklabels()
    #
    # # 设置横纵坐标的名称以及对应字体格式
    # font = {'weight': 'normal',
    #         'size': 30,}
    #
    #
    #
    # # 输入X和Y作为location，size=75，颜色为T，透明度alpha 为 50%
    # plt.scatter(np.log10(X), np.log10(Y), s=75, c=T, alpha=.5)
    # plt.xticks([0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5], [r'$10^0$', r'$10^0.5$', r'$10^1$', r'$10^1.5$', r'$10^2$', r'$10^2.5$', r'$10^3.0$', r'$10^3.5$'])
    # plt.yticks([0, 1, 2, 3, 4, 5, 6], [r'$10^0$', r'$10^1$', r'$10^2$', r'$10^3$', r'$10^4$', r'$10^5$', r'$10^6$'])
    # plt.xlabel('评论数', font) # 设置x轴名称
    # plt.ylabel('用户数', font)
    # plt.show()

    dir_name_in = "./review-step2"
    dir_name_out = "./review-step3"
    file_name_in = os.listdir(dir_name_in)
    file_name_out = os.listdir(dir_name_out)
    ret = list(set(file_name_in).intersection(set(file_name_out)))
    for ii in ret:
        os.remove(dir_name_in + '/' + ii)
    ###################################################################
    xyn_time_end = time.time()
    xyn_minute, xyn_seconds = divmod(xyn_time_end - xyn_time_start, 60)
    xyn_hour, xyn_minute = divmod(xyn_minute, 60)
    print(("%02d:%02d:%02d" % (xyn_hour, xyn_minute, xyn_seconds)))

