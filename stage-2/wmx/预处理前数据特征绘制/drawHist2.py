import matplotlib.mlab as mlab
import json
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']#显示中文

target_dim='dim1'
x=[]
with open("D:\数据科学大作业\BigJob\indicators_of_four_dim.json","r") as fp:
    df=json.load(fp)
    for item in df:
        if(len(df[item][target_dim])>0):
            for subitem in df[item][target_dim]:
                if(subitem[1]>10000): #subitem中的数字(此处为1)表示要取4项指标中的哪一项
                    x.append(subitem[1])

##区间数
num_bins=400

plt.hist(x,num_bins)

plt.xlabel('mi指数')

plt.ylabel('频数')

plt.title(r'mi指数分布情况直方图')

plt.show()
