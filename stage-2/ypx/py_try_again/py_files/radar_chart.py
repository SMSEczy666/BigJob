# Libraries
import matplotlib.pyplot as plt
import pandas as pd
from math import pi

out_path = r'../pngs/radar_chart.png'
# Set data
df = pd.DataFrame({
    'group': ['userA', 'B', 'C', 'D'],
    'var1': [70, 1.5, 30, 4],
    'var2': [60, 10, 9, 34],
    'var3': [80, 39, 23, 24],
    'var4': [93, 31, 33, 14],
    'var5': [56, 15, 32, 14],
    'var6': [70, 15, 32, 14],
    'var7': [20, 15, 32, 14]
})

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
print(angles)

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
plt.show()
