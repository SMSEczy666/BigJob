import json

import numpy as np

src_data = {}
to_save_dict = {}
user_ids = []

all_VL = {"dim1": [], "dim3": [], "dim4": []}  # 2索引
all_MI = {"dim1": [], "dim3": [], "dim4": []}  # 3索引
vl_avg = {"dim1": 0.0, "dim3": 0.0, "dim4": 0.0}
mi_avg = {"dim1": 0.0, "dim3": 0.0, "dim4": 0.0}

outputs_path = r'E:\Desktop\stage_2_user_scores.json'
src_path = r"E:\Desktop\indicators_of_four_dim_filtered.json"
# dim2中的全局变量
count_dim2 = 0
time_list_dim2 = []
line_list_dim2 = []
mi_list_dim2 = []
sumLine_dim2 = 0
sumMI_dim2 = 0


def calDebugTimeSocore(list):
    sumScore = 0
    n = 0
    for subItem in list:
        n += 1
        if (subItem[1] < 30 * 60):
            sumScore += 1
        elif (subItem[1] >= 30 * 60 and subItem[1] < 130 * 60):
            sumScore += 1 - ((subItem[1] - 30 * 60) / 60) * 0.01
        else:
            sumScore += 0
    return sumScore / n


def calLineScore(list, avgLine):
    n = 0
    sumScore = 0
    for subItem in list:
        n += 1
        sumScore += avgLine / subItem[2]
    return sumScore / n


def calMIScore(list, avgMi):
    n = 0
    sumScore = 0
    for subItem in list:
        n += 1
        sumScore += (avgMi / subItem[3]) ** 2
    return sumScore / n


def main():
    with open(src_path, "r") as fp:
        global src_data, to_save_dict, user_ids, count_dim2, sumLine_dim2, sumMI_dim2, all_VL, all_MI
        src_data = json.load(fp)
        fp.close()
        # 所有人的id
        user_ids = list(src_data.keys())
        for each_id in user_ids:
            to_save_dict[each_id] = {
                'dim1': 0,
                'dim2': 0,
                'dim3': 0,
                'dim4': 0
            }
        # 获取所有的值
        for each_user in src_data:
            cases_dims_1 = src_data[each_user]['dim1']
            cases_dims_2 = src_data[each_user]['dim2']
            cases_dims_3 = src_data[each_user]['dim3']
            cases_dims_4 = src_data[each_user]['dim4']

            # dim2部分
            if (len(cases_dims_2) > 0):
                time_list_dim2.append(calDebugTimeSocore(cases_dims_2))
                for subItem in cases_dims_2:
                    count_dim2 += 1
                    sumLine_dim2 += subItem[2]
                    sumMI_dim2 += subItem[3]
            # dim2结束

            for case_dims in cases_dims_1:
                # 有效行数
                all_VL['dim1'].append(case_dims[2])
                # MI指数
                all_MI['dim1'].append(case_dims[3])
            for case_dims in cases_dims_3:
                # 有效行数
                all_VL['dim3'].append(case_dims[2])
                # MI指数
                all_MI['dim3'].append(case_dims[3])
            for case_dims in cases_dims_4:
                # 有效行数
                all_VL['dim4'].append(case_dims[2])
                # MI指数
                all_MI['dim4'].append(case_dims[3])

        # dim2
        avgLine_dim2 = sumLine_dim2 / count_dim2
        avgMI_dim2 = sumMI_dim2 / count_dim2
        for item in src_data:
            if (len(src_data[item]['dim2']) > 0):
                line_list_dim2.append(calLineScore(src_data[item]['dim2'], avgLine_dim2))
                mi_list_dim2.append(calMIScore(src_data[item]['dim2'], avgMI_dim2))
        # dim2结束

        vl_avg['dim1'] = float(np.mean(all_VL['dim1']))
        mi_avg['dim1'] = float(np.mean(all_MI['dim1']))
        vl_avg['dim3'] = float(np.mean(all_VL['dim3']))
        mi_avg['dim3'] = float(np.mean(all_MI['dim3']))
        vl_avg['dim4'] = float(np.mean(all_VL['dim4']))
        mi_avg['dim4'] = float(np.mean(all_MI['dim4']))


