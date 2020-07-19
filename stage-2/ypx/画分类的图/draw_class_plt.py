import json

import mglearn
import numpy as np
from sklearn.model_selection import train_test_split
import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt

src_json = 'E:/Desktop/3ability_data.json'

# Reading data back
with open(src_json, 'r') as f:
    src_data = json.load(f)
    f.close()
# 数组形式
X_list = []
dt_list = []
vl_list = []
mi_list = []
dim4_list = []
for user in src_data:
    l = [src_data[user]['debug_time'], src_data[user]['code_line'], src_data[user]['mi_score']]
    X_list.append(l)
    dt_list.append(src_data[user]['debug_time'])
    vl_list.append(src_data[user]['code_line'])
    mi_list.append(src_data[user]['mi_score'])

# ndarray形式 有207个用户，每个用户有4个属性
data = np.asarray(X_list)
# TODO 这个y也就是target应该是我们手动确定标签，这里只是先简单搞下
dt_list.sort()
vl_list.sort()
mi_list.sort()
y_list = []
for user in src_data:
    dt_s = float(dt_list.index(src_data[user]['debug_time'])) / len(dt_list) * 100
    vl_s = float(vl_list.index(src_data[user]['code_line'])) / len(vl_list) * 100
    mi_s = float(mi_list.index(src_data[user]['mi_score'])) / len(mi_list) * 100
    max_s = max(dt_s, vl_s, mi_s)

    if max_s < 60:
        y_list.append(0)
    else:
        if dt_s == max_s:
            y_list.append(3)
        elif vl_s == max_s:
            y_list.append(2)
        elif mi_s == max_s:
            y_list.append(1)

target = np.array(y_list)
colors = list()
palette = {0: "black", 1: "green", 2: "blue", 3: "red"}
# 图颜色的对应
for c in np.nditer(target):
    colors.append(palette[int(c)])

# print(data)
# print(data.shape)
# print(target)
# print(target.shape)

# 搞训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(data, target, random_state=0)
print(X_train.shape)  # (155,4)
print(X_test.shape)  # (52,4)
print(y_train.shape)
# 就先画下训练集的情况，看机器学习能否分类
dataFrame = pd.DataFrame(X_train, columns=['dt', 'vl', 'mi'])
# , color=colors
grr = scatter_matrix(dataFrame, figsize=(15, 15), marker='o',
                     hist_kwds={'bins': 20}, s=60, alpha=.8, cmap=mglearn.cm3)
# 保存图片地址
plt.savefig('e:/desktop/class_plt.png')
