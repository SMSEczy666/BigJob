import matplotlib.pyplot as plt
import json

# 此方法主要进行dim4得分的可视化分析，target_dim为目标题型

# 要检查的题型，树图题目

plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文

target_dim = 'dim1'
src_path = r'E:\Desktop\dim1_ans.json'
dim4_s = []
cnt_30min = 0
with open(src_path, "r") as fp:
    df = json.load(fp)
    # 每个item是用户
    for item in df:
        dim4_s.append(df[item][target_dim])
        if df[item][target_dim] > 30:
            print(item)

# 绘制
# plt.plot(x_label, y_label)
plt.hist(dim4_s, int(max(dim4_s)) * 10 + 1)
# 标题
plt.title(target_dim + '得分分布（组距：0.1）')

plt.xlabel('dim1得分')
plt.ylabel('频数')
plt.show()
