import matplotlib.mlab as mlab
import json
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']#显示中文
import numpy as np
from scipy.stats import norm
mu=1000
x=[]
with open("D:\数据科学大作业\BigJob\indicators_of_four_dim.json","r") as fp:
    df=json.load(fp)
    for item in df:
        if(len(df[item]['dim1'])>0):
            for subitem in df[item]['dim1']:
                if(subitem[1]>10000):
                    x.append(subitem[1])

##区间数
num_bins=400
n,bins,patches=plt.hist(x,num_bins)

plt.xlabel('mi指数')

plt.ylabel('频数')

plt.title(r'mi指数分布情况直方图')

plt.show()
