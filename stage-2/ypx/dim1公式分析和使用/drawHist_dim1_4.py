import matplotlib.pyplot as plt
import json

# 此方法主要进行MI指数的可视化分析，target_dim为目标题型

# 要检查的题型，树图题目

plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文

target_dim = 'dim1'

lines = []
src_path = r'E:\0000ProfessionalClass\2_2nd\SMSE\OnGitHub\BigJob\indicators_of_four_dim_filtered.json'
with open(src_path, "r") as fp:
    df = json.load(fp)
    # 每个item是用户
    for item in df:
        if (len(df[item][target_dim]) > 0):
            # sub_item是4个维度的数组，也就是每一道题
            for sub_item in df[item][target_dim]:
                # print(sub_item[0])
                # 2是有效行数
                # 只看小于24小时，大于一分钟
                # debug_time < 24 * 60 * 60 and
                lines.append(sub_item[3])
            # # y轴是频数
            # if (count > 0 and count <= 10):
            #     y_label[count - 1] += 1
# 绘制
# plt.plot(x_label, y_label)
plt.hist(lines, 100)
# 标题
plt.title(target_dim + 'mi指数频数分布')

plt.xlabel('mi指数（范围0-100）')
plt.ylabel('频数')
plt.show()
