import datetime
import numpy as np
import matplotlib.pyplot as plt
import json

#此方法主要进行提交次数的可视化分析，target_dim为目标题型


target_dim='dim4'
x_label=[1,2,3,4,5,6,7,8,9,10]
y_label=[0,0,0,0,0,0,0,0,0,0,]
with open("D:\数据科学大作业\BigJob\indicators_of_four_dim.json","r") as fp:
    df=json.load(fp)
    for item in df:
        if(len(df[item][target_dim])>0):
            for sub_item in df[item][target_dim]:
                # print(sub_item[0])
                count=sub_item[0]
                if(count>0 and count<=10):
                    y_label[count-1]+=1
    print(y_label)
plt.plot(x_label,y_label)
plt.title(target_dim)
plt.show()
