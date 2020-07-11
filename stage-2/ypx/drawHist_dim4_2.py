import matplotlib.pyplot as plt
import json

# 此方法主要进行提交次数的可视化分析，target_dim为目标题型

# 要检查的题型，树图题目

plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文

target_dim = 'dim4'

x_label = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_label = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
times = []
cnt_30min = 0
with open(r"E:\0000ProfessionalClass\2_2nd\SMSE\OnGitHub\BigJob\indicators_of_four_dim.json", "r") as fp:
    df = json.load(fp)
    # 每个item是用户
    for item in df:
        if (len(df[item][target_dim]) > 0):
            # sub_item是4个维度的数组，也就是每一道题
            for sub_item in df[item][target_dim]:
                # print(sub_item[0])
                # 1是debug时间
                debug_time = sub_item[1]
                # 只看小于24小时，大于一分钟
                if debug_time > 10:
                    # debug_time < 24 * 60 * 60 and
                    times.append(debug_time / 60)
                if debug_time < 30 * 60:
                    cnt_30min += 1
                # # y轴是频数
                # if (count > 0 and count <= 10):
                #     y_label[count - 1] += 1
# 绘制
# plt.plot(x_label, y_label)
plt.hist(times, 300)
# 标题
plt.title(target_dim + 'debug时间频数分布')

plt.xlabel('debug时间/分钟，注：只看多于10s的样本')
plt.ylabel('频数')
plt.show()
print(cnt_30min)
