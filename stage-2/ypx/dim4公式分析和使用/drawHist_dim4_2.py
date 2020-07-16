import matplotlib.pyplot as plt
import json

# 此方法主要进行debug时间的可视化分析，target_dim为目标题型

# 要检查的题型，树图题目

plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文

target_dim = 'dim4'

times = []
cnt_30min = 0
cnt_60s = 0
cnt_total = 0
src_path = r'E:\0000ProfessionalClass\2_2nd\SMSE\OnGitHub\BigJob\stage-2\ypx\indicators_of_four_dim_filtered.json'
with open(src_path, "r") as fp:
    df = json.load(fp)
    # 每个item是用户
    for item in df:
        if (len(df[item][target_dim]) > 0):
            # sub_item是4个维度的数组，也就是每一道题
            for sub_item in df[item][target_dim]:
                # print(sub_item[0])
                # 1是debug时间
                cnt_total += 1
                debug_time = sub_item[1]
                # 只看多于1分钟
                if debug_time < 60:
                    cnt_60s += 1
                else:
                    times.append(debug_time / 60)
                if debug_time < 30 * 60:
                    cnt_30min += 1
                # # y轴是频数
                # if (count > 0 and count <= 10):
                #     y_label[count - 1] += 1
# 绘制
# plt.plot(x_label, y_label)
plt.hist(times, int(max(times)) + 1)
# 标题
plt.title(target_dim + 'debug时间频数分布')

plt.xlabel('debug时间/分钟，注：只看多于1分钟的样本')
plt.ylabel('频数')
# plt.ylim(0, 200)
plt.show()
print("样本总数", cnt_total)
print("debug时间小于60秒钟样本数", cnt_60s)
print("debug时间小于30分钟样本数", cnt_30min)
print("时间最多", max(times))
