import json
def getRealTime(t):
    return t/(1000)

new_dict={}
with open("../test_data.json",'r',encoding='UTF-8') as load_f:
    load_dict=json.load(load_f)
    for key in load_dict:
       # print("userId"+str(load_dict[key]['user_id']))
        new_dict[load_dict[key]['user_id']]=[]
        for item in load_dict[key]['cases']:
            if(len(item['upload_records'])==0):
                print("0record")
            else:
                case_dict={item['case_id']:getRealTime(item['upload_records'][-1]['upload_time']-item['upload_records'][0]['upload_time'])}
                new_dict[load_dict[key]['user_id']].append(case_dict)
            #print(str(item['case_id'])+"运行时间"+str(getRealTime(item['upload_records'][-1]['upload_time']-item['upload_records'][0]['upload_time'])))
           # print(getRealTime(item['upload_records'][-1]['upload_time']-item['upload_records'][0]['upload_time']))

with open("../sample_readJSON/time.json",'w') as dump_f:
    json.dump(new_dict,dump_f,indent=4)
    print("加载完成")
    dump_f.close()

    #t0=load_dict["3544"]['cases'][0]['upload_records'][-1]['upload_time']-load_dict["3544"]['cases'][0]['upload_records'][0]['upload_time']
    #print(getRealTime(t0))
    #str(getRealTime(load_dict[key]['cases'][0]['upload_records'][-1]['upload_time']-load_dict[key]['cases'][0]['upload_records'][0]['upload_time']