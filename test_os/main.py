import os


def path_example():
    abs_path = os.path.abspath(__file__)
    print(abs_path)
    re_path = os.path.dirname(__file__)
    print(re_path)
    # 相对路径
    path = os.path.join(re_path, '../my-django')
    print(os.listdir(path))


def file_example():
    path = os.path.join(os.path.dirname(__file__),
                        '../my-django/drf/tutorial/tutorial/quickstart')
    print(os.listdir(path))


def scan_file_name(path):
    file = os.listdir(path)
    result = []
    for f in file:
        is_dir = os.path.join(path, f)
        if os.path.isdir(is_dir):
            continue
        result.append(is_dir)
    return result

def rename_folder_name(dir):
    os.rename(dir)


if __name__ == '__main__':
    app_path = os.path.join(os.path.dirname(__file__),
                        '../my-django/drf/tutorial/tutorial/quickstart')
    os.rename(app_path,'myapp')
