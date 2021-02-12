import os

def main():
    # 开始
    print('-- playlist_set v0.1 --\n')

    # 指定生成的文件格式，默认 m3u
    file_format = 'm3u'

    # 功能选择
    print('1，生成指定目录的播放列表\n')
    go = input('选择需要的功能：')

    if go == '1': one_path(file_format)
    else: pass

def one_path(file_format):
    path = input('请输入操作路径：')
    # path = 'D:\\temp\\t'
    if file_format == 'm3u': print_m3u(path)
    else: pass

# 模块分割 --------------------------

def print_m3u(path):
    with os.scandir(path) as files:
        for file in files:
            print(file.name)

if __name__ == "__main__":
    main()