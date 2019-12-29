# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.pyplot import MultipleLocator
import sys
from collections import defaultdict
from operator import itemgetter
import copy

mpl.rcParams['font.sans-serif'] = ['SimHei']
mpl.rcParams['axes.unicode_minus'] = False

def main(input_filename):
    fin = open(input_filename, "r", encoding='utf8')

    name_count = defaultdict(int)

    for line in fin.readlines():
        if len(line.strip().split()) > 0:
            try:
                name = line.strip().split()[0]
                name_count[name] += 1
            except:
                # print(len(line))
                exit(0)

    sorted_dict = sorted(name_count.items(), key=lambda d: d[1], reverse=True)

    x = []
    y = []
    for tu in sorted_dict:
        x.append(str(tu[0]))
        y.append(int(tu[1]))
    # x = ['yyj', 'qq', 'fzc', 'syt', 'lcz', 'whm', 'scy', 'lyc', 'whp', 'zmm', 'dyp']
    # y = [12925, 11850, 6371, 3967, 2526, 2141, 1908, 1747, 1417, 1157, 1157]
    x = x[:10]
    y = y[:10]

    plt.figure(figsize=(8, 4))
    plt.bar(x, y, color="#F1B5B5")

    x_major_locator = MultipleLocator(1)
    ax = plt.gca()
    ax.xaxis.set_major_locator(x_major_locator)

    for tick in ax.get_xticklabels():
        tick.set_rotation(15)

    plt.xlabel(r"人名")
    plt.ylabel(r"条数")
    plt.title(r"2019年微信互发消息条数排名")
    for a, b in zip(x, y):
        plt.text(a, b, b, ha='center', va='bottom')
    plt.show()
        

if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv[1])
    else:
        print('[usage] <input>')

