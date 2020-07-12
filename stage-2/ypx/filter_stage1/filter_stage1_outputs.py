import json

src_path = r"E:\0000ProfessionalClass\2_2nd\SMSE\OnGitHub\BigJob\indicators_of_four_dim.json"
ans_path = r"E:\Desktop\indicators_of_four_dim_filtered.json"
with open(src_path, "r") as fp:
    src_data = json.load(fp)
    user_ids = list(src_data.keys())
    users_to_del = []
    for each_id in user_ids:
        # 这样赋值的话前面是后面的引用
        dims_of_the_id = src_data[each_id]
        cases_to_del_of_the_id = []
        to_del = False
        for each_dim in ['dim1', 'dim2', 'dim3', 'dim4']:
            cases_of_the_dim = dims_of_the_id[each_dim]
            if len(cases_of_the_dim) >= 5:
                index_of_case_to_del = []
                for each_case_index in range(len(cases_of_the_dim)):
                    # 超过24小时 or 0行 or mi100
                    if cases_of_the_dim[each_case_index][1] > 24 * 60 * 60 or cases_of_the_dim[each_case_index][2] == 0 \
                            or cases_of_the_dim[each_case_index][3] - 100 == 0:
                        index_of_case_to_del.append(each_case_index)
                index_of_case_to_del.sort(reverse=True)
                for del_index in index_of_case_to_del:
                    del cases_of_the_dim[del_index]
        # 每项删完之后再看看要不要删除用户
        for each_dim in ['dim1', 'dim2', 'dim3', 'dim4']:
            cases_of_the_dim = dims_of_the_id[each_dim]
            if len(cases_of_the_dim) < 5:
                # 这个用户不具备其中一项能力，删掉
                to_del = True
        if to_del:
            users_to_del.append(each_id)

    print(users_to_del)
    # print(src_data)
    for del_user_id in users_to_del:
        del src_data[del_user_id]
    fp.close()
    # 删完了，存下
    with open(ans_path, 'w') as r:
        # 定义为写模式，名称定义为r

        json.dump(src_data, r, indent=4)
        # 将dict写入名称为r的文件中

    r.close()
