import json

import numpy as np

src_data = {}
to_save_dict = {}
user_ids = []

src_path = r'../json_flies/indicators_of_four_dim_filtered.json'
outputs_path = r'../json_flies/7areas_score.json'
user_4cases_score = r'../json_flies/user_4cases_scores.json'

# 分题型来汇总所有的这些信息
all_dt = {"dim1": [], "dim2": [], "dim3": [], "dim4": []}
all_vl = {"dim1": [], "dim2": [], "dim3": [], "dim4": []}
all_mi = {"dim1": [], "dim2": [], "dim3": [], "dim4": []}
vl_avg = {"dim1": 0.0, "dim2": 0.0, "dim3": 0.0, "dim4": 0.0}
mi_avg = {"dim1": 0.0, "dim2": 0.0, "dim3": 0.0, "dim4": 0.0}
all_user_dt = [{"dim1": 0.0, "dim2": 0.0, "dim3": 0.0, "dim4": 0.0}]
# 形如[{"dim1": [[],[],[]]]
all_user_4_cases_3_areas_all_ = []


def main():
    with open(src_path, "r") as fp:
        global src_data, to_save_dict, user_ids, all_user_4_cases_3_areas_all_
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
        # 然后把之前算好的四种题型搞到这个要存到的地方
        with open(user_4cases_score, "r") as fff:
            u_4cases_score = json.load(fff)
            for each_id in user_ids:
                t1 = u_4cases_score[each_id]['dim1'] * 20
                if t1 > 100:
                    t1 = 100
                t2 = u_4cases_score[each_id]['dim2'] * 20
                if t2 > 100:
                    t2 = 100
                t3 = u_4cases_score[each_id]['dim3'] * 20
                if t3 > 100:
                    t3 = 100
                t4 = u_4cases_score[each_id]['dim4'] * 20
                if t4 > 100:
                    t4 = 100
                to_save_dict[each_id]['case1'] = t1
                to_save_dict[each_id]['case2'] = t2
                to_save_dict[each_id]['case3'] = t3
                to_save_dict[each_id]['case4'] = t4

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
            t = {'dim1': [case1_3areas[0], case1_3areas[1], case1_3areas[2]],
                 'dim2': [case2_3areas[0], case2_3areas[1], case2_3areas[2]],
                 'dim3': [case3_3areas[0], case3_3areas[1], case3_3areas[2]],
                 'dim4': [case4_3areas[0], case4_3areas[1], case4_3areas[2]]}
            all_user_4_cases_3_areas_all_.append(t)
        # 经过了上面的循环，完成了用户每个题型的所有题目的均值，这样作为该用户该题型该方面的分数
        print(all_user_4_cases_3_areas_all_)
        # 然后分别计算，总体的均分鸭，就不用算mi了鸭
        mean_vl_4cases_tool = [[], [], [], []]

        for one_user_score in all_user_4_cases_3_areas_all_:
            mean_vl_4cases_tool[0].extend(one_user_score['dim1'][1])
            mean_vl_4cases_tool[1].extend(one_user_score['dim2'][1])
            mean_vl_4cases_tool[2].extend(one_user_score['dim3'][1])
            mean_vl_4cases_tool[3].extend(one_user_score['dim4'][1])
        # 这个均分是所有人所有属于该类型题目的均分
        mean_4_cases_vl = [np.mean(mean_vl_4cases_tool[0]), np.mean(mean_vl_4cases_tool[1]),
                           np.mean(mean_vl_4cases_tool[2]), np.mean(mean_vl_4cases_tool[3])]
        # 下面要算出该用户，该题型，该方面的分数
        print(mean_4_cases_vl)
        # 形如[{"dim1": [99,2,3], "dim2": [1,2,3], "dim3": [1,2,3], "dim4": [1,2,3]} ]
        all_score_4cases_3areas = []
        for i in range(len(all_user_4_cases_3_areas_all_)):
            init_data = all_user_4_cases_3_areas_all_[i]
            t = {"dim1": [], "dim2": [], "dim3": [], "dim4": []}
            # 搞dt
            tmp_dt = []
            for e_time in init_data['dim1'][0]:
                if e_time < 30 * 60:
                    tmp_dt.append(1)
                else:
                    tmp_dt.append(1 - ((e_time - 1800) / (24 * 60 * 60)))
            t['dim1'].append(np.mean(tmp_dt) * 100)

            tmp_dt = []
            for e_time in init_data['dim2'][0]:
                if e_time < 30 * 60:
                    tmp_dt.append(1)
                else:
                    tmp_dt.append(1 - ((e_time - 1800) / (24 * 60 * 60)))
            t['dim2'].append(np.mean(tmp_dt) * 100)

            tmp_dt = []
            for e_time in init_data['dim3'][0]:
                if e_time < 30 * 60:
                    tmp_dt.append(1)
                else:
                    tmp_dt.append(1 - ((e_time - 1800) / (24 * 60 * 60)))
            t['dim3'].append(np.mean(tmp_dt) * 100)

            tmp_dt = []
            for e_time in init_data['dim4'][0]:
                if e_time < 30 * 60:
                    tmp_dt.append(1)
                else:
                    tmp_dt.append(1 - ((e_time - 1800) / (24 * 60 * 60)))
            t['dim4'].append(np.mean(tmp_dt) * 100)

            # 搞vl
            tmp_vl = []
            for e_vl in init_data['dim1'][1]:
                tmp_vl.append(mean_4_cases_vl[0] / e_vl)
            t['dim1'].append(np.mean(tmp_vl))

            tmp_vl = []
            for e_vl in init_data['dim1'][1]:
                tmp_vl.append(mean_4_cases_vl[1] / e_vl)
            t['dim2'].append(np.mean(tmp_vl))

            tmp_vl = []
            for e_vl in init_data['dim1'][1]:
                tmp_vl.append(mean_4_cases_vl[2] / e_vl)
            t['dim3'].append(np.mean(tmp_vl))

            tmp_vl = []
            for e_vl in init_data['dim1'][1]:
                tmp_vl.append(mean_4_cases_vl[3] / e_vl)
            t['dim4'].append(np.mean(tmp_vl))

            # 最简单的mi
            t['dim1'].append(np.mean(init_data['dim1'][2]))
            t['dim2'].append(np.mean(init_data['dim2'][2]))
            t['dim3'].append(np.mean(init_data['dim3'][2]))
            t['dim4'].append(np.mean(init_data['dim4'][2]))
            all_score_4cases_3areas.append(t)
        print(all_score_4cases_3areas)

        # 下面是四种题型分比例
        for i in range(len(all_score_4cases_3areas)):
            i_4cases_3areas = all_score_4cases_3areas[i]
            user_id = user_ids[i]
            to_save_dict[user_id]['dt_score'] = (i_4cases_3areas['dim1'][0] * 1 + i_4cases_3areas['dim2'][0] * 1 +
                                                 i_4cases_3areas['dim3'][0] * 1 + i_4cases_3areas['dim4'][0] * 1) / (
                                                        1 + 1 + 1 + 1)

            to_save_dict[user_id]['vl_score'] = (i_4cases_3areas['dim1'][1] * 1 + i_4cases_3areas['dim2'][1] * 1 +
                                                 i_4cases_3areas['dim3'][1] * 1 + i_4cases_3areas['dim4'][1] * 1) / (
                                                        1 + 1 + 1 + 1) * 40
            if to_save_dict[user_id]['vl_score'] > 100:
                to_save_dict[user_id]['vl_score'] = 100

            to_save_dict[user_id]['mi_score'] = (i_4cases_3areas['dim1'][2] * 1 + i_4cases_3areas['dim2'][2] * 1 +
                                                 i_4cases_3areas['dim3'][2] * 1 + i_4cases_3areas['dim4'][2] * 1) / (
                                                        1 + 1 + 1 + 1)

        with open(outputs_path, 'w+') as r:
            # 定义为写模式，名称定义为r
            json.dump(to_save_dict, r, indent=4)
            # 将dict写入名称为r的文件中
            r.close()


if __name__ == "__main__":
    main()
