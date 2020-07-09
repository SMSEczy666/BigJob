import json
import os
import urllib.parse
import urllib.request
import time

file_n_s = 'half_test_data'
file_n_e = 'test_data'
# 忘记文件名怎么取的
file_n_p = 'sample'
f = open(file_n_p + '.json', encoding='utf-8')  # 打开json文件
res = f.read()
data = json.loads(res)  # 加载json数据
# print(data)
# 所有人的id
keys_l = list(data.keys())
for i in range(len(keys_l)):
    user_info = data[keys_l[i]]
    user_id = user_info['user_id']
    # id下做的所有题目
    cases = user_info['cases']
    # 对于每一题
    for case in cases:
        # 获取文件名，url里对中文会urlencode，所以解个码
        filename = urllib.parse.unquote(os.path.basename(case["case_zip"]))
        # 如果有不能作为文件名的字符出现，就将其替换为空格
        intab = '*:?/\\<>|"'
        for t in intab:
            if t in filename:
                filename = filename.replace(t, ' ')
        # json给出的最终提交版所在网址有中文，要解码得url_
        url_ = urllib.parse.quote(case["case_zip"], safe='/:?=')
        # 存储在本地的路径，如果路径不存在就建立
        path = 'E:\\新桌面\\数据科学大作业\\' + file_n_e + '\\' + 'user' + str(user_id) + '\\' + case[
            "case_type"] + '\\' + str(case['case_id']) + '_final_score_' + str(case['final_score']) + '\\'
        if not os.path.exists(path):
            os.makedirs(path)
        path_final_case = path + filename
        # 下载最终版题目包到本地
        urllib.request.urlretrieve(url_, path_final_case)
        # 准备下载提交记录
        path_records = path + 'upload_records\\'
        records = case['upload_records']
        for j in range(len(records)):
            rec = records[j]
            # 时间戳是毫秒记的
            timestamp = float(rec['upload_time'])
            timestamp /= 1000
            timeArray = time.localtime(timestamp)
            otherStyleTime = time.strftime("%Y-%m-%d %H.%M.%S", timeArray)
            path_rec = path_records + otherStyleTime + '\\'
            if not os.path.exists(path_rec):
                os.makedirs(path_rec)
            path_rec_ = path_rec + filename
            rec_url = rec['code_url']
            # print(rec_url)
            # 下载提交的内容到本地
            urllib.request.urlretrieve(rec_url, path_rec_)

