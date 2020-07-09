import json
# 导入json头文件

import os, sys

# json源文件path
src_path = 'short_time_valid_data.json'

# 另存为的路径
ans_path = 'time_valid_data.json'

# 输出信息的文件
log_path = 'logs.txt'
# 临时数据存储
tmp = {}


def get_json_data(srcPath):
    # 定义为只读模型，并定义名称为f，保证源文件不被修改
    with open(srcPath, 'rb') as f:

        log_f = open("logs.txt", 'w+')
        data = json.load(f)
        # 所有人的id
        keys_l = list(data.keys())

        for each_id in keys_l:
            # 这样赋值的话前面是后面的引用
            cases_of_the_id = data[each_id]['cases']
            cases_to_del_of_the_id = []
            for i in range(len(cases_of_the_id)):
                one_case = cases_of_the_id[i]
                upload_records_of_the_case = one_case['upload_records']
                # 第一次满分索引
                first_full = len(upload_records_of_the_case) - 1
                if len(upload_records_of_the_case) == 0:
                    print(each_id, one_case['case_id'],  "===========================")
                    print(upload_records_of_the_case)
                for j in range(len(upload_records_of_the_case)):
                    # 找到第一次满分的索引
                    if 100 - upload_records_of_the_case[j]['score'] <= 0.1:
                        first_full = j
                        break

                for j in range(1, min(len(upload_records_of_the_case), first_full + 1)):
                    time_break = ((upload_records_of_the_case[j]['upload_time'] - upload_records_of_the_case[j - 1][
                        'upload_time']) / (1000 * 60 * 60))

                    # 两次间隔超出24小时，则这一题就不记入我们的统计中
                    if time_break >= 24:
                        # print('time_break', time_break)
                        cases_to_del_of_the_id.append(i)
                        break

            cases_to_del_of_the_id.sort(reverse=True)

            if len(cases_to_del_of_the_id) > 0:
                print('id是', each_id, '要删除的case索引是', cases_to_del_of_the_id, file=log_f)

            for to_del in cases_to_del_of_the_id:
                del cases_of_the_id[to_del]

        tmp = data
        # 将修改后的内容保存在dict中
        # print(data['49405']['cases'])
        f.close()
        # 关闭json读模式

    return tmp
    # 返回dict字典内容


def write_json_data(tmp):
    # 写入json文件

    with open(ans_path, 'w') as r:
        # 定义为写模式，名称定义为r

        json.dump(tmp, r, indent=4)
        # 将dict写入名称为r的文件中

    r.close()
    # 关闭json写模式


the_revised_dict = get_json_data(src_path)
#write_json_data(the_revised_dict)
