import json

import mglearn
import numpy as np
from sklearn.model_selection import train_test_split
import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt

src_json = r'../json_flies/3areas_score.json'

# Reading data back
with open(src_json, 'r') as f:
    src_data = json.load(f)
    f.close()
# 数组形式
X_list = []
dt_list = []
vl_list = []
mi_list = []

# 收集它得分信息
for user in src_data:
    X_list.append([src_data[user]['dt_score'], src_data[user]['vl_score'], src_data[user]['mi_score']])
# ndarray形式 有207个用户，每个用户有4个属性
data = np.asarray(X_list)
# 这个target应该我们定义吧，这个就先随机一下。。。
# TODO 颜色问题，即target如何确定 dt3学分、vl4学分、mi5学分
y_list = []
# 得分emm 前60优，前50中，差，dt 1 vl 1 mi占2
for user_rank in X_list:
    sort_s = float(user_rank[0] * 3 + user_rank[1] * 4 + user_rank[2] * 5) / (3 + 4 + 5)
    if sort_s > 60:
        y_list.append(1)
    elif sort_s < 50:
        y_list.append(3)
    else:
        y_list.append(2)

# 如果不是按照学分绩，而是简单的看
# for user_score in X_list:
#     user_dt_score = user_score[0]
#     user_vl_score = user_score[1]
#     user_mi_score = user_score[2]
#     if (user_dt_score > 60 and user_vl_score > 60) or (user_dt_score > 60 and user_mi_score > 75) or (
#             user_vl_score > 60 and user_mi_score > 75):
#         y_list.append(1)
#     elif (user_dt_score < 33 and user_vl_score < 33) or (user_dt_score < 33 and user_mi_score < 60) or (
#             user_vl_score < 33 and user_mi_score < 60):
#         y_list.append(3)
#     else:
#         y_list.append(2)
#         print("2=============", user_score)

target = np.array(y_list)

# 搞训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(data, target, random_state=0)

dataFrame = pd.DataFrame(X_train, columns=['dt', 'vl', 'mi'])
# 按照y_train着色啊
colors = list()
palette = {1: "red", 2: "blue", 3: "green"}
for c in y_train:
    colors.append(palette[int(c)])
grr = scatter_matrix(dataFrame, color=colors, figsize=(15, 15), marker='o',
                     hist_kwds={'bins': 20}, s=60, alpha=.8, cmap=mglearn.cm3)
plt.show()
