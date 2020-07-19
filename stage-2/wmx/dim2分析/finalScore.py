import json
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']#显示中文

def calDebugTimeSocore(list):
    sumScore=0
    n=0
    for subItem in list:
        n+=1
        if(subItem[1]<30*60):
            sumScore+=1
        elif(subItem[1]>=30*60 and subItem[1]<130*60):
            sumScore+=1-((subItem[1]-30*60)/60)*0.01
        else:
            sumScore+=0
    return sumScore/n

def calLineScore(list,avgLine):
    n=0
    sumScore=0
    for subItem in list:
        n+=1
        sumScore+=avgLine/subItem[2]
    return sumScore/n

def calMIScore(list,avgMi):
    n=0
    sumScore=0
    for subItem in list:
        n+=1
        sumScore+=(avgMi/subItem[3])**2
    return sumScore/n

target_dim="dim2"
count=0
time_list=[]
line_list=[]
mi_list=[]
sumLine=0
sumMI=0
with open("../../../indicators_of_four_dim_filtered.json",'r') as fp:
    df=json.load(fp)
    for item in df:
        if(len(df[item][target_dim])>0):
            time_list.append(calDebugTimeSocore(df[item][target_dim]))
            for subItem in df[item][target_dim]:
                count+=1
                sumLine+=subItem[2]
                sumMI+=subItem[3]
    avgLine=sumLine/count
    avgMI=sumMI/count
    for item in df:
        if(len(df[item][target_dim])>0):
            line_list.append(calLineScore(df[item][target_dim],avgLine))
            mi_list.append(calMIScore(df[item][target_dim],avgMI))
score_list=[]
for i in range(0,len(time_list)):
    score_list.append(0.5*time_list[i]+line_list[i]+1.5*mi_list[i])
plt.hist(score_list,50)
plt.xlabel("得分")
plt.ylabel("频数")
plt.show()



