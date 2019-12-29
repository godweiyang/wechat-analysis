# -*- coding: utf-8 -*-
import sys
from collections import defaultdict
from operator import itemgetter
import copy
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.pyplot import MultipleLocator

mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

'''
1577516323135: (14:58)
'''

# 00:00
t_time = 1577462443135

def main(input_filename):
    fin = open(input_filename, "r", encoding='utf8')

    h_list = [0] * 24

    for line in fin.readlines():
        s_time = int(line)
        delta = s_time - t_time
        delta_ms = ((delta % 86400000) + 86400000) % 86400000
        delta_s = delta_ms / 1000
        delta_m = delta_s / 60
        hh = int(delta_m / 60)
        mm = int(delta_m % 60)
        h_list[hh] += 1
    
    x = [i for i in range(24)]
    y = h_list

    plt.figure(figsize=(8, 4))
    plt.plot(x, y, color="#F1B5B5")

    x_major_locator = MultipleLocator(1)
    ax = plt.gca()
    ax.xaxis.set_major_locator(x_major_locator)

    plt.xlabel(r"时间")
    plt.ylabel(r"条数")
    plt.title(r"2019年微信每个时间段发送消息条数")
    for a, b in zip(x, y):
        plt.text(a, b, b, ha='center', va='bottom')
    plt.show()

if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print('[usage] <input>')

