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

# 业务模块 --------------------------

def one_path(file_format):
    path = input('请输入操作路径：')
    # path = 'D:\\temp\\t'
    if file_format == 'm3u': print_m3u(path)
    else: pass

# 功能模块 --------------------------

def print_m3u(path):
    path_out = path + 'playlist.m3u'
    
    m3u = open(path_out, "w")
    m3u.write('#EXTM3U\n')

    with os.scandir(path) as files:
        for file in files:
            m3u.write('#EXTINF:-1,\n')
            m3u.write(file.name + '\n')
    
    m3u.close

# 辅助模块 --------------------------

## 格式化路径
def path_fix(path):
    ### if path[]
    
    return path

if __name__ == "__main__":
    main()