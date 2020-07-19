import json
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']#显示中文
outputs_path = r"D:\数据科学大作业\BigJob\stage-2\wmx\按能力分（debug,简洁性,mi指数)\3ability_data.json"
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
        if(subItem[3]>0):
            n+=1
            sumScore+=(avgMi/subItem[3])**2
    return sumScore/n

target_dims=["dim1","dim2","dim3","dim4"]
user_ids=[]
counts=[]
avg_lines=[]
avg_mis=[]
time_list_dim1=[]
time_list_dim2=[]
time_list_dim3=[]
time_list_dim4=[]
user_time_list=[]
line_list_dim1=[]
line_list_dim2=[]
line_list_dim3=[]
line_list_dim4=[]
user_line_list=[]
mi_list_dim1=[]
mi_list_dim2=[]
mi_list_dim3=[]
mi_list_dim4=[]
user_mi_list=[]
sumLine=0
sumMI=0
count=0
with open("../../../indicators_of_four_dim_filtered.json",'r') as fp:
    df=json.load(fp)
    for item in df:
        if(len(df[item]["dim1"])):
            user_ids.append(item)
        for target_dim in target_dims:
            if (len(df[item][target_dim]) > 0):

                if(target_dim=="dim1"):
                    time_list_dim1.append(calDebugTimeSocore(df[item][target_dim]))
                    for subItem in df[item][target_dim]:
                        count += 1
                        sumLine += subItem[2]
                        sumMI += subItem[3]
                    avg_lines.append(sumLine/count)
                    avg_mis.append(sumMI/count)
                    sumLine = 0
                    sumMI = 0
                    count = 0
                elif(target_dim=="dim2"):
                    time_list_dim2.append(calDebugTimeSocore(df[item][target_dim]))
                    for subItem in df[item][target_dim]:
                        count += 1
                        sumLine += subItem[2]
                        sumMI += subItem[3]
                    avg_lines.append(sumLine/count)
                    avg_mis.append(sumMI/count)
                    sumLine = 0
                    sumMI = 0
                    count = 0
                elif(target_dim=="dim3"):
                    time_list_dim3.append(calDebugTimeSocore(df[item][target_dim]))
                    for subItem in df[item][target_dim]:
                        count += 1
                        sumLine += subItem[2]
                        sumMI += subItem[3]
                    avg_lines.append(sumLine/count)
                    avg_mis.append(sumMI/count)
                    sumLine = 0
                    sumMI = 0
                    count = 0
                else:
                    time_list_dim4.append(calDebugTimeSocore(df[item][target_dim]))
                    for subItem in df[item][target_dim]:
                        count += 1
                        sumLine += subItem[2]
                        sumMI += subItem[3]
                    avg_lines.append(sumLine/count)
                    avg_mis.append(sumMI/count)
                    sumLine = 0
                    sumMI = 0
                    count = 0
    for item in df:
        for target_dim in target_dims:
            if (len(df[item][target_dim]) > 0):
                if(target_dim=="dim1"):
                    line_list_dim1.append(calLineScore(df[item][target_dim], avg_lines[0]))
                    mi_list_dim1.append(calMIScore(df[item][target_dim], avg_mis[0]))
                elif(target_dim=="dim2"):
                    line_list_dim2.append(calLineScore(df[item][target_dim], avg_lines[1]))
                    mi_list_dim2.append(calMIScore(df[item][target_dim], avg_mis[1]))
                elif(target_dim=="dim3"):
                    line_list_dim3.append(calLineScore(df[item][target_dim], avg_lines[2]))
                    mi_list_dim3.append(calMIScore(df[item][target_dim], avg_mis[2]))
                else:
                    line_list_dim4.append(calLineScore(df[item][target_dim], avg_lines[3]))
                    mi_list_dim4.append(calMIScore(df[item][target_dim], avg_mis[3]))

for i in range(0,207):
    user_time_list.append(time_list_dim1[i]+time_list_dim2[i]+time_list_dim3[i]+time_list_dim4[i])
    user_line_list.append(line_list_dim1[i]+line_list_dim2[i]+line_list_dim3[i]+line_list_dim4[i])
    user_mi_list.append(mi_list_dim1[i]+mi_list_dim2[i]+mi_list_dim3[i]+mi_list_dim4[i])

to_save_dict = {}
for each_id in user_ids:
    to_save_dict[each_id] = {
            'debug_time':0.0,
            'code_line':0.0,
            'mi_score':0.0
    }
i=0
for user_id in user_ids:
    to_save_dict[user_id]['debug_time']=user_time_list[i]
    to_save_dict[user_id]['code_line']=user_line_list[i]
    to_save_dict[user_id]['mi_score']=user_mi_list[i]
    i+=1
    with open(outputs_path, 'w+') as r:
        # 定义为写模式，名称定义为r
        json.dump(to_save_dict, r)
        # 将dict写入名称为r的文件中
        r.close()




