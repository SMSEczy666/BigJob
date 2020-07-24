# Libraries
import json
import matplotlib.pyplot as plt
import pandas as pd
from math import pi

src_path = r'../json_flies/7areas_score.json'
plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文
with open(src_path, "r") as fp:
    # 预处理的data
    src_data = json.load(fp)
    fp.close()
    # 所有人的id
    user_ids = list(src_data.keys())
    for each_id in user_ids:
        plt.clf()
        df = pd.DataFrame({
            'group': ['userA'],
            '题型四': [src_data[each_id]['case4']],
            'mi指数': [src_data[each_id]['mi_score']],
            '代码简洁性': [src_data[each_id]['vl_score']],
            'debug能力': [src_data[each_id]['dt_score']],
            '题型一': [src_data[each_id]['case1']],
            '题型二': [src_data[each_id]['case2']],
            '题型三': [src_data[each_id]['case3']]
        })

        out_path = '../pngs/radar_chart' + '_user_' + each_id + '.png'

        # number of variable
        categories = list(df)[1:]
        N = len(categories)

        # We are going to plot the first line of the data frame.
        # But we need to repeat the first value to close the circular graph: 这个不懂，为啥要
        # [0]就是第一个人
        values = df.loc[0].drop('group').values.flatten().tolist()
        values += values[:1]
        print(values)

        # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
        angles = [n / float(N) * 2 * pi for n in range(N)]
        angles += angles[:1]

        # Initialise the spider plot 一行一列位置1 polar是极点图
        ax = plt.subplot(1, 1, 1, polar=True)

        # Draw one axe per variable + add labels labels yet
        # 逆时针写各个维度的值
        plt.xticks(angles[:-1], categories, color='grey', size=8)

        # 设置极径标签显示位置
        ax.set_rlabel_position(0)
        plt.yticks([20, 40, 60, 80], ["20", "40", "60", "80"], color="grey",
                   size=7)
        plt.ylim(0, 100)

        # Plot data
        ax.plot(angles, values, linewidth=1, linestyle='solid')

        # Fill area
        ax.fill(angles, values, 'black', alpha=0.2)
        plt.savefig(out_path)
