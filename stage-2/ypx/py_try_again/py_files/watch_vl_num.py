import matplotlib.pyplot as plt
import json

# 此方法主要进行dim4得分的可视化分析，target_dim为目标题型

# 要检查的题型，树图题目

plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文

# 所以要乘以40.。
target_dim = 'vl_score'
src_path = r'../json_flies/7areas_score.json'
dim4_s = []
cnt_30min = 0
with open(src_path, "r") as fp:
    df = json.load(fp)
    # 每个item是用户
    for item in df:
        dim4_s.append(df[item][target_dim])

# 绘制
# plt.plot(x_label, y_label)
plt.hist(dim4_s, 100)
# 标题
plt.title(target_dim + '得分分布（组距：0.1）')

plt.xlabel(target_dim + '得分')
plt.ylabel('频数')
plt.show()
