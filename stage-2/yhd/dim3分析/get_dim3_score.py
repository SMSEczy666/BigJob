import json

import numpy as np

target_dim = 'dim3'

x_label = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y_label = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
src_data = {}
all_VL = []  # 2索引
all_MI = []  # 3索引
vl_avg = 0.0
mi_avg = 0.0
to_save_dict = {}
user_ids = []
outputs_path = r'C:\Users\yhd\Desktop\数据科学大作业\BigJob\stage-2\yhd\dim3_ans.json'
src_path = r"C:\Users\yhd\Desktop\数据科学大作业\BigJob\indicators_of_four_dim_filtered.json"


def main():
    with open(src_path, "r") as fp:
        global src_data, vl_avg, mi_avg, to_save_dict, user_ids
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
            cases_dims = src_data[each_user][target_dim]
            for case_dims in cases_dims:
                # 有效行数
                all_VL.append(case_dims[2])
                # MI指数
                all_MI.append(case_dims[3])

        vl_avg = np.mean(all_VL)
        mi_avg = np.mean(all_MI)


def get_score():
    for each_id in user_ids:
        cases_dims = src_data[each_id][target_dim]
        if len(cases_dims) > 0:
            all_DTS_user_i = []
            VL_mean_tool_list = []
            MI_mean_tool_list = []
            for case_dims in cases_dims:
                # debug时间
                dt_i = case_dims[1]
                if dt_i < 30 * 60:
                    all_DTS_user_i.append(1)
                else:
                    dts_i = 1 - dt_i / (30 * 60) * 0.01
                    all_DTS_user_i.append(dts_i)
                # 有效行数
                # if case_dims[2] != 0:
                VL_mean_tool_list.append(vl_avg / case_dims[2])
                # MI指数
                MI_mean_tool_list.append(np.square(case_dims[3] / mi_avg))
            DT_score = np.mean(all_DTS_user_i)
            VL_score = np.mean(VL_mean_tool_list)
            MI_score = np.mean(MI_mean_tool_list)
            to_save_dict[each_id][target_dim] = DT_score + VL_score + MI_score

    with open(outputs_path, 'w+') as r:
        # 定义为写模式，名称定义为r
        json.dump(to_save_dict, r, indent=4)
        # 将dict写入名称为r的文件中
        r.close()


if __name__ == "__main__":
    main()
    get_score()
    print("vl_avg", vl_avg)
    print("mi_avg", mi_avg)