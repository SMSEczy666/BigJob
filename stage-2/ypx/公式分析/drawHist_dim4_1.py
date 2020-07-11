import datetime
import numpy as np
import matplotlib.pyplot as plt
import json

# 此方法主要进行提交次数的可视化分析，target_dim为目标题型

# 要检查的题型，树图题目

plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文

target_dim = 'dim4'

x_label = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_label = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
counts = []
cnt_1 = 0
cnt_2 = 0
with open(r"E:\0000ProfessionalClass\2_2nd\SMSE\OnGitHub\BigJob\indicators_of_four_dim.json", "r") as fp:
    df = json.load(fp)
    # 每个item是用户
    for item in df:
        if (len(df[item][target_dim]) > 0):
            # sub_item是4个维度的数组，也就是每一道题
            for sub_item in df[item][target_dim]:
                # print(sub_item[0])
                # 0号是次数
                count = sub_item[0]
                if count == 1:
                    cnt_1 += 1
                if count == 2:
                    cnt_2 += 1
                counts.append(count)
                # # y轴是频数
                # if (count > 0 and count <= 10):
                #     y_label[count - 1] += 1
    print(y_label)
# 绘制
# plt.plot(x_label, y_label)
plt.hist(counts, 300)
# 标题
plt.title(target_dim + '提交次数频数分布')
plt.xlabel('答题提交次数')
plt.ylabel('频数')
plt.show()
print("1次提交", cnt_1)
print("2次提交", cnt_2)