def get_score():
    global time_list_dim2
    for each_id in user_ids:
        cases_dims_1 = src_data[each_id]['dim1']
        cases_dims_3 = src_data[each_id]['dim3']
        cases_dims_4 = src_data[each_id]['dim4']

        if len(cases_dims_1) > 0:
            all_DTS_user_i = []
            VL_mean_tool_list = []
            MI_mean_tool_list = []
            for case_dims in cases_dims_1:
                # debug时间
                dt_i = case_dims[1]
                if dt_i < 30 * 60:
                    all_DTS_user_i.append(1)
                else:
                    dts_i = 1 - dt_i / (30 * 60) * 0.01
                    all_DTS_user_i.append(dts_i)
                # 有效行数
                # if case_dims[2] != 0:
                VL_mean_tool_list.append(vl_avg['dim1'] / case_dims[2])
                # MI指数
                MI_mean_tool_list.append(np.square(case_dims[3] / mi_avg['dim1']))
            DT_score = np.mean(all_DTS_user_i)
            VL_score = np.mean(VL_mean_tool_list)
            MI_score = np.mean(MI_mean_tool_list)
            to_save_dict[each_id]['dim1'] = DT_score + VL_score + MI_score

        if len(cases_dims_3) > 0:
            all_DTS_user_i = []
            VL_mean_tool_list = []
            MI_mean_tool_list = []
            for case_dims in cases_dims_3:
                # debug时间
                dt_i = case_dims[1]
                if dt_i < 30 * 60:
                    all_DTS_user_i.append(1)
                else:
                    dts_i = 1 - dt_i / (30 * 60) * 0.01
                    all_DTS_user_i.append(dts_i)
                # 有效行数
                # if case_dims[2] != 0:
                VL_mean_tool_list.append(vl_avg['dim3'] / case_dims[2])
                # MI指数
                MI_mean_tool_list.append(np.square(case_dims[3] / mi_avg['dim3']))
            DT_score = np.mean(all_DTS_user_i)
            VL_score = np.mean(VL_mean_tool_list)
            MI_score = np.mean(MI_mean_tool_list)
            to_save_dict[each_id]['dim3'] = DT_score + VL_score + MI_score

        if len(cases_dims_4) > 0:
            all_DTS_user_i = []
            VL_mean_tool_list = []
            MI_mean_tool_list = []
            for case_dims in cases_dims_4:
                # debug时间
                dt_i = case_dims[1]
                if dt_i < 30 * 60:
                    all_DTS_user_i.append(1)
                else:
                    dts_i = 1 - dt_i / (30 * 60) * 0.01
                    all_DTS_user_i.append(dts_i)
                # 有效行数
                # if case_dims[2] != 0:
                VL_mean_tool_list.append(vl_avg['dim4'] / case_dims[2])
                # MI指数
                MI_mean_tool_list.append(np.square(case_dims[3] / mi_avg['dim4']))
            DT_score = np.mean(all_DTS_user_i)
            VL_score = np.mean(VL_mean_tool_list)
            MI_score = np.mean(MI_mean_tool_list)
            to_save_dict[each_id]['dim4'] = DT_score + VL_score + MI_score

    # dim2部分
    for i in range(0, len(time_list_dim2)):
        to_save_dict[user_ids[i]]['dim2'] = 0.5 * time_list_dim2[i] + line_list_dim2[i] + 1.5 * mi_list_dim2[i]
    # dim2部分

    with open(outputs_path, 'w+') as r:
        # 定义为写模式，名称定义为r
        json.dump(to_save_dict, r, indent=4)
        # 将dict写入名称为r的文件中
        r.close()


if __name__ == "__main__":
    main()
    get_score()
