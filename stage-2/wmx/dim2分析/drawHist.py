import json
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']#显示中文

target_dim="dim2" #目标分析题型为dim2

x1=[] #提交次数
x21=[] #debug时间(一分钟以上)（数据预处理中舍去了超过24小时的样本）
x22=[]
x3=[] #代码有效行数
x4=[] #mi指数
count=0
count_oneMinute=0
count_30Minute=0
count_1submit=0
count_50line=0
count_100mi=0
with open("../../../indicators_of_four_dim_filtered.json",'r') as fp:
    df=json.load(fp)
    for item in df:
        if(len(df[item][target_dim])>0):
            for sub_item in df[item][target_dim]:
                count+=1
                if(sub_item[0]==1):
                    count_1submit+=1
                if(sub_item[2]<=50):
                    count_50line+=1
                if(sub_item[3]>100):
                    count_100mi+=1
                x1.append(sub_item[0])
                x3.append(sub_item[2])
                x4.append(sub_item[3])
                if(sub_item[1]>60):
                    x21.append(sub_item[1])
                    count_oneMinute+=1
                if(sub_item[1]>60*30):
                    x22.append(sub_item[1])
                    count_30Minute+=1
num_bins=[50,500,50,50]
plt.hist(x1,num_bins[0])
plt.xlabel("提交次数")
plt.ylabel("频数")
plt.title(r"提交次数分布情况")
plt.show()

plt.hist(x21,num_bins[1])
plt.xlabel("debug时间(超过1分钟)")
plt.ylabel("频数")
plt.title(r"debug时间分布情况(超过一分钟)")
plt.show()

plt.hist(x22,num_bins[1])
plt.xlabel("debug时间（超过30分钟)")
plt.ylabel("频数")
plt.title(r"debug时间分布情况(超过三十分钟)")
plt.show()

plt.hist(x3,num_bins[2])
plt.xlabel("有效代码行数")
plt.ylabel("频数")
plt.title(r"有效代码行数分布情况")
plt.show()

plt.hist(x4,num_bins[3])
plt.xlabel("mi指数")
plt.ylabel("频数")
plt.title(r"mi指数分布情况")
plt.show()

print("有效样本数目"+str(count))
print("只提交了一次的样本数目"+str(count_1submit))
print("debug时间超过1分钟的样本数"+str(count_oneMinute))
print("debug时间超过30分钟的样本数"+str(count_30Minute))
print("有效代码行数小于50行的样本数"+str(count_50line))
print(count_100mi)


