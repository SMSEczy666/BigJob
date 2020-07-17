import matplotlib.pyplot as plt
import json

# 此方法主要进行提交次数的可视化分析，target_dim为目标题型

# 要检查的题型，查找排序题目

plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文

target_dim = 'dim3'

counts = []
cnt_1 = 0
cnt_2 = 0
src_path = r'C:\Users\yhd\Desktop\数据科学大作业\BigJob\indicators_of_four_dim_filtered.json'
with open(src_path, "r") as fp:
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
# 绘制
# plt.plot(x_label, y_label)
plt.hist(counts, max(counts))
# 标题
plt.title(target_dim + '提交次数频数分布')
plt.xlabel('答题提交次数')
plt.ylabel('频数')
plt.show()
print("样本总数", len(counts))
print("1次提交", cnt_1)
print("2次提交", cnt_2)