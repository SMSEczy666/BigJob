import json

import numpy as np

src_data = {}
to_save_dict = {}
user_ids = []

src_path = r'../json_flies/indicators_of_four_dim_filtered.json'
outputs_path = r'../json_flies/3areas_score.json'

# 分题型来汇总所有的这些信息
all_dt = {"dim1": [], "dim2": [], "dim3": [], "dim4": []}
all_vl = {"dim1": [], "dim2": [], "dim3": [], "dim4": []}
all_mi = {"dim1": [], "dim2": [], "dim3": [], "dim4": []}
vl_avg = {"dim1": 0.0, "dim2": 0.0, "dim3": 0.0, "dim4": 0.0}
mi_avg = {"dim1": 0.0, "dim2": 0.0, "dim3": 0.0, "dim4": 0.0}
all_user_dt = [{"dim1": 0.0, "dim2": 0.0, "dim3": 0.0, "dim4": 0.0}]
# 形如[{"dim1": [1,2,3], "dim2": [1,2,3], "dim3": [1,2,3], "dim4": [1,2,3]} ]
all_user_4_cases_3_areas_avg = []


def main():
    with open(src_path, "r") as fp:
        global src_data, to_save_dict, user_ids, all_user_4_cases_3_areas_avg
        # 预处理的data
        src_data = json.load(fp)
        fp.close()
        # 所有人的id
        user_ids = list(src_data.keys())
        for each_id in user_ids:
            to_save_dict[each_id] = {
                'dt_score': 0,
                'vl_score': 0,
                'mi_score': 0
            }

        # 经过了下面的循环，完成了用户每个题型的所有题目的均值，这样作为该用户该题型该方面的分数
        for each_user in src_data:
            # 四种题型的各个题目的各个预处理数据
            cases_dims_1 = src_data[each_user]['dim1']
            cases_dims_2 = src_data[each_user]['dim2']
            cases_dims_3 = src_data[each_user]['dim3']
            cases_dims_4 = src_data[each_user]['dim4']
            case1_3areas = [[], [], []]
            case2_3areas = [[], [], []]
            case3_3areas = [[], [], []]
            case4_3areas = [[], [], []]
            for case_dims in cases_dims_1:
                # dt
                case1_3areas[0].append(case_dims[1])
                # vl
                case1_3areas[1].append(case_dims[2])
                # mi
                case1_3areas[2].append(case_dims[3])
            for case_dims in cases_dims_2:
                # dt
                case2_3areas[0].append(case_dims[1])
                # vl
                case2_3areas[1].append(case_dims[2])
                # mi
                case2_3areas[2].append(case_dims[3])
            for case_dims in cases_dims_3:
                # dt
                case3_3areas[0].append(case_dims[1])
                # vl
                case3_3areas[1].append(case_dims[2])
                # mi
                case3_3areas[2].append(case_dims[3])
            for case_dims in cases_dims_4:
                # dt
                case4_3areas[0].append(case_dims[1])
                # vl
                case4_3areas[1].append(case_dims[2])
                # mi
                case4_3areas[2].append(case_dims[3])
            t = {'dim1': [(np.mean(case1_3areas[0])), (np.mean(case1_3areas[1])), (np.mean(case1_3areas[2]))],
                 'dim2': [(np.mean(case2_3areas[0])), (np.mean(case2_3areas[1])), (np.mean(case2_3areas[2]))],
                 'dim3': [(np.mean(case3_3areas[0])), (np.mean(case3_3areas[1])), (np.mean(case3_3areas[2]))],
                 'dim4': [(np.mean(case4_3areas[0])), (np.mean(case4_3areas[1])), (np.mean(case4_3areas[2]))]}
            all_user_4_cases_3_areas_avg.append(t)
        # 经过了上面的循环，完成了用户每个题型的所有题目的均值，这样作为该用户该题型该方面的分数

        # 下面要算出该用户，该题型，该方面的排名分数
        # 得到了这样的汇总表，这样的话就方便得到排名了，因为mi不需要处理，so...
        all_score_in_12areas = {'dim1': [[], []], 'dim2': [[], []], 'dim3': [[], []], 'dim4': [[], []]}
        for i in range(len(all_user_4_cases_3_areas_avg)):
            dict_i = all_user_4_cases_3_areas_avg[i]
            all_score_in_12areas['dim1'][0].append(dict_i['dim1'][0])
            all_score_in_12areas['dim1'][1].append(dict_i['dim1'][1])
            all_score_in_12areas['dim2'][0].append(dict_i['dim2'][0])
            all_score_in_12areas['dim2'][1].append(dict_i['dim2'][1])
            all_score_in_12areas['dim3'][0].append(dict_i['dim3'][0])
            all_score_in_12areas['dim3'][1].append(dict_i['dim3'][1])
            all_score_in_12areas['dim4'][0].append(dict_i['dim4'][0])
            all_score_in_12areas['dim4'][1].append(dict_i['dim4'][1])
        # 升序排就是越小越排名前
        all_score_in_12areas['dim1'][0].sort()
        all_score_in_12areas['dim1'][1].sort()
        all_score_in_12areas['dim2'][0].sort()
        all_score_in_12areas['dim2'][1].sort()
        all_score_in_12areas['dim3'][0].sort()
        all_score_in_12areas['dim3'][1].sort()
        all_score_in_12areas['dim4'][0].sort()
        all_score_in_12areas['dim4'][1].sort()

        # 形如[{"dim1": [99,2,3], "dim2": [1,2,3], "dim3": [1,2,3], "dim4": [1,2,3]} ]
        all_rank_score_4cases_3areas = []
        for i in range(len(all_user_4_cases_3_areas_avg)):
            init_data = all_user_4_cases_3_areas_avg[i]
            t = {"dim1": [], "dim2": [], "dim3": [], "dim4": []}
            t['dim1'].append(
                (all_score_in_12areas['dim1'][0].index(init_data['dim1'][0]) + 1) / len(
                    all_user_4_cases_3_areas_avg) * 100)
            t['dim1'].append(
                (all_score_in_12areas['dim1'][1].index(init_data['dim1'][1]) + 1) / len(
                    all_user_4_cases_3_areas_avg) * 100)
            t['dim2'].append(
                (all_score_in_12areas['dim2'][0].index(init_data['dim2'][0]) + 1) / len(
                    all_user_4_cases_3_areas_avg) * 100)
            t['dim2'].append(
                (all_score_in_12areas['dim2'][1].index(init_data['dim2'][1]) + 1) / len(
                    all_user_4_cases_3_areas_avg) * 100)
            t['dim3'].append(
                (all_score_in_12areas['dim3'][0].index(init_data['dim3'][0]) + 1) / len(
                    all_user_4_cases_3_areas_avg) * 100)
            t['dim3'].append(
                (all_score_in_12areas['dim3'][1].index(init_data['dim3'][1]) + 1) / len(
                    all_user_4_cases_3_areas_avg) * 100)
            t['dim4'].append(
                (all_score_in_12areas['dim4'][0].index(init_data['dim4'][0]) + 1) / len(
                    all_user_4_cases_3_areas_avg) * 100)
            t['dim4'].append(
                (all_score_in_12areas['dim4'][1].index(init_data['dim4'][1]) + 1) / len(
                    all_user_4_cases_3_areas_avg) * 100)
            t['dim1'].append(init_data['dim1'][2])
            t['dim2'].append(init_data['dim2'][2])
            t['dim3'].append(init_data['dim3'][2])
            t['dim4'].append(init_data['dim4'][2])

            all_rank_score_4cases_3areas.append(t)
        # 这样 all_rank_score_4cases_3areas就存了得分了

        # 下面是四种题型分比例
        for i in range(len(all_rank_score_4cases_3areas)):
            i_4cases_3areas = all_rank_score_4cases_3areas[i]
            user_id = user_ids[i]
            to_save_dict[user_id]['dt_score'] = (i_4cases_3areas['dim1'][0] * 1 + i_4cases_3areas['dim2'][0] * 1 +
                                                 i_4cases_3areas['dim3'][0] * 1 + i_4cases_3areas['dim4'][0] * 1) / \
                                                (1 + 1 + 1 + 1)
            to_save_dict[user_id]['vl_score'] = (i_4cases_3areas['dim1'][1] * 1 + i_4cases_3areas['dim2'][1] * 1 +
                                                 i_4cases_3areas['dim3'][1] * 1 + i_4cases_3areas['dim4'][1] * 1) / \
                                                (1 + 1 + 1 + 1)
            to_save_dict[user_id]['mi_score'] = (i_4cases_3areas['dim1'][2] * 1 + i_4cases_3areas['dim2'][2] * 1 +
                                                 i_4cases_3areas['dim3'][2] * 1 + i_4cases_3areas['dim4'][2] * 1) / \
                                                (1 + 1 + 1 + 1)
        with open(outputs_path, 'w+') as r:
            # 定义为写模式，名称定义为r
            json.dump(to_save_dict, r, indent=4)
            # 将dict写入名称为r的文件中
            r.close()

        # 因为貌似不用均值了
        # vl_avg['dim1'] = float(np.mean(all_VL['dim1']))
        # mi_avg['dim1'] = float(np.mean(all_MI['dim1']))
        # vl_avg['dim2'] = float(np.mean(all_VL['dim2']))
        # mi_avg['dim2'] = float(np.mean(all_MI['dim2']))
        # vl_avg['dim3'] = float(np.mean(all_VL['dim3']))
        # mi_avg['dim3'] = float(np.mean(all_MI['dim3']))
        # vl_avg['dim4'] = float(np.mean(all_VL['dim4']))
        # mi_avg['dim4'] = float(np.mean(all_MI['dim4']))


