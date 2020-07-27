import json
import time
import subprocess
import os
import chardet

# 在已经处理好时间的json上搞
p2 = 'short_time_valid_data.json'
p1 = 'time_valid_data.json'
p3 = 'super_short_time_valid_data.json'
src_json_path = p1

ans_json_path = 'E:/新桌面/indicators_of_four_dim_v1.json'

to_save_dict = {}


def handle_json_data(src_path):
    with open(src_path, 'rb') as src_json_file:
        json_data = json.load(src_json_file)
        # 所有人的id
        keys_l = list(json_data.keys())
        log_f = open(r"E:\新桌面\logs_when_getting_indicators_v1.txt", 'w+')
        for each_id in keys_l:
            the_id = each_id
            to_save_dict[the_id] = {
                'dim1': [],
                'dim2': [],
                'dim3': [],
                'dim4': []
            }
            cases_of_the_id = json_data[the_id]['cases']
            for i in range(len(cases_of_the_id)):
                the_case = cases_of_the_id[i]
                c_i = the_case['case_id']
                c_t = the_case['case_type']
                f_s = the_case['final_score']
                upload_records_of_the_case = the_case['upload_records']
                # 第一次满分索引
                first_full = len(upload_records_of_the_case) - 1
                # 直接到下一个循环
                if len(upload_records_of_the_case) == 0:
                    continue
                for j in range(len(upload_records_of_the_case)):
                    # 找到第一次满分的索引
                    if 100 - upload_records_of_the_case[j]['score'] <= 0.1:
                        first_full = j
                        break

                for_name_timestamp = time.localtime(float(upload_records_of_the_case[first_full]['upload_time']) / 1000)
                time_name = time.strftime("%Y-%m-%d %H.%M.%S", for_name_timestamp)

                # 即使没有满分，提交次数和debug时间也是正确的
                my_upload_cnt = first_full + 1
                # 单位秒
                my_debug_time = (upload_records_of_the_case[first_full]['upload_time'] - upload_records_of_the_case[0][
                    'upload_time']) / 1000

                # 下面是找到那个py文件
                py_file_path = 'E:\\新桌面\\test_data\\test_data\\user' + str(
                    the_id) + '\\' + c_t + '\\' + c_i + '_final_score_' + str(
                    f_s) + '\\upload_records\\' + time_name + '\\main.py'
                if not os.path.exists(py_file_path):
                    print("user", the_id, "case", c_i, "record", time_name,
                          "===========没有找到upload_records里面的main.py======",
                          file=log_f)
                    continue
                tmp_py_file_path = 'E:\\新桌面\\gbk_py_files_v1\\user' + str(the_id) + '\\'
                if not os.path.exists(tmp_py_file_path):
                    os.makedirs(tmp_py_file_path)
                tmp_py_file_path += 'case' + c_i + ".py"
                d_p_f = {}
                tmp_to_j = open(py_file_path, 'rb')

                if chardet.detect(tmp_to_j.read())['encoding'] == 'utf-8':
                    print("转")
                    py_file_p_f = open(py_file_path, 'r', encoding='utf-8')
                    d_p_f = py_file_p_f.read().encode('utf-8').decode('gbk', errors="ignore")
                else:
                    py_file_p_f = open(py_file_path, 'r', encoding='gbk', errors="ignore")
                    d_p_f = py_file_p_f.read()

                with open(tmp_py_file_path, 'w', encoding='gbk') as tmp_py_file_p_f:
                    tmp_py_file_p_f.write("")
                    tmp_py_file_p_f.write(d_p_f)
                    tmp_py_file_p_f.close()
                print("user", the_id, "case", c_i, "===========搞过啦=============")

                my_cnt_line = get_line_from_file(tmp_py_file_path)
                dim_num = 0
                if c_t == '数字操作' or c_t == '数组':
                    dim_num = 1
                elif c_t == '线性表' or c_t == '字符串':
                    dim_num = 2
                elif c_t == '查找算法' or c_t == '排序算法':
                    dim_num = 3
                elif c_t == '树结构' or c_t == '图结构':
                    dim_num = 4
                dim_name = 'dim' + str(dim_num)

                # TODO
                tmp_mi_p = "E:\\新桌面\\mi_of_cases_v1\\user" + the_id + "\\"
                if not os.path.exists(tmp_mi_p):
                    os.makedirs(tmp_mi_p)
                tmp_mi_p += "case" + c_i + ".json"
                get_mi_json_from_powershell(tmp_py_file_path, tmp_mi_p)
                try:
                    with open(tmp_mi_p, 'r') as tmp_mi_json_file:
                        tmp_mi_json_data = json.load(tmp_mi_json_file)
                        keys_l = list(tmp_mi_json_data.keys())
                        my_mi = float(tmp_mi_json_data[keys_l[0]]['mi'])
                    tmp_mi_json_file.close()
                except KeyError:
                    print("user", the_id, "case", c_i, "=============没有mi可能不是Python写的================", file=log_f)
                    continue

                to_save_dict[the_id][dim_name].append([my_upload_cnt, my_debug_time, my_cnt_line, my_mi])

    src_json_file.close()

    with open(ans_json_path, 'w+') as r:
        # 定义为写模式，名称定义为r
        json.dump(to_save_dict, r, indent=4)
        # 将dict写入名称为r的文件中
        r.close()


def get_line_from_file(filename):
    line_list = []
    with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
        # 按行访问
        for line in f:
            try:
                # 每行添加到列表，返回列表
                line_list.append(line)
            except IOError:
                pass
    count = len(line_list)
    for i in range(len(line_list)):
        content = line_list[i]
        if content == '\n':
            count -= 1
        else:
            for j in range(len(content)):
                if content[j] != " ":
                    if content[j] == "#":
                        count -= 1
                        break
                    else:
                        break
    f.close()
    return count


def get_mi_json_from_powershell(src_py_f, ans_json_f):
    try:
        args = [r"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe", "-ExecutionPolicy", "Unrestricted",
                r"E:\新桌面\radon_mi.ps1",
                src_py_f, ans_json_f]
        p = subprocess.Popen(args, stdout=subprocess.PIPE)
        dt = p.stdout.read()
        return dt
    except Exception:
        print("exception")
        return False


if __name__ == "__main__":
    handle_json_data(src_json_path)
