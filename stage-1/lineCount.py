import json

src_path = ''
ans_path = ''


def open_file(filename, mode='r'):
    return open(filename, mode, encoding='utf-8', errors='ignore')


def get_line_from_file(filename):
    line_list = []
    with open_file(filename) as f:
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


def write_json_data(tmp):
    # 写入json文件

    with open(ans_path, 'w') as r:
        # 定义为写模式，名称定义为r

        json.dump(tmp, r, indent=4)
        # count写入名称为r的文件中

    r.close()
    # 关闭json写模式


write_json_data(get_line_from_file(src_path))