def get_score():
    for each_id in user_ids:
        cases_dims_1 = src_data[each_id]['dim1']
        cases_dims_2 = src_data[each_id]['dim2']
        cases_dims_3 = src_data[each_id]['dim3']
        cases_dims_4 = src_data[each_id]['dim4']
        user_st_score_on_dims = []
        user_vl_score_on_dims = []
        user_mi_score_on_dims = []
        dt_s = 0.0
        vl_s = 0.0
        mi_s = 0.0
        # 在题型1上
        if len(cases_dims_1) > 0:
            # 在dt时间上
            user_dt_on_dim = []
            user_vl_on_dim = []
            user_mi_on_dim = []
            for case_dims in cases_dims_1:
                user_dt_on_dim.append(case_dims[1])
                user_vl_on_dim.append(case_dims[2])
                user_mi_on_dim.append(case_dims[3])
            # mi的分数就是原来指数的均值好了
            user_mi_score_on_dims.append(np.mean(user_mi_on_dim))
            # 其他两个要看排名，算得分，下面的均值就是用户做了这么多题目，只好看均值作为用户的。。
            np.mean(user_dt_on_dim)
            np.mean(user_vl_on_dim)

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
            dt_s += DT_score
            vl_s += VL_score
            mi_s += MI_score
        if len(cases_dims_2) > 0:
            all_DTS_user_i = []
            VL_mean_tool_list = []
            MI_mean_tool_list = []
            for case_dims in cases_dims_2:
                # debug时间
                dt_i = case_dims[1]
                if dt_i < 30 * 60:
                    all_DTS_user_i.append(1)
                else:
                    dts_i = 1 - dt_i / (30 * 60) * 0.01
                    all_DTS_user_i.append(dts_i)
                # 有效行数
                # if case_dims[2] != 0:
                VL_mean_tool_list.append(vl_avg['dim2'] / case_dims[2])
                # MI指数
                MI_mean_tool_list.append(np.square(case_dims[3] / mi_avg['dim2']))
            DT_score = np.mean(all_DTS_user_i)
            VL_score = np.mean(VL_mean_tool_list)
            MI_score = np.mean(MI_mean_tool_list)
            dt_s += DT_score
            vl_s += VL_score
            mi_s += MI_score

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
            dt_s += DT_score
            vl_s += VL_score
            mi_s += MI_score

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
            dt_s += DT_score
            vl_s += VL_score
            mi_s += MI_score
        # 3.2 3.8
        to_save_dict[each_id]['DT_score'] = dt_s
        to_save_dict[each_id]['VL_score'] = vl_s
        to_save_dict[each_id]['MI_score'] = mi_s

    with open(outputs_path, 'w+') as r:
        # 定义为写模式，名称定义为r
        json.dump(to_save_dict, r, indent=4)
        # 将dict写入名称为r的文件中
        r.close()


if __name__ == "__main__":
    main()
